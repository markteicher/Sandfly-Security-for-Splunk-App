#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# File: bin/sandfly_input.py
# Sandfly Security for Splunk App
#
# Purpose:
# - Authenticate to Sandfly API
# - Validate credentials and role permissions
# - Enforce operational correctness
#
# Design principles:
# - Read-only API usage
# - Explicit failure phases
# - Clear, user-facing errors
# - Splunk-supported logging levels ONLY
# =============================================================================

import sys
import time
from typing import Any, Dict, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

import splunklib.modularinput as smi


REQUIRED_ROLES = {"admin", "api_result_read", "api_scan"}
DEFAULT_TIMEOUT = 60


# -----------------------------------------------------------------------------#
# Logging helper
# -----------------------------------------------------------------------------#
def log(log_fn, level, msg):
    log_fn(level, msg)


# -----------------------------------------------------------------------------#
# Sandfly API Client
# -----------------------------------------------------------------------------#
class SandflyAPI:
    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        log_fn,
        verify_ssl: bool = True,
        timeout: int = DEFAULT_TIMEOUT,
        proxy_url: Optional[str] = None,
        proxy_user: Optional[str] = None,
        proxy_pass: Optional[str] = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.timeout = timeout
        self.log_fn = log_fn

        self.access_token = None
        self.refresh_token = None
        self.token_expiry = 0

        self.session = requests.Session()
        self.session.verify = verify_ssl
        self.session.headers.update({"Accept": "application/json"})

        retry = Retry(
            total=5,
            backoff_factor=1,
            status_forcelist=(429, 500, 502, 503, 504),
            allowed_methods=["GET", "POST"],
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retry))

        if proxy_url:
            proxy = proxy_url
            if proxy_user and proxy_pass:
                proxy = proxy_url.replace("://", f"://{proxy_user}:{proxy_pass}@", 1)
            self.session.proxies = {"http": proxy, "https": proxy}

        self.authenticate()

    # -------------------------------------------------------------------------#
    # Authentication
    # -------------------------------------------------------------------------#
    def authenticate(self):
        log(self.log_fn, smi.LogLevel.INFO, "Authenticating to Sandfly API")

        url = f"{self.base_url}/v4/auth/login"
        payload = {
            "username": self.username,
            "password": self.password,
            "full_details": True,
        }

        try:
            resp = self.session.post(
                url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=self.timeout,
            )
        except Exception as e:
            raise RuntimeError(f"Unable to connect to Sandfly server: {e}")

        if resp.status_code == 401:
            raise RuntimeError("Authentication failed: invalid username or password")

        if resp.status_code != 200:
            raise RuntimeError(
                f"Authentication failed (HTTP {resp.status_code}): {resp.text}"
            )

        data = resp.json()

        self.access_token = data.get("access_token")
        self.refresh_token = data.get("refresh_token")
        self.token_expiry = time.time() + 300

        if not self.access_token or not self.refresh_token:
            raise RuntimeError("Authentication response missing access or refresh token")

        self._validate_roles(data)

        log(self.log_fn, smi.LogLevel.INFO, "Authentication and role validation successful")

    # -------------------------------------------------------------------------#
    # Role validation
    # -------------------------------------------------------------------------#
    def _validate_roles(self, auth_response: Dict[str, Any]):
        user = auth_response.get("user")
        if not user:
            raise RuntimeError("Authentication response missing user details")

        roles = set(user.get("roles", []))
        if not roles:
            raise RuntimeError("User account has no roles assigned")

        if not roles.intersection(REQUIRED_ROLES):
            raise RuntimeError(
                "Insufficient permissions: account must have at least ONE of "
                + ", ".join(sorted(REQUIRED_ROLES))
            )

        log(
            self.log_fn,
            smi.LogLevel.INFO,
            f"Validated roles: {', '.join(sorted(roles))}",
        )

    # -------------------------------------------------------------------------#
    # Headers
    # -------------------------------------------------------------------------#
    def headers(self) -> Dict[str, str]:
        if time.time() >= self.token_expiry:
            self.refresh()
        return {"Authorization": f"Bearer {self.access_token}"}

    # -------------------------------------------------------------------------#
    # Token refresh
    # -------------------------------------------------------------------------#
    def refresh(self):
        log(self.log_fn, smi.LogLevel.INFO, "Refreshing Sandfly API token")

        url = f"{self.base_url}/v4/auth/refresh"
        resp = self.session.post(
            url,
            headers={"Authorization": f"Bearer {self.refresh_token}"},
            timeout=self.timeout,
        )

        if resp.status_code != 200:
            raise RuntimeError("Token refresh failed")

        data = resp.json()
        self.access_token = data.get("access_token")
        self.refresh_token = data.get("refresh_token")
        self.token_expiry = time.time() + 300

    # -------------------------------------------------------------------------#
    # GET wrapper
    # -------------------------------------------------------------------------#
    def get(self, path: str) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        resp = self.session.get(url, headers=self.headers(), timeout=self.timeout)

        if resp.status_code == 401:
            self.refresh()
            resp = self.session.get(url, headers=self.headers(), timeout=self.timeout)

        if resp.status_code != 200:
            raise RuntimeError(
                f"API GET failed ({path}): HTTP {resp.status_code}"
            )

        return resp.json()


# -----------------------------------------------------------------------------#
# Splunk Modular Input
# -----------------------------------------------------------------------------#
class SandflyInput(smi.Script):
    def get_scheme(self):
        scheme = smi.Scheme("Sandfly Security Input")
        scheme.use_external_validation = True

        scheme.add_argument(smi.Argument("sandfly_url", "Sandfly URL", smi.Argument.data_type_string, True))
        scheme.add_argument(smi.Argument("username", "Username", smi.Argument.data_type_string, True))
        scheme.add_argument(smi.Argument("password", "Password", smi.Argument.data_type_string, True, encrypted=True))
        scheme.add_argument(smi.Argument("verify_ssl", "Verify SSL", smi.Argument.data_type_boolean, False))
        scheme.add_argument(smi.Argument("timeout", "Timeout", smi.Argument.data_type_number, False))
        scheme.add_argument(smi.Argument("proxy_url", "Proxy URL", smi.Argument.data_type_string, False))
        scheme.add_argument(smi.Argument("proxy_user", "Proxy Username", smi.Argument.data_type_string, False))
        scheme.add_argument(smi.Argument("proxy_pass", "Proxy Password", smi.Argument.data_type_string, False, encrypted=True))

        return scheme

    # -------------------------------------------------------------------------#
    # Setup-time validation
    # -------------------------------------------------------------------------#
    def validate_input(self, definition):
        p = definition.parameters

        api = SandflyAPI(
            base_url=p["sandfly_url"],
            username=p["username"],
            password=p["password"],
            log_fn=lambda *_: None,
            verify_ssl=p.get("verify_ssl", True),
            timeout=int(p.get("timeout") or DEFAULT_TIMEOUT),
            proxy_url=p.get("proxy_url"),
            proxy_user=p.get("proxy_user"),
            proxy_pass=p.get("proxy_pass"),
        )

        # Explicit API reachability check
        api.get("/v4/version")

    # -------------------------------------------------------------------------#
    # Runtime
    # -------------------------------------------------------------------------#
    def stream_events(self, inputs, ew):
        log(ew.log, smi.LogLevel.INFO, "Sandfly input started")

        for stanza, cfg in inputs.inputs.items():
            params = cfg["params"]

            SandflyAPI(
                base_url=params["sandfly_url"],
                username=params["username"],
                password=params["password"],
                log_fn=ew.log,
                verify_ssl=params.get("verify_ssl", True),
                timeout=int(params.get("timeout") or DEFAULT_TIMEOUT),
                proxy_url=params.get("proxy_url"),
                proxy_user=params.get("proxy_user"),
                proxy_pass=params.get("proxy_pass"),
            )

            log(ew.log, smi.LogLevel.INFO, f"Input stanza '{stanza}' initialized")

        log(ew.log, smi.LogLevel.INFO, "Sandfly input completed successfully")


if __name__ == "__main__":
    sys.exit(SandflyInput().run(sys.argv))

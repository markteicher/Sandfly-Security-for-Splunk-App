#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: bin/sandfly_input.py
# -------------------------------------------------------------------------
# Sandfly Security for Splunk App – Modular Input
#
# Authentication:
#   POST /v4/auth/login
#
# Role enforcement:
#   Requires one of:
#     - admin
#     - api_result_read
#     - api_scan
# -------------------------------------------------------------------------

import json
import os
import sys
import time
from typing import Any, Dict, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

import splunklib.modularinput as smi


def load_checkpoint(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return {}


def save_checkpoint(path: str, data: Dict[str, Any]) -> None:
    tmp = f"{path}.tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh)
    os.replace(tmp, path)


def to_json(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False, default=str)


class SandflyAPI:
    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        log,
        verify_ssl: bool = True,
        timeout: int = 60,
        proxy_url: Optional[str] = None,
        proxy_user: Optional[str] = None,
        proxy_pass: Optional[str] = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.username = username
        self.password = password
        self.timeout = timeout
        self.log = log

        self.access_token = None
        self.refresh_token = None
        self.token_expiry = 0
        self.roles = []

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
                proxy = proxy_url.replace(
                    "://", f"://{proxy_user}:{proxy_pass}@", 1
                )
            self.session.proxies = {"http": proxy, "https": proxy}

        self.login()
        self.validate_roles()

    def login(self) -> None:
        self.log(smi.LogLevel.INFO, "Authenticating to Sandfly API")

        url = f"{self.base_url}/v4/auth/login"
        resp = self.session.post(
            url,
            json={
                "username": self.username,
                "password": self.password,
                "full_details": True,
            },
            headers={"content-type": "application/json"},
            timeout=self.timeout,
        )
        resp.raise_for_status()

        data = resp.json()

        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        self.token_expiry = time.time() + 300

        user = data.get("user", {})
        self.roles = user.get("roles", [])

    def validate_roles(self) -> None:
        required = {"admin", "api_result_read", "api_scan"}
        actual = set(self.roles or [])

        if not actual.intersection(required):
            raise RuntimeError(
                "Sandfly authentication succeeded, but the account lacks required API permissions.\n\n"
                "Required role(s): admin OR api_result_read OR api_scan\n"
                f"Account roles detected: {sorted(actual)}\n\n"
                "Assign one of the required roles in Sandfly and re-run setup."
            )

    def refresh(self) -> None:
        self.log(smi.LogLevel.INFO, "Refreshing Sandfly API token")
        url = f"{self.base_url}/v4/auth/refresh"
        resp = self.session.post(
            url,
            headers={"Authorization": f"Bearer {self.refresh_token}"},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        self.token_expiry = time.time() + 300

    def headers(self) -> Dict[str, str]:
        if time.time() >= self.token_expiry:
            self.refresh()
        return {"Authorization": f"Bearer {self.access_token}"}

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        resp = self.session.get(
            url,
            headers=self.headers(),
            params=params or {},
            timeout=self.timeout,
        )
        if resp.status_code == 401:
            self.refresh()
            resp = self.session.get(
                url,
                headers=self.headers(),
                params=params or {},
                timeout=self.timeout,
            )
        resp.raise_for_status()
        return resp.json()


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

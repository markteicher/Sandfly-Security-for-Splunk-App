#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# File: bin/sandfly_validation.py
# Sandfly Security for Splunk App
#
# Purpose:
# - Validate modular input configuration at setup time
# - Authenticate to Sandfly
# - Enforce required role permissions
# - Verify API reachability (GET /v4/version)
#
# Design constraints:
# - Validation only (no data collection)
# - Read-only API calls
# - No stdout printing
# - Raise explicit, user-facing errors
# - Splunk AppInspect compliant
# =============================================================================

import requests

# At least ONE of these roles is required
REQUIRED_ROLES = {
    "admin",
    "api_result_read",
    "api_scan",
}


def validate_input(definition):
    """
    Splunk validation handler.
    Called before the modular input is enabled.
    """
    params = definition.parameters

    sandfly_url = params.get("sandfly_url")
    username = params.get("username")
    password = params.get("password")

    verify_ssl = params.get("verify_ssl", True)
    timeout = int(params.get("timeout") or 60)

    proxy_url = params.get("proxy_url")
    proxy_user = params.get("proxy_user")
    proxy_pass = params.get("proxy_pass")

    # ------------------------------------------------------------------
    # Basic parameter validation
    # ------------------------------------------------------------------
    if not sandfly_url:
        raise ValueError("Sandfly URL is required")

    if not username or not password:
        raise ValueError("Username and password are required")

    # ------------------------------------------------------------------
    # Session setup
    # ------------------------------------------------------------------
    session = requests.Session()
    session.verify = verify_ssl
    session.headers.update({"Accept": "application/json"})

    # Proxy handling
    if proxy_url:
        proxy = proxy_url
        if proxy_user and proxy_pass:
            proxy = proxy_url.replace(
                "://", f"://{proxy_user}:{proxy_pass}@", 1
            )
        session.proxies = {
            "http": proxy,
            "https": proxy,
        }

    # ------------------------------------------------------------------
    # Authenticate (POST /v4/auth/login)
    # ------------------------------------------------------------------
    login_url = f"{sandfly_url.rstrip('/')}/v4/auth/login"
    payload = {
        "username": username,
        "password": password,
        "full_details": True,
    }

    try:
        resp = session.post(
            login_url,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=timeout,
        )
    except Exception as e:
        raise ValueError(f"Unable to connect to Sandfly server: {e}")

    if resp.status_code == 401:
        raise ValueError("Authentication failed: invalid username or password")

    if resp.status_code != 200:
        raise ValueError(
            f"Authentication failed (HTTP {resp.status_code}): {resp.text}"
        )

    data = resp.json()

    access_token = data.get("access_token")
    if not access_token:
        raise ValueError(
            "Authentication succeeded but no access token was returned"
        )

    # ------------------------------------------------------------------
    # Role validation
    # ------------------------------------------------------------------
    user = data.get("user")
    if not user:
        raise ValueError(
            "Authentication response missing user details; cannot validate roles"
        )

    roles = set(user.get("roles", []))
    if not roles:
        raise ValueError("User account has no roles assigned")

    if not roles.intersection(REQUIRED_ROLES):
        raise ValueError(
            "Insufficient permissions: account must have at least ONE of the "
            "following roles: "
            + ", ".join(sorted(REQUIRED_ROLES))
        )

    # ------------------------------------------------------------------
    # API reachability check (GET /v4/version)
    # ------------------------------------------------------------------
    version_url = f"{sandfly_url.rstrip('/')}/v4/version"
    resp = session.get(
        version_url,
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=timeout,
    )

    if resp.status_code != 200:
        raise ValueError(
            f"Sandfly API validation failed (/v4/version): "
            f"HTTP {resp.status_code}"
        )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
# File: bin/sandfly_setup_handler.py
# Sandfly Security for Splunk App
#
# Purpose:
# - Validate Sandfly connectivity during app setup
# - Authenticate and verify role permissions
# - Verify API reachability
# - Store configuration only (no ingestion)
#
# Design constraints:
# - Setup-time validation only
# - Read-only API calls
# - No stdout printing
# - Explicit error reporting
# - Splunk AppInspect compliant
# =============================================================================

import requests
from splunklib.binding import HTTPError
from splunklib.modularinput import LogLevel


REQUIRED_ROLES = {"admin", "api_result_read", "api_scan"}


def validate_sandfly_connection(
    sandfly_url,
    username,
    password,
    verify_ssl=True,
    timeout=60,
    proxy_url=None,
    proxy_user=None,
    proxy_pass=None,
):
    if not sandfly_url:
        raise ValueError("Sandfly URL is required")

    if not username or not password:
        raise ValueError("Username and password are required")

    session = requests.Session()
    session.verify = verify_ssl
    session.headers.update({"Accept": "application/json"})

    if proxy_url:
        proxy = proxy_url
        if proxy_user and proxy_pass:
            proxy = proxy_url.replace(
                "://", f"://{proxy_user}:{proxy_pass}@", 1
            )
        session.proxies = {"http": proxy, "https": proxy}

    # -------------------------------------------------------------------------
    # Authenticate
    # -------------------------------------------------------------------------
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
            f"Authentication failed: HTTP {resp.status_code} - {resp.text}"
        )

    data = resp.json()

    access_token = data.get("access_token")
    if not access_token:
        raise ValueError("Authentication succeeded but no access token was returned")

    # -------------------------------------------------------------------------
    # Role validation
    # -------------------------------------------------------------------------
    user = data.get("user")
    if not user:
        raise ValueError("Authentication response missing user details")

    roles = set(user.get("roles", []))
    if not roles:
        raise ValueError("User has no roles assigned")

    if not roles.intersection(REQUIRED_ROLES):
        raise ValueError(
            "Insufficient permissions: account must have at least one of "
            + ", ".join(sorted(REQUIRED_ROLES))
        )

    # -------------------------------------------------------------------------
    # API reachability check
    # -------------------------------------------------------------------------
    version_url = f"{sandfly_url.rstrip('/')}/v4/version"
    resp = session.get(
        version_url,
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=timeout,
    )

    if resp.status_code != 200:
        raise ValueError(
            f"Sandfly API validation failed (/v4/version): HTTP {resp.status_code}"
        )

    return resp.json()


def setup_handler(request):
    try:
        config = request["form"]

        sandfly_url = config.get("sandfly_url")
        username = config.get("username")
        password = config.get("password")

        verify_ssl = config.get("verify_ssl", "true").lower() == "true"
        timeout = int(config.get("timeout") or 60)

        proxy_url = config.get("proxy_url")
        proxy_user = config.get("proxy_user")
        proxy_pass = config.get("proxy_pass")

        validate_sandfly_connection(
            sandfly_url=sandfly_url,
            username=username,
            password=password,
            verify_ssl=verify_ssl,
            timeout=timeout,
            proxy_url=proxy_url,
            proxy_user=proxy_user,
            proxy_pass=proxy_pass,
        )

        return {
            "status": "success",
            "message": "Successfully validated Sandfly API connectivity and permissions",
        }

    except HTTPError as e:
        return {
            "status": "error",
            "message": f"Splunk HTTP error: {str(e)}",
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }

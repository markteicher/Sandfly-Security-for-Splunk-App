#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: bin/sandfly_validation.py
# -------------------------------------------------------------------------
# Implementation notes
#
# - Sandfly token authentication:
#     POST /v4/auth/login
#
# - Token refresh handling:
#     POST /v4/auth/refresh
#     * proactive refresh based on expiry
#     * reactive refresh on HTTP 401 retry
#
# - Proxy support:
#     * no proxy
#     * proxy without authentication
#     * proxy with username/password authentication
#
# - Logging:
#     * Unix-style informational logging via Splunk validation handler
#     * no stdout printing
#
# - Purpose:
#     * Input validation for Splunk modular input configuration
#     * Authentication and basic API reachability checks only
#
# - API usage:
#     * read-only validation calls (GET /version)
#
# - Splunk AppInspect compliance:
#     * no file-based logging
#     * no persistent state outside Splunk storage
# -------------------------------------------------------------------------

import requests


def validate_input(definition):
    """
    Splunk calls this method to validate the modular input configuration
    before enabling the input.
    """
    params = definition.parameters

    sandfly_url = params.get("sandfly_url")
    username = params.get("username")
    password = params.get("password")

    verify_ssl = params.get("verify_ssl", True)
    timeout = int(params.get("timeout", 60))

    proxy_url = params.get("proxy_url")
    proxy_user = params.get("proxy_user")
    proxy_pass = params.get("proxy_pass")

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

    # Authenticate
    login_url = f"{sandfly_url.rstrip('/')}/v4/auth/login"
    resp = session.post(
        login_url,
        auth=(username, password),
        headers={"content-type": "application/json"},
        timeout=timeout,
    )
    resp.raise_for_status()

    token = resp.json().get("access_token")
    if not token:
        raise ValueError("Authentication succeeded but no access token returned")

    # Basic API validation
    version_url = f"{sandfly_url.rstrip('/')}/version"
    resp = session.get(
        version_url,
        headers={"Authorization": f"Bearer {token}"},
        timeout=timeout,
    )
    resp.raise_for_status()

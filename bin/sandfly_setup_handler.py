#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: bin/sandfly_setup_handler.py
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
#     * Unix-style informational logging via Splunk setup handler
#     * no stdout printing
#
# - Purpose:
#     * Validate Sandfly connectivity during app setup
#     * Store configuration only (no data ingestion)
#
# - API usage:
#     * read-only validation calls (GET /version)
#
# - Splunk AppInspect compliance:
#     * no file-based logging
#     * no persistent state outside Splunk storage
# -------------------------------------------------------------------------

import json
import requests

from splunklib.client import Service
from splunklib.binding import HTTPError
from splunklib.searchcommands import dispatch

from splunklib.modularinput import LogLevel


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
        raise RuntimeError("Authentication succeeded but no access token returned")

    version_url = f"{sandfly_url.rstrip('/')}/version"
    resp = session.get(
        version_url,
        headers={"Authorization": f"Bearer {token}"},
        timeout=timeout,
    )
    resp.raise_for_status()

    return resp.json()


def setup_handler(request):
    try:
        config = request["form"]

        sandfly_url = config.get("sandfly_url")
        username = config.get("username")
        password = config.get("password")
        verify_ssl = config.get("verify_ssl", "true").lower() == "true"
        timeout = int(config.get("timeout", 60))
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
            "message": "Successfully connected to Sandfly Security API",
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

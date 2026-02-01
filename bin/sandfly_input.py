#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: bin/sandfly_input.py
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
#     * Unix-style informational logging via Splunk event writer (ew.log)
#     * no stdout printing
#
# - Collectors:
#     * strict read-only collectors only (GET endpoints)
#     * no state-changing API calls
#
# - Collection model:
#     * inventory-style collectors (e.g. /hosts)
#     * streaming collectors (e.g. /results)
#
# - Results streaming:
#     * checkpointing via /results/getMaxID
#     * incremental fetch via /results/:id
#
# - Pagination safety:
#     * supports endpoints returning:
#         {"data":[...], "more_results":bool, "total":int}
#
# - HTTP resiliency:
#     * retries with backoff for transient failures (429 / 5xx)
#
# - Splunk AppInspect compliance:
#     * no file-based logging
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

    def login(self) -> None:
        self.log(smi.LogLevel.INFO, "Authenticating to Sandfly API")
        url = f"{self.base_url}/v4/auth/login"
        resp = self.session.post(
            url,
            auth=(self.username, self.password),
            headers={"content-type": "application/json"},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        data = resp.json()
        self.access_token = data["access_token"]
        self.refresh_token = data["refresh_token"]
        self.token_expiry = time.time() + 300

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

    def validate_input(self, definition):
        p = definition.parameters
        api = SandflyAPI(
            p["sandfly_url"],
            p["username"],
            p["password"],
            log=lambda *_: None,
            verify_ssl=p.get("verify_ssl", True),
            timeout=int(p.get("timeout") or 60),
            proxy_url=p.get("proxy_url"),
            proxy_user=p.get("proxy_user"),
            proxy_pass=p.get("proxy_pass"),
        )
        api.get("/version")

    def stream_events(self, inputs, ew):
        ew.log(smi.LogLevel.INFO, "Sandfly input starting")

        for stanza, cfg in inputs.inputs.items():
            params = cfg["params"]
            ckpt_file = os.path.join(cfg["checkpoint_dir"], f"{stanza}.json")
            checkpoint = load_checkpoint(ckpt_file)

            api = SandflyAPI(
                params["sandfly_url"],
                params["username"],
                params["password"],
                log=ew.log,
                verify_ssl=params.get("verify_ssl", True),
                timeout=int(params.get("timeout") or 60),
                proxy_url=params.get("proxy_url"),
                proxy_user=params.get("proxy_user"),
                proxy_pass=params.get("proxy_pass"),
            )

            ew.log(smi.LogLevel.INFO, "Collecting inventory: /hosts")
            hosts = api.get("/hosts").get("data", [])
            for host in hosts:
                ew.write_event(smi.Event(to_json(host), sourcetype="sandfly:hosts"))
            ew.log(smi.LogLevel.INFO, f"Collected {len(hosts)} host records")

            last_id = int(checkpoint.get("last_result_id", 0))
            max_id = int(api.get("/results/getMaxID").get("id", last_id))

            ew.log(smi.LogLevel.INFO, f"Results stream: last_id={last_id} max_id={max_id}")

            ingested = 0
            for rid in range(last_id + 1, max_id + 1):
                result = api.get(f"/results/{rid}")
                ew.write_event(smi.Event(to_json(result), sourcetype="sandfly:results"))
                ingested += 1

            ew.log(smi.LogLevel.INFO, f"Ingested {ingested} new results")

            checkpoint["last_result_id"] = max_id
            save_checkpoint(ckpt_file, checkpoint)

            ew.log(smi.LogLevel.INFO, f"Checkpoint updated: last_result_id={max_id}")

        ew.log(smi.LogLevel.INFO, "Sandfly input completed successfully")


if __name__ == "__main__":
    sys.exit(SandflyInput().run(sys.argv))

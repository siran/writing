# .scripts/zenodo_api.py
import os
import json
import time
import traceback
from typing import Dict, List, Tuple, Optional

import requests  # assumes installed

from common import echo, die

MIN_REQUEST_INTERVAL = float(os.environ.get("ZENODO_MIN_REQUEST_INTERVAL", "1.0"))
RETRY_FOREVER_INTERVAL = float(os.environ.get("ZENODO_RETRY_FOREVER_INTERVAL", "3.0"))
_LAST_REQUEST_TS = 0.0
DEFAULT_USER_AGENT = os.environ.get(
    "ZENODO_USER_AGENT",
    "preferredframe-publish/1.0 (https://github.com/siran/writing)",
)


def _throttle_request():
    if MIN_REQUEST_INTERVAL <= 0:
        return
    global _LAST_REQUEST_TS
    now = time.monotonic()
    wait = _LAST_REQUEST_TS + MIN_REQUEST_INTERVAL - now
    if wait > 0:
        try:
            time.sleep(wait)
        except KeyboardInterrupt:
            pass


def _mark_request_time():
    global _LAST_REQUEST_TS
    _LAST_REQUEST_TS = time.monotonic()


def _log_429_headers(headers):
    keys = [
        "Retry-After",
        "X-RateLimit-Reset",
        "X-RateLimit-Limit",
        "X-RateLimit-Remaining",
    ]
    parts = [f"{k}={headers.get(k)}" for k in keys if headers.get(k) is not None]
    if parts:
        echo(f"[WARN] 429 response headers: {', '.join(parts)}")


def _log_non2xx_headers(r):
    try:
        if not r.ok:
            echo(f"[WARN] Non-2xx response headers ({r.status_code}): {dict(r.headers)}")
    except Exception:
        pass


def zenodo_api_and_token(env: str) -> Tuple[str, str]:
    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        die("Missing ZENODO_TOKEN for Zenodo API.")

    api = os.environ.get("ZENODO_SANDBOX_API", "https://sandbox.zenodo.org/api")
    if env == "prod":
        api = os.environ.get("ZENODO_API", "https://zenodo.org/api")

    return api, token


def _auth_headers(token: str) -> Dict[str, str]:
    return {"Authorization": f"Bearer {token}", "User-Agent": DEFAULT_USER_AGENT}


def _rate_limit_delay(headers) -> Optional[float]:
    reset = headers.get("X-RateLimit-Reset")
    try:
        if reset is not None:
            reset_ts = float(reset)
            now = time.time()
            if reset_ts > now:
                return max(0.0, reset_ts - now)
    except Exception:
        pass
    retry_after = headers.get("Retry-After")
    try:
        if retry_after is not None:
            return float(retry_after)
    except Exception:
        pass
    return None


def http_put_raw(url: str, token: str, fp):
    echo(f"+ HTTP PUT (raw) {url}")
    headers = _auth_headers(token)
    start_pos = None
    try:
        start_pos = fp.tell()
    except Exception:
        start_pos = None
    while True:
        if start_pos is not None:
            try:
                fp.seek(start_pos)
            except Exception:
                pass
        _throttle_request()
        try:
            r = requests.put(url, data=fp, headers=headers)
        except requests.exceptions.RequestException as e:
            _mark_request_time()
            delay = max(RETRY_FOREVER_INTERVAL, 0.0)
            echo(
                f"[WARN] Bucket PUT exception {type(e).__name__}: {e}; "
                f"retrying in {delay}s..."
            )
            try:
                time.sleep(delay)
            except KeyboardInterrupt:
                raise
            continue
        _mark_request_time()
        _log_non2xx_headers(r)
        if r.ok:
            return r.json() if "application/json" in (r.headers.get("Content-Type", "")) else {}
        wait = _rate_limit_delay(r.headers)
        if r.status_code == 429:
            try:
                echo(f"[WARN] 429 response body:\n{r.text}")
            except Exception:
                pass
            try:
                _log_429_headers(r.headers)
            except Exception:
                pass
        if r.status_code in {429, 500, 502, 503, 504}:
            delay = max(RETRY_FOREVER_INTERVAL, 0.0)
            wait_time = max(delay, wait) if wait is not None else delay
            echo(f"[WARN] Bucket PUT {r.status_code} at {url}; retrying in {wait_time}s...")
            try:
                time.sleep(wait_time)
            except KeyboardInterrupt:
                raise
            continue
        try:
            print(r.text)
        except Exception:
            pass
        die(f"Zenodo bucket PUT error {r.status_code} at {url}")


def http_json(method: str, url: str, token: str, data=None, files=None) -> Dict:
    echo(f"+ HTTP {method.upper()} {url}")
    headers = _auth_headers(token)
    print(f"{data=}")
    print(f"{files=}")
    while True:
        _throttle_request()
        try:
            if method.upper() in ("POST", "PUT", "PATCH"):
                r = requests.request(method, url, headers=headers, json=data, files=files)
            else:
                r = requests.request(method, url, headers=headers, params=data)
        except requests.exceptions.RequestException as e:
            _mark_request_time()
            delay = max(RETRY_FOREVER_INTERVAL, 0.0)
            echo(
                f"[WARN] Zenodo API exception {type(e).__name__}: {e}; "
                f"retrying in {delay}s..."
            )
            try:
                time.sleep(delay)
            except KeyboardInterrupt:
                raise
            continue
        _mark_request_time()
        _log_non2xx_headers(r)
        if r.ok:
            try:
                return r.json()
            except Exception:
                return {}
        retry_delay = _rate_limit_delay(r.headers)
        if r.status_code == 429:
            try:
                echo(f"[WARN] 429 response body:\n{r.text}")
            except Exception:
                pass
            try:
                _log_429_headers(r.headers)
            except Exception:
                pass
        if r.status_code in {429, 500, 502, 503, 504}:
            delay = max(RETRY_FOREVER_INTERVAL, 0.0)
            wait = max(delay, retry_delay) if retry_delay is not None else delay
            echo(f"[WARN] Zenodo API {r.status_code} at {url}; retrying in {wait}s...")
            try:
                time.sleep(wait)
            except KeyboardInterrupt:
                raise
            continue
        try:
            echo(r.text)
        except Exception:
            pass
        die(f"Zenodo API error {r.status_code} at {url}")


def reserve_deposition(
    api: str,
    token: str,
    title: str,
    creators: List[Dict],
    publication_year: str,
    community: str,
    journal: str,
    publication_type: str,
) -> Tuple[int, str, Optional[str]]:
    """
    Reserve a DOI on Zenodo with minimal metadata + prereserve_doi.
    Full metadata is sent later once final paths are known.
    """
    dep = http_json("POST", f"{api}/deposit/depositions", token, data={})

    try:
        print("\n--- DEBUG: Zenodo POST /deposit/depositions response ---")
        print(json.dumps(dep, indent=2, ensure_ascii=False))
    except Exception:
        traceback.print_exc()

    dep_id = dep.get("id")
    if not dep_id:
        die("Could not create deposition (no id).")

    minimal_meta = {
        "upload_type": "publication",
        "publication_type": publication_type,
        "title": title,
        "creators": creators,
        "journal_title": journal,
        "publisher": {"name": journal},
        "publication_year": publication_year,
        "communities": [{"identifier": community}],
        "prereserve_doi": True,
    }

    dep = http_json(
        "PUT",
        f"{api}/deposit/depositions/{dep_id}",
        token,
        data={"metadata": minimal_meta},
    )

    try:
        print(f"\n--- DEBUG: Zenodo PUT /deposit/depositions/{dep_id} response ---")
        print(json.dumps(dep, indent=2, ensure_ascii=False))
    except Exception:
        traceback.print_exc()

    pr = (dep.get("metadata") or {}).get("prereserve_doi") or {}
    reserved_doi = pr.get("doi")
    concept_doi = dep.get("conceptdoi")

    if not reserved_doi:
        die("Zenodo did not return a reserved DOI.")
    return dep_id, reserved_doi, concept_doi


def get_deposition(api: str, token: str, dep_id: int) -> Dict:
    return http_json("GET", f"{api}/deposit/depositions/{dep_id}", token)


def ensure_draft_or_die(api: str, token: str, dep_id: int) -> Dict:
    dep = get_deposition(api, token, dep_id)
    state = dep.get("state")
    submitted = dep.get("submitted")
    links = dep.get("links") or {}
    bucket = links.get("bucket")
    can_upload = (submitted in (False, None)) and bool(bucket)
    if not can_upload:
        echo(f"\nZenodo deposition {dep_id} is not modifiable via bucket:")
        echo(f"  state={state!r}, submitted={submitted!r}, has_bucket={bool(bucket)}")
        die("Cannot upload: need a draft with a bucket link. Create a new version or unlock draft.")
    return dep

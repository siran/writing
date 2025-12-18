# .scripts/zenodo_api.py
import os
import json
import time
import traceback
from typing import Dict, List, Tuple, Optional

import requests  # assumes installed

from common import echo, die


def zenodo_api_and_token(env: str) -> Tuple[str, str]:
    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        die("Missing ZENODO_TOKEN for Zenodo API.")

    api = os.environ.get("ZENODO_SANDBOX_API", "https://sandbox.zenodo.org/api")
    if env == "prod":
        api = os.environ.get("ZENODO_API", "https://zenodo.org/api")

    return api, token


def http_put_raw(url: str, token: str, fp):
    echo(f"+ HTTP PUT (raw) {url}")
    headers = {"Authorization": f"Bearer {token}"}
    backoffs = [1, 2, 4, 8, 16]
    for i, delay in enumerate(backoffs, start=1):
        r = requests.put(url, data=fp, headers=headers)
        if r.ok:
            return r.json() if "application/json" in (r.headers.get("Content-Type", "")) else {}
        if r.status_code in {429, 500, 502, 503, 504} and i < len(backoffs):
            echo(f"[WARN] Bucket PUT {r.status_code} at {url}; retrying in {delay}s...")
            try:
                time.sleep(delay)
            except KeyboardInterrupt:
                break
            continue
        try:
            print(r.text)
        except Exception:
            pass
        die(f"Zenodo bucket PUT error {r.status_code} at {url}")
    die(f"Zenodo bucket PUT error at {url}")


def http_json(method: str, url: str, token: str, data=None, files=None) -> Dict:
    echo(f"+ HTTP {method.upper()} {url}")
    headers = {"Authorization": f"Bearer {token}"}
    print(f"{data=}")
    print(f"{files=}")
    backoffs = [1, 2, 4, 8, 16]
    for i, delay in enumerate(backoffs, start=1):
        if method.upper() in ("POST", "PUT", "PATCH"):
            r = requests.request(method, url, headers=headers, json=data, files=files)
        else:
            r = requests.request(method, url, headers=headers, params=data)
        if r.ok:
            try:
                return r.json()
            except Exception:
                return {}
        retry_after = r.headers.get("Retry-After")
        retry_delay = None
        try:
            retry_delay = int(retry_after)
        except Exception:
            pass
        if r.status_code in {429, 500, 502, 503, 504} and i < len(backoffs):
            wait = retry_delay if retry_delay is not None else delay
            echo(f"[WARN] Zenodo API {r.status_code} at {url}; retrying in {wait}s...")
            try:
                time.sleep(wait)
            except KeyboardInterrupt:
                break
            continue
        try:
            echo(r.text)
        except Exception:
            pass
        die(f"Zenodo API error {r.status_code} at {url}")
    die(f"Zenodo API error at {url}")


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

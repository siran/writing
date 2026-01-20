#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import hashlib
import re
import sys
import shutil
import time
from dataclasses import dataclass
from pathlib import Path
from datetime import date
from typing import List, Optional, Dict, Tuple

from common import echo, die, run
from doc_utils import (
    compute_site_base_url,
    infer_journal_from_site_base,
    render_in_staging,
    parse_pnpmd,
    normalize_markdown_prose,
    write_provenance,
    find_latest_provenance_for_stem,
    dump_yaml,
    detect_license,
    ORCID_URL_RE,
    ORCID_ID_RE,
)

# Make render helpers visible (for title_from_book_yaml).
ROOT = Path(__file__).resolve().parents[2]
RENDER_DIR = ROOT / ".scripts" / "render"
if str(RENDER_DIR) not in sys.path:
    sys.path.append(str(RENDER_DIR))
from pnpmd_util import title_from_book_yaml
from zenodo_api import (
    zenodo_api_and_token,
    http_json,
    http_put_raw,
    reserve_deposition,
    ensure_draft_or_die,
)

DEFAULT_ORCID = "0009-0009-9098-9468"
DEFAULT_ORCID_NAME = "An M. Rodriguez"
DEFAULT_ORCID_EMAIL = "an@preferredframe.com"
MAX_EXTRA_ASSET_BYTES = 1024 * 1024

ASSET_TYPE_ALIASES = {
    "code": "software",
    "script": "software",
}
RELATED_RESOURCE_TYPES = {
    "dataset",
    "image",
    "lesson",
    "other",
    "physicalobject",
    "poster",
    "presentation",
    "publication",
    "publication-article",
    "publication-book",
    "publication-preprint",
    "software",
    "video",
}


@dataclass
class ExtraAsset:
    src: Path
    asset_type: Optional[str] = None
    name: Optional[str] = None
    final_path: Optional[Path] = None
    assets_url: Optional[str] = None


# ---------------- git helpers ----------------

def slug_branch(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9._-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    s = s.lstrip(".-")
    if s.endswith(".lock"):
        s = s[:-5] + "-lock"
    return s[:80] or "x"


def _pending_namespace(raw: str) -> str:
    s = (raw or "").strip().lower()
    s = re.sub(r"[^a-z0-9._-]+", "-", s)
    s = s.strip("-")
    return s or "preferredframe"


def _pending_hash_value(mode: str, stem: str, src_commit: str, staged_md: Path) -> str:
    if mode == "stem":
        payload = stem
    elif mode == "commit":
        payload = src_commit
    else:
        payload = staged_md.read_bytes()
    if isinstance(payload, bytes):
        digest = hashlib.sha256(payload).hexdigest()
    else:
        digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return digest[:12]


def make_pending_doi(args, stem: str, src_commit: str, staged_md: Path) -> str:
    namespace = _pending_namespace(args.assets_prefix)
    digest = _pending_hash_value(args.pending_hash, stem, src_commit, staged_md)
    return f"pending/{namespace}.{digest}"


def git_repo_root(path: Path) -> Path:
    out = run(["git", "rev-parse", "--show-toplevel"], cwd=path)
    root = out.strip()
    if not root:
        die("not inside a git repository")
    return Path(root)


def git_status_clean(repo: Path) -> bool:
    out = run(["git", "status", "--porcelain"], cwd=repo)
    return out.strip() == ""


def git_staged_paths(repo: Path) -> List[str]:
    out = run(["git", "diff", "--cached", "--name-only"], cwd=repo)
    return [ln.strip() for ln in out.splitlines() if ln.strip()]


def _author_key(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (name or "").lower())


def _apply_provenance_defaults(parsed: dict, prov: Optional[Dict]) -> dict:
    if not prov:
        return parsed
    updated = dict(parsed)
    if not updated.get("title"):
        updated["title"] = (prov.get("title") or "").strip()
    if not updated.get("keywords"):
        updated["keywords"] = list(prov.get("keywords") or [])
    if not updated.get("one_sentence"):
        updated["one_sentence"] = (prov.get("one_sentence_summary") or "").strip()
    if not updated.get("abstract"):
        updated["abstract"] = (prov.get("abstract") or "").strip()
    if not updated.get("reference_doi_urls"):
        updated["reference_doi_urls"] = list(prov.get("references_doi") or [])

    prov_authors = list(prov.get("authors") or [])
    if prov_authors:
        if not updated.get("authors"):
            updated["authors"] = [dict(a) for a in prov_authors]
        else:
            prov_by_key = {_author_key(a.get("name", "")): a for a in prov_authors}
            merged = []
            for author in updated.get("authors") or []:
                entry = dict(author)
                key = _author_key(entry.get("name", ""))
                src = prov_by_key.get(key)
                if src:
                    if not entry.get("orcid") and src.get("orcid"):
                        entry["orcid"] = src.get("orcid")
                    if not entry.get("email") and src.get("email"):
                        entry["email"] = src.get("email")
                merged.append(entry)
            updated["authors"] = merged
    return updated


def _desired_provenance_fields(parsed: dict, creators: List[Dict]) -> Dict[str, object]:
    return {
        "title": (parsed.get("title") or "").strip(),
        "keywords": list(parsed.get("keywords") or []),
        "one_sentence_summary": normalize_markdown_prose(parsed.get("one_sentence") or ""),
        "abstract": normalize_markdown_prose(parsed.get("abstract") or ""),
        "authors": creators,
    }


def _provenance_diffs(prev_prov: Dict, parsed: dict, creators: List[Dict]) -> List[str]:
    desired = _desired_provenance_fields(parsed, creators)
    diffs: List[str] = []
    for key, val in desired.items():
        if not val:
            continue
        prev_val = prev_prov.get(key)
        if prev_val != val:
            diffs.append(key)
    return diffs


def _update_provenance_from_parsed(
    prov_path: Path, prev_prov: Dict, parsed: dict, creators: List[Dict]
) -> bool:
    desired = _desired_provenance_fields(parsed, creators)
    changed = False
    for key, val in desired.items():
        if not val:
            continue
        if prev_prov.get(key) != val:
            prev_prov[key] = val
            changed = True
    if changed:
        prov_path.write_text(dump_yaml(prev_prov), encoding="utf-8")
    return changed


def _validate_required_metadata(parsed: dict) -> dict:
    missing = []
    if not parsed.get("keywords"):
        missing.append("keywords")
    if not parsed.get("one_sentence"):
        missing.append("one_sentence_summary")
    if not parsed.get("abstract"):
        missing.append("abstract")
    if missing:
        die(f"Missing required metadata: {', '.join(missing)}")
    return parsed


def _infer_subjournal_from_provenance(site_repo: Path, stem: str) -> Optional[str]:
    candidates = []
    defaults = ["documents", "posts", "prints", "reports"]
    for sj in defaults:
        prov_path, _prov = find_latest_provenance_for_stem(site_repo, sj, stem)
        if prov_path:
            candidates.append(prov_path)

    if not candidates:
        for p in site_repo.rglob("provenance.yaml"):
            try:
                rel = p.relative_to(site_repo)
            except ValueError:
                continue
            parts = rel.parts
            if len(parts) >= 2 and parts[1] == stem:
                candidates.append(p)

    if not candidates:
        return None
    candidates.sort(key=lambda p: p.stat().st_mtime)
    return candidates[-1].relative_to(site_repo).parts[0]


def git_head(repo: Path) -> str:
    return run(["git", "rev-parse", "HEAD"], cwd=repo).strip()


def git_origin_url(repo: Path) -> str:
    return run(["git", "config", "--get", "remote.origin.url"], cwd=repo).strip()


# ---- zenodo DOI → record id ----

ZENODO_DOI_RECID_RE = re.compile(r"zenodo\.(\d+)$")


def record_id_from_doi(doi: str) -> Optional[int]:
    m = ZENODO_DOI_RECID_RE.search(doi.strip())
    if not m:
        return None
    try:
        return int(m.group(1))
    except ValueError:
        return None


def _is_pending_doi(doi: str) -> bool:
    return (doi or "").strip().lower().startswith("pending/")


def _doi_env_kind(doi: str) -> Optional[str]:
    d = (doi or "").strip().lower()
    if d.startswith("10.5072/"):
        return "sandbox"
    if d.startswith("10.5281/"):
        return "prod"
    return None


def _doi_env_mismatch(args, prev_doi: str, prev_concept: str) -> Optional[str]:
    doi_env = _doi_env_kind(prev_doi)
    concept_env = _doi_env_kind(prev_concept)
    if doi_env and concept_env and doi_env != concept_env:
        return f"{doi_env}/{concept_env}"
    expected = "prod" if args.env == "prod" else "sandbox"
    if doi_env and doi_env != expected:
        return doi_env
    if concept_env and concept_env != expected:
        return concept_env
    return None


def _file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _copy_if_changed(src: Path, dest: Path) -> bool:
    try:
        if dest.exists() and dest.is_file():
            if src.stat().st_size == dest.stat().st_size:
                if _file_sha256(src) == _file_sha256(dest):
                    echo(f"+ skip copy (unchanged) {src} -> {dest}")
                    return False
    except Exception:
        pass
    dest.parent.mkdir(parents=True, exist_ok=True)
    echo(f"+ copy {src} -> {dest}")
    shutil.copy2(src, dest)
    return True


def _reuse_pending_artifacts(
    site_repo: Path,
    subjournal: str,
    stem: str,
    prov_path: Path,
    prov: Dict,
    assets_repo: Optional[Path],
    assets_prefix: Optional[str],
) -> Optional[Tuple[Path, Path, Path, Path, Optional[Path], Optional[Path], Path]]:
    artifacts = prov.get("artifacts") or {}
    md_name = artifacts.get("md")
    pdf_name = artifacts.get("pdf_name")
    html_name = artifacts.get("html_name")
    pmd_name = artifacts.get("pandoc_md_name")
    if not (md_name and pdf_name and html_name and pmd_name):
        return None

    pending_dir = prov_path.parent
    if not pending_dir.exists():
        return None

    staging = site_repo / subjournal / "_staging" / stem
    staging.mkdir(parents=True, exist_ok=True)

    assets_base = None
    if assets_repo and assets_prefix:
        doi_suffix = pending_dir.name
        doi_prefix = pending_dir.parent.name
        assets_base = assets_repo / assets_prefix / stem / doi_prefix / doi_suffix
        if not assets_base.exists():
            assets_base = None

    def copy_from(name: str, dest_name: Optional[str] = None, allow_assets: bool = False) -> Optional[Path]:
        sources = [pending_dir / name]
        if allow_assets and assets_base is not None:
            sources.append(assets_base / name)
        for src in sources:
            if src.exists():
                dst = staging / (dest_name or name)
                shutil.copy2(src, dst)
                return dst
        return None

    staged_md = copy_from(md_name)
    staged_pdf = copy_from(pdf_name, allow_assets=True)
    staged_html = copy_from(html_name)
    if not (staged_md and staged_pdf and staged_html):
        return None

    pmd_dest_name = staged_md.with_suffix(".pandoc.md").name
    staged_pmd = copy_from(pmd_name, pmd_dest_name)
    if not staged_pmd:
        return None

    staged_embed_html = None
    embed_name = artifacts.get("embed_html_name")
    if embed_name:
        staged_embed_html = copy_from(embed_name, allow_assets=True)

    staged_epub = None
    epub_name = artifacts.get("epub_name")
    if epub_name:
        staged_epub = copy_from(epub_name, allow_assets=True)

    return (
        staging,
        staged_md,
        staged_pdf,
        staged_html,
        staged_embed_html,
        staged_epub,
        staged_pmd,
    )


# ---------------- context & cleanup ----------------

@dataclass
class PublishContext:
    site_repo: Optional[Path] = None
    orig_branch: Optional[str] = None
    branch_name: Optional[str] = None
    final_dir: Optional[Path] = None
    api: Optional[str] = None
    token: Optional[str] = None
    dep_id: Optional[int] = None


def cleanup_best_effort(ctx: PublishContext):
    """Try to clean Zenodo draft, local files, and git branches. Never raises."""
    echo("\n[cleanup] Attempting best-effort cleanup...")

    # 1) Zenodo draft
    if ctx.api and ctx.token and ctx.dep_id:
        try:
            http_json(
                "DELETE",
                f"{ctx.api}/deposit/depositions/{ctx.dep_id}",
                ctx.token,
                data=None,
            )
            echo(f"[cleanup] Deleted Zenodo deposition {ctx.dep_id}")
        except Exception as e:
            echo(f"[cleanup] WARNING: failed to delete Zenodo deposition: {e}")

    # 2) Local final_dir
    if ctx.final_dir and ctx.final_dir.exists():
        try:
            shutil.rmtree(ctx.final_dir)
            echo(f"[cleanup] Removed final_dir {ctx.final_dir}")
        except Exception as e:
            echo(f"[cleanup] WARNING: failed to remove {ctx.final_dir}: {e}")

    # 3) Git branches
    if ctx.site_repo and ctx.orig_branch:
        try:
            cur = run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                cwd=ctx.site_repo,
                check=False,
            ).strip()
        except Exception:
            cur = None

        try:
            if cur and cur != ctx.orig_branch:
                run(["git", "checkout", ctx.orig_branch], cwd=ctx.site_repo, check=False)
        except Exception as e:
            echo(f"[cleanup] WARNING: failed to checkout {ctx.orig_branch}: {e}")

    if ctx.site_repo and ctx.branch_name:
        try:
            run(
                ["git", "branch", "-D", ctx.branch_name],
                cwd=ctx.site_repo,
                check=False,
            )
        except Exception as e:
            echo(f"[cleanup] WARNING: failed to delete branch {ctx.branch_name}: {e}")

    echo("[cleanup] Done (best effort).")


# ---------------- small orchestration helpers ----------------

def parse_args():
    import argparse

    ap = argparse.ArgumentParser(description="Publish a Preferred Frame print (PNPMD).")
    ap.add_argument("md_path", help="Path to the source .md or .yml (book mode).")
    ap.add_argument(
        "--env",
        choices=["sandbox", "prod"],
        default="sandbox",
        help="Zenodo environment (default: sandbox)",
    )
    ap.add_argument(
        "--offline",
        action="store_true",
        help="Skip Zenodo API calls; use a pending DOI (pending/<namespace>.<hash>).",
    )
    ap.add_argument(
        "--pending-hash",
        choices=["md", "stem", "commit"],
        default="md",
        help="Hash source for pending DOI when --offline is set (default: md).",
    )
    ap.add_argument("--community", default="preferredframe", help="Zenodo community slug.")
    ap.add_argument(
        "--journal",
        default=None,
        help="Journal title shown in Zenodo and provenance. "
        "If omitted, inferred from CNAME/site base URL.",
    )
    ap.add_argument(
        "--subjournal",
        default=None,
        help="Top-level subjournal folder (prints, documents, posts, reports, ...). "
        "If omitted, you will be prompted.",
    )
    ap.add_argument(
        "--orcid",
        default=None,
        help=(
            "Comma-separated ORCIDs (author order) to fill missing ORCIDs. "
            f"If omitted, defaults to {DEFAULT_ORCID!r} for the first author only."
        ),
    )
    ap.add_argument(
        "--keywords",
        default=None,
        help="Comma-separated keywords override (avoids interactive prompt).",
    )
    ap.add_argument(
        "--oss",
        default=None,
        help="One-sentence summary override (avoids interactive prompt).",
    )
    ap.add_argument(
        "--abstract",
        default=None,
        help="Abstract override (avoids interactive prompt).",
    )
    ap.add_argument(
        "--update-provenance",
        action="store_true",
        help="Update existing provenance.yaml with front matter metadata when they differ.",
    )
    ap.add_argument(
        "--new-version-of",
        dest="new_version_of",
        default=None,
        help="Stem of an existing publication this should be a new version of.",
    )
    ap.add_argument(
        "--assets-dir", default="../assets", help="Path to local assets repo (default: ../assets)."
    )
    ap.add_argument(
        "--assets-base-url",
        default="https://assets.preferredframe.com",
        help="Public base URL for assets (default: https://assets.preferredframe.com)",
    )
    ap.add_argument(
        "--assets-prefix",
        default="preferredframe",
        help="Subdirectory under the assets repo/base-url (default: preferredframe).",
    )
    ap.add_argument(
        "--add-asset",
        action="append",
        default=[],
        help="Add an extra file to the Zenodo deposit (repeatable, <=1MB).",
    )
    ap.add_argument(
        "--asset-type",
        default=None,
        help=(
            "Type for extra assets (e.g. Software). Maps to Zenodo related "
            "resource_type."
        ),
    )
    ap.add_argument(
        "--no-assets-push",
        action="store_true",
        help="Do not push the assets repo (default: push).",
    )
    ap.add_argument(
        "--omit-toc",
        action="store_true",
        help="Pass through to render.py to omit the table of contents.",
    )
    ap.add_argument(
        "--omit-numbering",
        action="store_true",
        help="Pass through to render.py to disable section numbering.",
    )
    ap.add_argument(
        "--as-is",
        action="store_true",
        help="Pass through to render.py to bypass preprocessing and render the file as-is.",
    )
    ap.add_argument(
        "--toc-depth",
        type=int,
        default=1,
        help="TOC depth passed to render.py (default: 1).",
    )
    return ap.parse_args()


def _prompt_required_metadata(parsed: dict) -> dict:
    """
    Ensure keywords, one_sentence, and abstract are populated. Prompts interactively if missing.
    """
    updated = dict(parsed)
    if not updated.get("keywords"):
        kw = input("Enter keywords (comma-separated): ").strip()
        kws = [k.strip() for k in kw.split(",") if k.strip()] if kw else []
        updated["keywords"] = kws
    if not updated.get("one_sentence"):
        updated["one_sentence"] = input("Enter one-sentence summary: ").strip()
    if not updated.get("abstract"):
        updated["abstract"] = input("Enter abstract: ").strip()

    missing = []
    if not updated["keywords"]:
        missing.append("keywords")
    if not updated["one_sentence"]:
        missing.append("one_sentence_summary")
    if not updated["abstract"]:
        missing.append("abstract")
    if missing:
        die(f"Missing required metadata: {', '.join(missing)}")
    return updated


def _normalize_orcid_input(raw: str) -> str:
    s = (raw or "").strip()
    if not s:
        return ""
    m = ORCID_URL_RE.search(s)
    if m:
        return m.group(1).upper()
    m = ORCID_ID_RE.search(s)
    if m:
        return m.group(1).upper()
    return ""


def _split_csv_arg(raw: Optional[str]) -> List[str]:
    if not raw:
        return []
    return [s.strip() for s in raw.split(",") if s.strip()]


def _normalize_asset_type(raw: Optional[str]) -> str:
    s = (raw or "").strip().lower()
    if not s:
        return ""
    s = s.replace("_", "-").replace(" ", "-")
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return ASSET_TYPE_ALIASES.get(s, s)


def _asset_resource_type(asset_type: Optional[str]) -> Optional[str]:
    if not asset_type:
        return None
    norm = _normalize_asset_type(asset_type)
    return norm if norm in RELATED_RESOURCE_TYPES else None


def _parse_extra_assets(raw_paths: List[str], asset_type: Optional[str]) -> List[ExtraAsset]:
    if not raw_paths:
        return []

    if not asset_type:
        die(
            "--asset-type is required when using --add-asset "
            "(example: --asset-type Software)"
        )

    resource_type = _asset_resource_type(asset_type)
    if not resource_type:
        allowed = ", ".join(sorted(RELATED_RESOURCE_TYPES))
        die(f"Unsupported --asset-type {asset_type!r}. Allowed: {allowed}")

    assets: List[ExtraAsset] = []
    seen_names = set()
    for raw in raw_paths:
        path_str = (raw or "").strip()
        if not path_str:
            continue
        src = Path(path_str).expanduser().resolve()
        if not src.exists():
            die(f"--add-asset file not found: {src}")
        if not src.is_file():
            die(f"--add-asset is not a file: {src}")
        size = src.stat().st_size
        if size > MAX_EXTRA_ASSET_BYTES:
            die(
                f"--add-asset file too large (>1MB): {src} ({size} bytes)"
            )
        if src.name in seen_names:
            die(f"--add-asset filename collision: {src.name}")
        seen_names.add(src.name)
        assets.append(ExtraAsset(src=src, asset_type=resource_type, name=src.name))
    return assets


def _apply_orcid_list(parsed: dict, orcids: List[str], *, warn_unused: bool = True) -> dict:
    updated = dict(parsed)
    authors = [dict(a) for a in (updated.get("authors") or [])]
    if not orcids or not authors:
        return updated

    used = 0
    for author in authors:
        name = (author.get("name") or "").strip()
        if not name or author.get("orcid"):
            continue
        if used >= len(orcids):
            break
        author["orcid"] = orcids[used]
        used += 1

    if warn_unused and used < len(orcids):
        echo(
            f"WARNING: {len(orcids) - used} ORCID(s) from --orcid not used "
            "because there were fewer authors missing ORCID."
        )

    updated["authors"] = authors
    return updated


def _find_default_orcid_author(authors: List[Dict]) -> Optional[int]:
    target_key = _author_key(DEFAULT_ORCID_NAME)
    for idx, author in enumerate(authors):
        name_key = _author_key(author.get("name", ""))
        if name_key and name_key == target_key:
            return idx
    for idx, author in enumerate(authors):
        email = (author.get("email") or "").strip().lower()
        if email == DEFAULT_ORCID_EMAIL:
            return idx
    return None


def _apply_cli_overrides(parsed: dict, args) -> dict:
    updated = dict(parsed)
    if args.keywords is not None:
        updated["keywords"] = _split_csv_arg(args.keywords)
    if args.oss is not None:
        updated["one_sentence"] = (args.oss or "").strip()
    if args.abstract is not None:
        updated["abstract"] = (args.abstract or "").strip()
    if args.orcid is not None:
        orcid_items = _split_csv_arg(args.orcid)
        orcids: List[str] = []
        for item in orcid_items:
            norm = _normalize_orcid_input(item)
            if not norm:
                die(f"Invalid ORCID in --orcid list: {item!r}")
            orcids.append(norm)
        updated = _apply_orcid_list(updated, orcids, warn_unused=True)
    else:
        default_orcid = _normalize_orcid_input(DEFAULT_ORCID)
        if default_orcid:
            authors = [dict(a) for a in (updated.get("authors") or [])]
            if authors:
                idx = _find_default_orcid_author(authors)
                if idx is not None:
                    target = authors[idx]
                    if (target.get("name") or "").strip() and not target.get("orcid"):
                        target["orcid"] = default_orcid
                        authors[idx] = target
                        updated["authors"] = authors
    return updated


def _prompt_missing_orcids(parsed: dict) -> dict:
    """
    Ensure each author has an ORCID. Prompts interactively when missing.
    """
    updated = dict(parsed)
    authors = [dict(a) for a in (updated.get("authors") or [])]
    skip_remaining = False
    for author in authors:
        name = (author.get("name") or "").strip()
        if not name or author.get("orcid"):
            continue
        if skip_remaining:
            break
        while True:
            raw = input(
                f"Enter ORCID for {name} "
                "(format 0000-0000-0000-0000, or 'skip' to omit): "
            ).strip()
            if not raw:
                confirm = input(
                    f"{name} has no ORCID. Skip remaining authors? [Y/n] "
                ).strip().lower()
                if confirm in ("", "y", "yes"):
                    skip_remaining = True
                    break
                if confirm in ("n", "no"):
                    continue
                echo("Please answer Y or n.")
                continue
            if raw.lower() in {"skip", "none", "n/a"}:
                break
            orcid = _normalize_orcid_input(raw)
            if orcid:
                author["orcid"] = orcid
                break
            echo("Invalid ORCID format. Example: 0000-0000-0000-0000 or https://orcid.org/0000-0000-0000-0000")
        if skip_remaining:
            break

    if authors and not any((a.get("orcid") or "").strip() for a in authors):
        target = next((a for a in authors if (a.get("name") or "").strip()), None)
        if not target:
            die("At least one ORCID is required, but no authors were found.")
        name = (target.get("name") or "").strip()
        while True:
            raw = input(
                f"At least one ORCID is required. Enter ORCID for {name}: "
            ).strip()
            if not raw:
                echo("ORCID is required to proceed.")
                continue
            orcid = _normalize_orcid_input(raw)
            if orcid:
                target["orcid"] = orcid
                break
            echo("Invalid ORCID format. Example: 0000-0000-0000-0000 or https://orcid.org/0000-0000-0000-0000")
    updated["authors"] = authors
    return updated


def preflight_and_context(
    args,
) -> Tuple[Path, Optional[Path], Path, str, str, str, Optional[str]]:
    """
    Resolve src_md and optional book_yaml, check git, infer site_base/journal/subjournal.
    Returns:
        src_md, book_yaml, site_repo, src_commit, src_origin, site_base, subjournal (if provided)
    """
    src_path = Path(args.md_path).resolve()

    book_yaml: Optional[Path] = None
    if src_path.suffix.lower() in (".yml", ".yaml"):
        book_yaml = src_path
        # Use the YAML itself as the primary input; combined .md will be produced in staging.
        src_md = src_path
    else:
        src_md = src_path

    src_repo = git_repo_root(src_md.parent)
    if not git_status_clean(src_repo):
        input(
            f"Source repo has uncommitted changes: {src_repo}. "
            f"Press Enter to continue or Ctrl-C to abort."
        )
    src_commit = git_head(src_repo)
    src_origin = git_origin_url(src_repo)

    site_repo = git_repo_root(Path.cwd())
    if not git_status_clean(site_repo):
        input(
            f"Site repo has uncommitted changes: {site_repo}. "
            f"Press Enter to continue or Ctrl-C to abort."
        )

    site_base = compute_site_base_url(site_repo)
    echo(f"+ site_base_url = {site_base}")

    if not args.journal:
        args.journal = infer_journal_from_site_base(site_base)
    echo(f"+ journal = {args.journal}")

    if args.subjournal:
        echo(f"+ subjournal = {args.subjournal}")

    return src_md, book_yaml, site_repo, src_commit, src_origin, site_base, args.subjournal


def determine_versioning(
    args, site_repo: Path, subjournal: str, src_commit: str, stem: str
) -> Tuple[bool, Optional[int], Optional[str], Optional[Path], Optional[Dict]]:
    """Figure out whether this is a new version and, if so, of which record."""
    if args.new_version_of:
        nv = args.new_version_of.strip().rstrip("/")
        nv_path = Path(nv)
        prev_stem = nv_path.stem if nv_path.name else nv
    else:
        prev_stem = stem

    prov_path_prev, prov_prev = find_latest_provenance_for_stem(
        site_repo, subjournal, prev_stem
    )

    is_new_version = False
    prev_record_id: Optional[int] = None
    prev_concept = None

    if prov_prev:
        prev_source = prov_prev.get("source") or {}
        prev_commit = (prev_source.get("commit") or "").strip()
        prev_doi = (prov_prev.get("doi") or "").strip()
        prev_concept = (prov_prev.get("concept_doi") or "").strip() or None

        echo(
            f"Found previous publication for stem '{prev_stem}' in subjournal '{subjournal}':"
        )
        echo(f" - provenance: {prov_path_prev}")
        echo(f" - DOI:        {prev_doi or '(none)'}")
        echo(f" - concept_doi:{prev_concept or '(none)'}")
        echo(f" - commit:     {prev_commit or '(unknown)'}")

        prev_env_mismatch = _doi_env_mismatch(args, prev_doi, prev_concept or "")
        if prev_env_mismatch:
            note = (
                "previous DOI envs are mixed"
                if "/" in prev_env_mismatch
                else f"previous DOI appears to be {prev_env_mismatch}"
            )
            echo(f"WARNING: {note}; treating as unpublished for {args.env}.")
            return False, None, None, prov_path_prev, prov_prev

        if prev_commit and prev_commit == src_commit and not _is_pending_doi(prev_doi):
            die(f"This commit has already been published as DOI {prev_doi or '(unknown)'}.")

        if _is_pending_doi(prev_doi):
            echo("Previous DOI is pending; treating as unpublished for versioning.")
            if args.offline:
                echo("Offline mode: creating a new pending DOI without Zenodo linkage.")
                return True, None, prev_concept, prov_path_prev, prov_prev
            if args.new_version_of:
                echo("WARNING: pending DOI cannot be used for Zenodo newversion; publishing as a new record.")
            return False, None, prev_concept, prov_path_prev, prov_prev

        if args.new_version_of:
            is_new_version = True
            prev_record_id = record_id_from_doi(prev_doi)
            if not prev_record_id:
                if args.offline:
                    echo(
                        "WARNING: previous DOI is not a Zenodo DOI; "
                        "proceeding without Zenodo linkage (--offline)."
                    )
                else:
                    die(f"Cannot extract Zenodo record id from previous DOI '{prev_doi}'.")
        else:
            ans_ver = input(
                f"Treat this as a new version of the latest one? [y/N]: "
            ).strip().lower()
            if ans_ver in ("y", "yes"):
                is_new_version = True
                prev_record_id = record_id_from_doi(prev_doi)
                if not prev_record_id:
                    if args.offline:
                        echo(
                            "WARNING: previous DOI is not a Zenodo DOI; "
                            "proceeding without Zenodo linkage (--offline)."
                        )
                    else:
                        die(f"Cannot extract Zenodo record id from previous DOI '{prev_doi}'.")
            else:
                die(
                    f"a document named '{stem}' already has been published in '{subjournal}'"
                )
    else:
        if args.new_version_of:
            die(
                f"--new-version-of={args.new_version_of!r} was given, "
                f"but no previous provenance was found for that stem in subjournal "
                f"'{subjournal}'."
            )

    return is_new_version, prev_record_id, prev_concept, prov_path_prev, prov_prev


def prompt_change_log(is_new_version: bool) -> Optional[str]:
    if not is_new_version:
        return None
    echo("\nThis is a new version. Enter change log (multi-line).")
    echo("Finish with an empty line.")
    lines: List[str] = []
    while True:
        ln = input()
        if ln.strip() == "":
            break
        lines.append(ln)
    return "\n".join(lines).strip() if lines else ""


def prepare_branch(site_repo: Path, stem: str, src_commit: str) -> str:
    date_str = date.today().strftime("%Y-%m")
    branch_name = f"publish/{date_str}-{slug_branch(stem)}-{src_commit[:8]}"
    echo(f"+ git checkout -b {branch_name}")
    run(["git", "checkout", "-b", branch_name], cwd=site_repo)
    return branch_name


def reserve_or_new_version(
    args,
    is_new_version: bool,
    prev_record_id: Optional[int],
    prev_concept: Optional[str],
    title: str,
    creators: List[Dict],
    publication_year: str,
    publication_type: str,
) -> Tuple[str, str, str, Optional[str], int]:
    """
    Create or reuse a Zenodo deposition (via newversion),
    returning (api, token, doi, concept_doi, dep_id).
    """
    api, token = zenodo_api_and_token(args.env)

    # Sandbox: never link to prod record IDs; always mint fresh concepts.
    if args.env == "sandbox" and is_new_version:
        echo(
            "+ sandbox env: ignoring previous record; "
            "creating a fresh concept instead of a linked new version."
        )
        is_new_version = False
        prev_record_id = None

    if is_new_version:
        if prev_record_id is None:
            die("Internal error: prev_record_id missing for new version.")

        dep = http_json(
            "POST",
            f"{api}/deposit/depositions/{prev_record_id}/actions/newversion",
            token,
            data=None,
        )
        dep_id = dep.get("id")
        if not dep_id:
            die("Zenodo did not return a deposition id for the new version.")

        minimal_meta = {
            "upload_type": "publication",
            "publication_type": publication_type,
            "title": title,
            "creators": creators,
            "journal_title": args.journal,
            "publisher": {"name": args.journal},
            "publication_year": publication_year,
            "communities": [{"identifier": args.community}],
            "prereserve_doi": True,
        }

        dep = http_json(
            "PUT",
            f"{api}/deposit/depositions/{dep_id}",
            token,
            data={"metadata": minimal_meta},
        )

        pr = (dep.get("metadata") or {}).get("prereserve_doi") or {}
        doi = pr.get("doi")
        concept_doi = dep.get("conceptdoi") or prev_concept

        if not doi:
            die("Zenodo did not return a reserved DOI for the new version.")

        if prev_concept and concept_doi and concept_doi != prev_concept:
            echo(f"WARNING: concept DOI changed {prev_concept} → {concept_doi}")
    else:
        dep_id, doi, concept_doi = reserve_deposition(
            api,
            token,
            title,
            creators,
            publication_year,
            args.community,
            args.journal,
            publication_type,
        )

    return api, token, doi, concept_doi, dep_id


def preview_actions(
    site_repo: Path,
    final_md: Path,
    final_html: Path,
    final_embed_html: Optional[Path],
    final_pmd: Path,
    prov_path: Path,
    final_pdf: Path,
    final_epub: Optional[Path],
    extra_assets: List[ExtraAsset],
    assets_prefix: str,
    stem: str,
    doi_prefix: str,
    doi_suffix: str,
    dep_id: Optional[int],
    title: str,
    publication_date: str,
    doi: str,
    branch_name: str,
    args,
    zenodo_enabled: bool,
    zenodo_meta: Dict,
):
    echo("\n--- PROVENANCE ---")
    print(prov_path)
    with open(prov_path, "r", encoding="utf-8") as f:
        print(f.read(), end="")

    echo("\n--- ZENODO METADATA (preview) ---")
    import json as _json

    print(_json.dumps(zenodo_meta, indent=2, ensure_ascii=False))

    echo("\n--- FILES TO COMMIT (site repo) ---")
    files_to_commit = [final_md, final_html, final_pmd, prov_path]
    for p in files_to_commit:
        echo(f" - {p.relative_to(site_repo)}")

    echo("\n--- FILES TO UPLOAD TO ZENODO ---")
    upload_list = [final_md, final_pdf, final_pmd, final_html]
    if final_embed_html is not None:
        upload_list.append(final_embed_html)
    if final_epub is not None:
        upload_list.append(final_epub)
    for asset in extra_assets:
        if asset.final_path is not None:
            upload_list.append(asset.final_path)
    for p in upload_list:
        echo(f" - {p.name}")

    echo("\n--- PREVIEW: ACTIONS AFTER CONFIRMATION ---")
    echo("Site repo:")
    echo(f"  git add {final_md.relative_to(site_repo)}")
    echo(f"  git add {final_html.relative_to(site_repo)}")
    echo(f"  git add {final_pmd.relative_to(site_repo)}")
    echo(f"  git add {prov_path.relative_to(site_repo)}")
    echo("  git commit ...")
    if args.assets_dir:
        echo("Assets repo:")
        echo(
            f"  copy {final_pdf} -> "
            f"{args.assets_dir}/{assets_prefix}/{stem}/{doi_prefix}/{doi_suffix}/{final_pdf.name}"
        )
        if final_embed_html is not None:
            echo(
                f"  copy {final_embed_html} -> "
                f"{args.assets_dir}/{assets_prefix}/{stem}/{doi_prefix}/{doi_suffix}/{final_embed_html.name}"
            )
        if final_epub is not None:
            echo(
                f"  copy {final_epub} -> "
                f"{args.assets_dir}/{assets_prefix}/{stem}/{doi_prefix}/{doi_suffix}/{final_epub.name}"
            )
        for asset in extra_assets:
            src = asset.final_path or asset.src
            echo(
                f"  copy {src} -> "
                f"{args.assets_dir}/{assets_prefix}/{stem}/{doi_prefix}/{doi_suffix}/{asset.src.name}"
            )
        echo("  git add <those files>")
        if not args.no_assets_push:
            echo("  git commit ...")
            echo("  git push")
    echo("Zenodo:")
    if zenodo_enabled:
        echo(
            f"  PUT /deposit/depositions/{dep_id} "
            f"(full metadata incl. related_identifiers)"
        )
        embed_label = ", embed.html" if final_embed_html is not None else ""
        extra_label = (
            f", {len(extra_assets)} extra asset(s)" if extra_assets else ""
        )
        echo(
            "  PUT md, PDF, pandoc.md, html"
            + embed_label
            + (", epub" if final_epub is not None else "")
            + extra_label
            + " to bucket"
        )
        echo("  POST /deposit/depositions/{id}/actions/publish")
        echo(f"  GET /records/{dep_id} (fetch concept DOI)")
        echo("  update provenance.yaml with concept DOI (optional, then commit)")
    else:
        echo("  SKIPPED (--offline)")
    echo("Git:")
    echo("  git checkout main")
    echo(f"  git merge --no-ff {branch_name}")
    echo("  git push origin main")
    echo(f"  git branch -d {branch_name}")


# ---------------- main publish workflow ----------------

def run_publish(args, ctx: PublishContext) -> None:
    if args.env == "prod" and not args.offline:
        confirm = input(
            "WARNING: --env=prod will publish to LIVE Zenodo. Type 'prod' to continue: "
        ).strip()
        if confirm != "prod":
            die("Aborting: production environment not confirmed.")

    zenodo_enabled = not args.offline
    extra_assets = _parse_extra_assets(args.add_asset, args.asset_type)

    # Preflight / context
    src_md, book_yaml, site_repo, src_commit, src_origin, site_base, subjournal = (
        preflight_and_context(args)
    )
    ctx.site_repo = site_repo

    publication_date_iso = date.today().isoformat()
    publication_year = publication_date_iso[0:4]
    publication_date = publication_date_iso

    stem = src_md.stem
    if book_yaml is not None:
        t = title_from_book_yaml(book_yaml)
        if t:
            stem = t
    pub_type = "book" if book_yaml is not None else "article"
    resource_type = f"publication-{pub_type}"

    if not subjournal:
        inferred_sj = _infer_subjournal_from_provenance(site_repo, stem)
        if inferred_sj:
            subjournal = inferred_sj
            args.subjournal = inferred_sj
            echo(f"+ subjournal = {subjournal} (from provenance)")
        else:
            choices = ["documents", "posts", "prints", "reports"]
            default_sj = "prints"
            echo(f"Available subjournals: {', '.join(choices)}")
            ans_sj = input(
                f"Select subjournal [{'/'.join(choices)}] (default: {default_sj}): "
            ).strip().lower()
            if not ans_sj:
                ans_sj = default_sj
            if ans_sj not in choices:
                echo(
                    f"Unrecognized subjournal '{ans_sj}'. Valid options: {', '.join(choices)}"
                )
                die("Aborting: invalid subjournal.")
            subjournal = ans_sj
            args.subjournal = ans_sj
            echo(f"+ subjournal = {subjournal}")

    # Versioning / history
    is_new_version, prev_record_id, prev_concept, prev_prov_path, prev_prov = (
        determine_versioning(args, site_repo, subjournal, src_commit, stem)
    )
    change_log = prompt_change_log(is_new_version)

    # Branch
    orig_branch = run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=site_repo
    ).strip()
    ctx.orig_branch = orig_branch
    branch_name = prepare_branch(site_repo, stem, src_commit)
    ctx.branch_name = branch_name

    # Stage & render (PNPMD + optional book YAML → EPUB)
    assets_prefix = args.assets_prefix.strip("/")
    assets_repo = None
    if args.assets_dir:
        try:
            assets_repo = Path(args.assets_dir).resolve()
        except Exception:
            assets_repo = None
    pending_reuse = False
    pending_date = None
    prev_doi = ""
    prev_concept = ""
    prev_env_mismatch = None
    if (
        not args.offline
        and not args.new_version_of
        and prev_prov
        and prev_prov_path
    ):
        prev_doi = (prev_prov.get("doi") or "").strip()
        prev_concept = (prev_prov.get("concept_doi") or "").strip()
        prev_env_mismatch = _doi_env_mismatch(args, prev_doi, prev_concept)
        if _is_pending_doi(prev_doi) or prev_env_mismatch:
            pending_reuse = True
            pending_date = (prev_prov.get("publication_date") or "").strip() or None
            prev_source = prev_prov.get("source") or {}
            prev_commit = (prev_source.get("commit") or "").strip()
            if prev_env_mismatch:
                note = (
                    "previous DOI envs are mixed"
                    if "/" in prev_env_mismatch
                    else f"previous DOI appears to be {prev_env_mismatch}"
                )
                echo(f"WARNING: {note}; reusing artifacts to mint a fresh DOI.")
            if prev_commit and prev_commit != src_commit:
                echo(
                    "WARNING: previous provenance commit differs from current HEAD; "
                    "reusing artifacts to finish DOI minting."
                )
        else:
            prev_env_mismatch = None

    render_args: List[str] = []
    if args.omit_toc:
        render_args.append("--omit-toc")
    if args.omit_numbering:
        render_args.append("--omit-numbering")
    if args.as_is:
        render_args.append("--as-is")
    if args.toc_depth is not None:
        render_args += ["--toc-depth", str(args.toc_depth)]

    staged_pmd: Optional[Path] = None
    if pending_reuse:
        reused = _reuse_pending_artifacts(
            site_repo,
            subjournal,
            stem,
            prev_prov_path,
            prev_prov,
            assets_repo,
            assets_prefix,
        )
        if reused:
            (
                staging,
                staged_md,
                staged_pdf,
                staged_html,
                staged_embed_html,
                staged_epub,
                staged_pmd,
            ) = reused
            echo(f"+ reuse pending artifacts from {prev_prov_path}")
        else:
            pending_reuse = False
            echo("WARNING: pending artifacts missing; re-rendering.")

    if not pending_reuse:
        staging, staged_md, staged_pdf, staged_html, staged_embed_html, staged_epub = render_in_staging(
            site_repo,
            subjournal,
            src_md,
            publication_date_iso,
            book_yaml=book_yaml,
            render_args=render_args,
        )
        staged_pmd = staged_md.with_suffix(".pandoc.md")

    if pending_reuse and pending_date:
        publication_date_iso = pending_date
        publication_year = pending_date[0:4]
        publication_date = pending_date
    elif pending_reuse and not pending_date:
        echo("WARNING: pending provenance missing publication_date; using today's date.")

    if staged_pmd is None:
        die("Internal error: missing pandoc.md after staging.")

    # Parse PNPMD
    parsed = parse_pnpmd(staged_md.read_text(encoding="utf-8"))
    if pending_reuse:
        parsed = _apply_provenance_defaults(parsed, prev_prov)
    parsed = _apply_cli_overrides(parsed, args)
    if pending_reuse:
        parsed = _validate_required_metadata(parsed)
    else:
        parsed = _prompt_required_metadata(parsed)
        parsed = _prompt_missing_orcids(parsed)
    creators: List[Dict] = []
    for a in parsed["authors"]:
        if not a.get("name"):
            continue
        creators.append(
            {
                "name": a["name"],
                **({"orcid": a["orcid"]} if a.get("orcid") else {}),
                **({"email": a["email"]} if a.get("email") else {}),
            }
        )
    if pending_reuse and prev_prov_path and prev_prov:
        diffs = _provenance_diffs(prev_prov, parsed, creators)
        if diffs:
            if args.update_provenance:
                if _update_provenance_from_parsed(prev_prov_path, prev_prov, parsed, creators):
                    rel_prev = str(prev_prov_path.relative_to(site_repo))
                    run(["git", "add", rel_prev], cwd=site_repo)
                    echo(
                        f"+ updated provenance from front matter ({', '.join(diffs)})"
                    )
            else:
                echo(
                    "NOTE: provenance metadata differs from front matter; "
                    "re-run with --update-provenance to sync."
                )
    title = parsed["title"]

    # Zenodo deposition (reserve or new version)
    if zenodo_enabled:
        api, token, doi, concept_doi, dep_id = reserve_or_new_version(
            args,
            is_new_version,
            prev_record_id,
            prev_concept,
            title,
            creators,
            publication_year,
            pub_type,
        )
        ctx.api = api
        ctx.token = token
        ctx.dep_id = dep_id
    else:
        api = None
        token = None
        dep_id = None
        concept_doi = None
        doi = make_pending_doi(args, stem, src_commit, staged_md)
        echo(f"+ offline: pending DOI = {doi}")

    license_id = detect_license(staged_md, book_yaml)
    if not license_id:
        license_id = "cc-by-nc-nd-4.0"

    # Final destination
    if "/" in doi:
        doi_prefix, doi_suffix = doi.split("/", 1)
    else:
        die("Reserved DOI has no '/'?")

    final_dir = site_repo / subjournal / stem / doi_prefix / doi_suffix
    final_dir.mkdir(parents=True, exist_ok=True)
    ctx.final_dir = final_dir

    final_md = final_dir / staged_md.name
    final_pdf = final_dir / staged_pdf.name
    final_html = final_dir / staged_html.name
    final_embed_html = (
        final_dir / staged_embed_html.name if staged_embed_html is not None else None
    )
    final_pmd = final_dir / staged_pmd.name
    final_epub = final_dir / staged_epub.name if staged_epub is not None else None

    move_pairs = [
        (staged_md, final_md),
        (staged_pdf, final_pdf),
        (staged_html, final_html),
        (staged_pmd, final_pmd),
    ]
    if staged_embed_html is not None:
        move_pairs.append((staged_embed_html, final_embed_html))
    if staged_epub is not None:
        move_pairs.append((staged_epub, final_epub))

    for src, dst in move_pairs:
        echo(f"+ move {src} -> {dst}")
        shutil.move(str(src), str(dst))

    try:
        shutil.rmtree(staging)
    except Exception:
        pass

    for asset in extra_assets:
        dest = final_dir / asset.src.name
        if dest.exists():
            die(f"Extra asset would overwrite existing file: {dest}")
        echo(f"+ copy {asset.src} -> {dest}")
        shutil.copy2(asset.src, dest)
        asset.final_path = dest
        asset.assets_url = (
            f"{args.assets_base_url.rstrip('/')}/{assets_prefix}/"
            f"{stem}/{doi_prefix}/{doi_suffix}/{asset.src.name}"
        )

    site_html_url = (
        f"{site_base}/{subjournal}/{stem}/{doi_prefix}/{doi_suffix}/{final_html.name}"
    )
    site_md_url = (
        f"{site_base}/{subjournal}/{stem}/{doi_prefix}/{doi_suffix}/{final_md.name}"
    )
    site_pandoc_md_url = (
        f"{site_base}/{subjournal}/{stem}/{doi_prefix}/{doi_suffix}/{final_pmd.name}"
    )
    version_permalink = f"{site_base}/{subjournal}/{stem}/{doi_prefix}/{doi_suffix}/"
    assets_pdf_url = (
        f"{args.assets_base_url.rstrip('/')}/{assets_prefix}/"
        f"{stem}/{doi_prefix}/{doi_suffix}/{final_pdf.name}"
    )
    assets_embed_html_url = (
        f"{args.assets_base_url.rstrip('/')}/{assets_prefix}/"
        f"{stem}/{doi_prefix}/{doi_suffix}/{final_embed_html.name}"
        if final_embed_html is not None
        else None
    )
    if final_epub is not None:
        assets_epub_url = (
            f"{args.assets_base_url.rstrip('/')}/{assets_prefix}/"
            f"{stem}/{doi_prefix}/{doi_suffix}/{final_epub.name}"
        )
    else:
        assets_epub_url = None

    self_related_identifiers = [
        {
            "relation": "isIdenticalTo",
            "identifier": site_html_url,
            "resource_type": resource_type,
        },
        {
            "relation": "isIdenticalTo",
            "identifier": site_md_url,
            "resource_type": resource_type,
        },
        {
            "relation": "isIdenticalTo",
            "identifier": assets_pdf_url,
            "resource_type": resource_type,
        },
    ]
    if assets_embed_html_url:
        self_related_identifiers.append(
            {
                "relation": "isIdenticalTo",
                "identifier": assets_embed_html_url,
                "resource_type": resource_type,
            }
        )
    if assets_epub_url:
        self_related_identifiers.append(
            {
                "relation": "isIdenticalTo",
                "identifier": assets_epub_url,
                "resource_type": resource_type,
            }
        )

    extra_related_identifiers = []
    for asset in extra_assets:
        if asset.assets_url and asset.asset_type:
            extra_related_identifiers.append(
                {
                    "relation": "isIdenticalTo",
                    "identifier": asset.assets_url,
                    "resource_type": asset.asset_type,
                }
            )

    reference_related_identifiers = [
        {
            "relation": "cites",
            "identifier": ref_url,
            "resource_type": resource_type,
        }
        for ref_url in parsed["reference_doi_urls"]
    ]

    related_identifiers = (
        self_related_identifiers + extra_related_identifiers + reference_related_identifiers
    )

    # Notes must be non-empty; prefer one-sentence summary, then abstract, then title.
    notes_text = normalize_markdown_prose(parsed["one_sentence"])
    if not notes_text:
        notes_text = normalize_markdown_prose(parsed["abstract"])
    if not notes_text:
        notes_text = title

    zenodo_meta = {
        "upload_type": "publication",
        "publication_type": pub_type,
        "title": title,
        "creators": creators,
        "description": normalize_markdown_prose(parsed["abstract"]),
        "keywords": parsed["keywords"],
        "journal_title": args.journal,
        "publisher": {"name": args.journal},
        "publication_year": publication_year,
        "date": publication_date,
        "license": license_id,
        "related_identifiers": related_identifiers,
        "communities": [{"identifier": args.community}],
        "prereserve_doi": True,
    }
    zenodo_meta["notes"] = notes_text

    # Provenance
    prov_path = write_provenance(
        final_dir,
        final_md,
        final_pdf,
        final_html,
        final_embed_html,
        final_pmd,
        final_epub,
        src_origin,
        src_commit,
        title,
        creators,
        parsed,
        publication_date,
        publication_year,
        doi,
        concept_doi,
        assets_pdf_url,
        assets_epub_url,
        assets_embed_html_url,
        site_html_url,
        site_md_url,
        site_pandoc_md_url,
        version_permalink,
        zenodo_metadata=zenodo_meta,
        journal_name=args.journal,
        subjournal=subjournal,
        change_log=change_log,
        publication_type=pub_type,
    )

    # Preview
    preview_actions(
        site_repo,
        final_md,
        final_html,
        final_embed_html,
        final_pmd,
        prov_path,
        final_pdf,
        final_epub,
        extra_assets,
        assets_prefix,
        stem,
        doi_prefix,
        doi_suffix,
        dep_id,
        title,
        publication_date,
        doi,
        branch_name,
        args,
        zenodo_enabled,
        zenodo_meta,
    )

    # Confirmation
    prompt = "\nProceed with publication commit"
    if zenodo_enabled:
        prompt += " and DOI minting"
    else:
        prompt += " (Zenodo skipped)"
    prompt += "? [y/N]: "
    ans = input(prompt).strip().lower()
    if ans not in ("y", "yes"):
        echo("Aborting; cleaning up Zenodo draft, git branch, and files.")
        cleanup_best_effort(ctx)
        sys.exit(0)

    # Determine rendered artifacts (ignore CSS).
    upload_paths = sorted(
        p
        for p in final_dir.iterdir()
        if p.is_file()
        and (
            p.name.endswith(".pandoc.md")
            or p.suffix.lower() in {".md", ".pdf", ".html", ".epub"}
        )
    )
    for asset in extra_assets:
        if asset.final_path and asset.final_path not in upload_paths:
            upload_paths.append(asset.final_path)
    upload_paths = sorted(upload_paths, key=lambda p: p.name)

    echo("\n--- FILES TO UPLOAD TO ZENODO ---")
    for p in upload_paths:
        echo(f" - {p.name}")

    # Commit site repo: stage non-binary artifacts only (.md/.html/.pandoc.md/.yml/.yaml/.json/.txt/.md).
    allowed_exts = {".md", ".html", ".yaml", ".yml", ".json", ".txt"}
    extra_asset_paths = {
        asset.final_path for asset in extra_assets if asset.final_path is not None
    }
    files_to_stage = [
        p
        for p in final_dir.iterdir()
        if p.is_file()
        and not p.name.endswith(".embed.html")
        and (p.name.endswith(".pandoc.md") or p.suffix in allowed_exts)
        and p not in extra_asset_paths
    ]
    if not files_to_stage:
        die(f"No files to stage in {final_dir}")

    rel_paths = [str(p.relative_to(site_repo)) for p in files_to_stage]
    run(["git", "add"] + rel_paths, cwd=site_repo)
    run(
        [
            "git",
            "commit",
            "-m",
            f"Publish print: {title} ({publication_date}, DOI {doi}); "
            f"source {src_commit[:10]} as '{final_md.stem}'",
        ],
        cwd=site_repo,
    )

    concept_doi_updated = None
    if zenodo_enabled:
        # Apply final metadata
        _ = http_json(
            "PUT",
            f"{api}/deposit/depositions/{dep_id}",
            token,
            data={"metadata": zenodo_meta},
        )

        # Upload & publish
        dep = ensure_draft_or_die(api, token, dep_id)
        bucket_url = (dep.get("links") or {}).get("bucket")
        if not bucket_url:
            die("Draft has no bucket link; cannot upload.")

        from urllib.parse import quote

        # Upload the actual rendered artifacts (ignore CSS).

        for path in upload_paths:
            fname = path.name
            put_url = f"{bucket_url}/{quote(fname)}"
            with open(path, "rb") as fh:
                http_put_raw(put_url, token, fh)
            print("sleeping 1")
            time.sleep(1)

        _published = http_json(
            "POST", f"{api}/deposit/depositions/{dep_id}/actions/publish", token
        )

        # Post-publish: concept DOI update
        try:
            record = http_json("GET", f"{api}/records/{dep_id}", token, data=None)
            concept_doi_rec = record.get("conceptdoi")
            if concept_doi_rec:
                echo(f"\nConcept DOI from record: {concept_doi_rec}")
                ans_cd = input(
                    "Update provenance.yaml with this concept DOI? [Y/n]: "
                ).strip().lower()
                if ans_cd in ("", "y", "yes"):
                    import yaml as _yaml

                    try:
                        prov_data = _yaml.safe_load(
                            prov_path.read_text(encoding="utf-8")
                        ) or {}
                        concept_doi_old = prov_data.get("concept_doi")
                        if concept_doi_old == concept_doi_rec:
                            echo("Concept DOI unchanged; provenance already up to date.")
                        else:
                            echo(
                                f"Updating concept DOI "
                                f"{concept_doi_old or 'None'} → {concept_doi_rec}"
                            )
                            prov_data["concept_doi"] = concept_doi_rec
                            prov_path.write_text(
                                dump_yaml(prov_data),
                                encoding="utf-8",
                            )
                            rel_prov2 = str(prov_path.relative_to(site_repo))
                            run(["git", "add", rel_prov2], cwd=site_repo)
                            run(
                                [
                                    "git",
                                    "commit",
                                    "-m",
                                    f"Update concept DOI {concept_doi_old or 'None'} → {concept_doi_rec}",
                                ],
                                cwd=site_repo,
                            )
                            concept_doi_updated = concept_doi_rec
                    except Exception as e:
                        echo(f"WARNING: Failed to update provenance with concept DOI: {e}")
            else:
                echo("No concept DOI present in record; leaving provenance as-is.")
        except Exception as e:
            echo(f"WARNING: Failed to retrieve record to update concept DOI: {e}")
    else:
        echo("\n[offline] Skipping Zenodo upload and publish.")

    # Assets repo (push after Zenodo is finished)
    if args.assets_dir:
        assets_repo = Path(args.assets_dir).resolve()
        if not (assets_repo / ".git").exists():
            die(f"Assets dir is not a git repo: {assets_repo}")

        dest_pdf = assets_repo / assets_prefix / stem / doi_prefix / doi_suffix / final_pdf.name
        _copy_if_changed(final_pdf, dest_pdf)
        paths_to_add = [os.path.relpath(dest_pdf, assets_repo)]

        if final_embed_html is not None:
            dest_embed_html = (
                assets_repo / assets_prefix / stem / doi_prefix / doi_suffix / final_embed_html.name
            )
            _copy_if_changed(final_embed_html, dest_embed_html)
            paths_to_add.append(os.path.relpath(dest_embed_html, assets_repo))

        if final_epub is not None:
            dest_epub = (
                assets_repo / assets_prefix / stem / doi_prefix / doi_suffix / final_epub.name
            )
            _copy_if_changed(final_epub, dest_epub)
            paths_to_add.append(os.path.relpath(dest_epub, assets_repo))

        for asset in extra_assets:
            if asset.final_path is None:
                continue
            size = asset.final_path.stat().st_size
            if size > MAX_EXTRA_ASSET_BYTES:
                die(
                    f"Extra asset too large for assets repo (>1MB): "
                    f"{asset.final_path} ({size} bytes)"
                )
            dest_asset = (
                assets_repo / assets_prefix / stem / doi_prefix / doi_suffix / asset.final_path.name
            )
            _copy_if_changed(asset.final_path, dest_asset)
            paths_to_add.append(os.path.relpath(dest_asset, assets_repo))

        run(["git", "add"] + paths_to_add, cwd=assets_repo)
        staged_paths = git_staged_paths(assets_repo)
        if not staged_paths:
            echo("+ assets unchanged; skipping assets commit/push.")
        elif args.no_assets_push:
            echo("+ assets staged (--no-assets-push); skipping commit/push.")
        else:
            suffix_parts = []
            if final_embed_html is not None:
                suffix_parts.append("embed.html")
            if final_epub is not None:
                suffix_parts.append("epub")
            if extra_assets:
                suffix_parts.append("extra-assets")
            suffix = f", {', '.join(suffix_parts)}" if suffix_parts else ""
            run(
                [
                    "git",
                    "commit",
                    "-m",
                    f"{title}.pdf ({publication_date}, {doi}){suffix}",
                ],
                cwd=assets_repo,
            )
            run(["git", "push"], cwd=assets_repo)

    # Merge branch into main
    run(["git", "checkout", "main"], cwd=site_repo)
    run(["git", "merge", "--no-ff", branch_name], cwd=site_repo)
    run(["git", "push", "origin", "main"], cwd=site_repo)
    run(["git", "branch", "-d", branch_name], cwd=site_repo)

    status_line = "Publication committed and DOI minted"
    if not zenodo_enabled:
        status_line = "Publication committed (Zenodo skipped)"
    echo(
        f"\n✅ {status_line}"
        f"\nVersion DOI: {doi}"
        f"\nConcept DOI: {concept_doi_updated or concept_doi or '(none)'}"
        f"\nPermalink: {version_permalink}"
        f"\nFolder: {final_dir}"
    )


def main():
    args = parse_args()
    ctx = PublishContext()
    try:
        run_publish(args, ctx)
    except SystemExit as e:
        # Only cleanup on non-zero exit; success or user-no-with-0 handled already.
        if e.code not in (0, None):
            cleanup_best_effort(ctx)
        raise
    except BaseException:
        cleanup_best_effort(ctx)
        raise


if __name__ == "__main__":
    main()

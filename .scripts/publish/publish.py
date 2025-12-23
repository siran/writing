#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
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


# ---------------- git helpers ----------------

def slug_branch(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9._-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    s = s.lstrip(".-")
    if s.endswith(".lock"):
        s = s[:-5] + "-lock"
    return s[:80] or "x"


def git_repo_root(path: Path) -> Path:
    out = run(["git", "rev-parse", "--show-toplevel"], cwd=path)
    root = out.strip()
    if not root:
        die("not inside a git repository")
    return Path(root)


def git_status_clean(repo: Path) -> bool:
    out = run(["git", "status", "--porcelain"], cwd=repo)
    return out.strip() == ""


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


def _prompt_missing_orcids(parsed: dict) -> dict:
    """
    Ensure each author has an ORCID. Prompts interactively when missing.
    """
    updated = dict(parsed)
    authors = [dict(a) for a in (updated.get("authors") or [])]
    for author in authors:
        name = (author.get("name") or "").strip()
        if not name or author.get("orcid"):
            continue
        while True:
            raw = input(
                f"Enter ORCID for {name} "
                "(format 0000-0000-0000-0000, or 'skip' to omit): "
            ).strip()
            if not raw:
                echo("ORCID is required for Zenodo; enter an ORCID or type 'skip' to omit.")
                continue
            if raw.lower() in {"skip", "none", "n/a"}:
                break
            orcid = _normalize_orcid_input(raw)
            if orcid:
                author["orcid"] = orcid
                break
            echo("Invalid ORCID format. Example: 0000-0000-0000-0000 or https://orcid.org/0000-0000-0000-0000")
    updated["authors"] = authors
    return updated


def preflight_and_context(
    args,
) -> Tuple[Path, Optional[Path], Path, str, str, str, str]:
    """
    Resolve src_md and optional book_yaml, check git, infer site_base/journal/subjournal.
    Returns:
        src_md, book_yaml, site_repo, src_commit, src_origin, site_base, subjournal
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

    if not args.subjournal:
        choices = ["documents", "posts", "prints", "reports"]
        default_sj = "prints"
        echo(f"Available subjournals: {', '.join(choices)}")
        ans_sj = input(
            f"Select subjournal [{'/'.join(choices)}] (default: {default_sj}): "
        ).strip().lower()
        if not ans_sj:
            ans_sj = default_sj
        if ans_sj not in choices:
            echo(f"Unrecognized subjournal '{ans_sj}'. Valid options: {', '.join(choices)}")
            die("Aborting: invalid subjournal.")
        args.subjournal = ans_sj
    echo(f"+ subjournal = {args.subjournal}")

    return src_md, book_yaml, site_repo, src_commit, src_origin, site_base, args.subjournal


def determine_versioning(
    args, site_repo: Path, subjournal: str, src_commit: str, stem: str
) -> Tuple[bool, Optional[int], Optional[str]]:
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

        if prev_commit and prev_commit == src_commit:
            die(f"This commit has already been published as DOI {prev_doi or '(unknown)'}.")

        echo(
            f"Found previous publication for stem '{prev_stem}' in subjournal '{subjournal}':"
        )
        echo(f" - provenance: {prov_path_prev}")
        echo(f" - DOI:        {prev_doi or '(none)'}")
        echo(f" - concept_doi:{prev_concept or '(none)'}")
        echo(f" - commit:     {prev_commit or '(unknown)'}")

        if args.new_version_of:
            is_new_version = True
            prev_record_id = record_id_from_doi(prev_doi)
            if not prev_record_id:
                die(f"Cannot extract Zenodo record id from previous DOI '{prev_doi}'.")
        else:
            ans_ver = input(
                f"Treat this as a new version of the latest one? [y/N]: "
            ).strip().lower()
            if ans_ver in ("y", "yes"):
                is_new_version = True
                prev_record_id = record_id_from_doi(prev_doi)
                if not prev_record_id:
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

    return is_new_version, prev_record_id, prev_concept


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
    final_pmd: Path,
    prov_path: Path,
    final_pdf: Path,
    final_epub: Optional[Path],
    assets_prefix: str,
    stem: str,
    doi_prefix: str,
    doi_suffix: str,
    dep_id: int,
    title: str,
    publication_date: str,
    doi: str,
    branch_name: str,
    args,
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
    for p in [final_md, final_html, final_pmd, prov_path]:
        echo(f" - {p.relative_to(site_repo)}")

    echo("\n--- FILES TO UPLOAD TO ZENODO ---")
    upload_list = [final_md, final_pdf, final_pmd, final_html]
    if final_epub is not None:
        upload_list.append(final_epub)
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
        if final_epub is not None:
            echo(
                f"  copy {final_epub} -> "
                f"{args.assets_dir}/{assets_prefix}/{stem}/{doi_prefix}/{doi_suffix}/{final_epub.name}"
            )
        echo("  git add <those files>")
        if not args.no_assets_push:
            echo("  git commit ...")
            echo("  git push")
    echo("Zenodo:")
    echo(
        f"  PUT /deposit/depositions/{dep_id} "
        f"(full metadata incl. related_identifiers)"
    )
    echo("  PUT md, PDF, pandoc.md, html" + (", epub" if final_epub is not None else "") + " to bucket")
    echo("  POST /deposit/depositions/{id}/actions/publish")
    echo(f"  GET /records/{dep_id} (fetch concept DOI)")
    echo("  update provenance.yaml with concept DOI (optional, then commit)")
    echo("Git:")
    echo("  git checkout main")
    echo(f"  git merge --no-ff {branch_name}")
    echo("  git push origin main")
    echo(f"  git branch -d {branch_name}")


# ---------------- main publish workflow ----------------

def run_publish(args, ctx: PublishContext) -> None:
    if args.env == "prod":
        confirm = input(
            "WARNING: --env=prod will publish to LIVE Zenodo. Type 'prod' to continue: "
        ).strip()
        if confirm != "prod":
            die("Aborting: production environment not confirmed.")

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

    # Versioning / history
    is_new_version, prev_record_id, prev_concept = determine_versioning(
        args, site_repo, subjournal, src_commit, stem
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
    render_args: List[str] = []
    if args.omit_toc:
        render_args.append("--omit-toc")
    if args.omit_numbering:
        render_args.append("--omit-numbering")
    if args.as_is:
        render_args.append("--as-is")
    if args.toc_depth is not None:
        render_args += ["--toc-depth", str(args.toc_depth)]

    staging, staged_md, staged_pdf, staged_html, staged_epub = render_in_staging(
        site_repo,
        subjournal,
        src_md,
        publication_date_iso,
        book_yaml=book_yaml,
        render_args=render_args,
    )
    staged_pmd = staged_md.with_suffix(".pandoc.md")

    # Parse PNPMD
    parsed = parse_pnpmd(staged_md.read_text(encoding="utf-8"))
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
    title = parsed["title"]

    # Zenodo deposition (reserve or new version)
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
    final_pmd = final_dir / staged_pmd.name
    final_epub = final_dir / staged_epub.name if staged_epub is not None else None

    move_pairs = [
        (staged_md, final_md),
        (staged_pdf, final_pdf),
        (staged_html, final_html),
        (staged_pmd, final_pmd),
    ]
    if staged_epub is not None:
        move_pairs.append((staged_epub, final_epub))

    for src, dst in move_pairs:
        echo(f"+ move {src} -> {dst}")
        shutil.move(str(src), str(dst))

    try:
        shutil.rmtree(staging)
    except Exception:
        pass

    assets_prefix = args.assets_prefix.strip("/")

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
    if assets_epub_url:
        self_related_identifiers.append(
            {
                "relation": "isIdenticalTo",
                "identifier": assets_epub_url,
                "resource_type": resource_type,
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

    related_identifiers = self_related_identifiers + reference_related_identifiers

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
        final_pmd,
        prov_path,
        final_pdf,
        final_epub,
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
        zenodo_meta,
    )

    # Confirmation
    ans = input("\nProceed with publication commit and DOI minting? [y/N]: ").strip().lower()
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

    echo("\n--- FILES TO UPLOAD TO ZENODO ---")
    for p in upload_paths:
        echo(f" - {p.name}")

    # Commit site repo: stage non-binary artifacts only (.md/.html/.pandoc.md/.yml/.yaml/.json/.txt/.md).
    allowed_exts = {".md", ".html", ".yaml", ".yml", ".json", ".txt"}
    files_to_stage = [
        p for p in final_dir.iterdir() if p.is_file() and (p.name.endswith(".pandoc.md") or p.suffix in allowed_exts)
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

    # Assets repo
    if args.assets_dir:
        assets_repo = Path(args.assets_dir).resolve()
        if not (assets_repo / ".git").exists():
            die(f"Assets dir is not a git repo: {assets_repo}")

        dest_pdf = assets_repo / assets_prefix / stem / doi_prefix / doi_suffix / final_pdf.name
        dest_pdf.parent.mkdir(parents=True, exist_ok=True)
        echo(f"+ copy {final_pdf} -> {dest_pdf}")
        shutil.copy2(final_pdf, dest_pdf)

        paths_to_add = [os.path.relpath(dest_pdf, assets_repo)]

        if final_epub is not None:
            dest_epub = (
                assets_repo / assets_prefix / stem / doi_prefix / doi_suffix / final_epub.name
            )
            dest_epub.parent.mkdir(parents=True, exist_ok=True)
            echo(f"+ copy {final_epub} -> {dest_epub}")
            shutil.copy2(final_epub, dest_epub)
            paths_to_add.append(os.path.relpath(dest_epub, assets_repo))

        run(["git", "add"] + paths_to_add, cwd=assets_repo)
        if not args.no_assets_push:
            suffix = ", epub" if final_epub is not None else ""
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
    concept_doi_updated = None
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

    # Merge branch into main
    run(["git", "checkout", "main"], cwd=site_repo)
    run(["git", "merge", "--no-ff", branch_name], cwd=site_repo)
    run(["git", "push", "origin", "main"], cwd=site_repo)
    run(["git", "branch", "-d", branch_name], cwd=site_repo)

    echo(
        f"\n✅ Publication committed and DOI minted"
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

#!/usr/bin/env python3
"""
Copy a script/directory from writing/.scripts to sibling repos.

Interactive prompts:
- choose which item under .scripts to copy (e.g., render/, build_site/, publish/ or any file)
- choose targets (preferredframe = main site, research = preprints)
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = ROOT / ".scripts"

# Known sibling repos; adjust here if paths change.
TARGETS = {
    "preferredframe (main site)": ROOT.parent / "preferredframe",
    "research (preprints)": ROOT.parent / "research",
}


def prompt_yes_no(message: str, default: bool = False) -> bool:
    suffix = " [Y/n]: " if default else " [y/N]: "
    answer = input(message + suffix).strip().lower()
    if not answer:
        return default
    return answer in {"y", "yes"}


def choose_item() -> Path:
    if not SCRIPTS_DIR.exists():
        sys.exit(f".scripts directory not found at {SCRIPTS_DIR}")

    options = sorted(
        p for p in SCRIPTS_DIR.iterdir() if not p.name.startswith(".") and p.name != Path(__file__).name
    )
    print("Available items under .scripts:")
    for p in options:
        kind = "/" if p.is_dir() else ""
        print(f" - {p.name}{kind}")

    name = input("Item to replicate (exact name from above): ").strip()
    if not name:
        sys.exit("No item selected.")

    src = SCRIPTS_DIR / name
    if not src.exists():
        sys.exit(f"Not found: {src}")
    return src


def select_targets():
    chosen = []
    for label, repo_root in TARGETS.items():
        scripts_path = repo_root / ".scripts"
        if not scripts_path.exists():
            print(f"Skip {label}: missing {scripts_path}")
            continue
        if prompt_yes_no(f"Replicate to {label} at {scripts_path}?"):
            chosen.append(scripts_path)
    if not chosen:
        sys.exit("No targets selected.")
    return chosen


def run_rsync(src: Path, dest_scripts: Path) -> int:
    dest_scripts.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        dest = dest_scripts / src.name
        dest.mkdir(parents=True, exist_ok=True)
        cmd = [
            "rsync",
            "-av",
            "--delete",
            "--exclude",
            "__pycache__/",
            str(src) + "/",
            str(dest) + "/",
        ]
    else:
        cmd = ["rsync", "-av", str(src), str(dest_scripts)]

    print("\n", " ".join(cmd))
    return subprocess.call(cmd)


def main() -> int:
    src = choose_item()
    targets = select_targets()

    failures = 0
    for dest in targets:
        print(f"\n=== Syncing to {dest} ===")
        rc = run_rsync(src, dest)
        if rc != 0:
            print(f"Failed (exit {rc}) for {dest}")
            failures += 1
    if failures:
        return 1

    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

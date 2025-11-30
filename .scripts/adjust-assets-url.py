#!/usr/bin/env python3
import re
import shutil
import subprocess
from pathlib import Path
import sys

# --- config ---
SIRAN_ROOT = Path.home() / "src" / "siran"
ASSETS_ROOT = SIRAN_ROOT / "assets"
BASE_URL = "https://siran.github.io/assets"
TARGET_DIR = Path.cwd()   # only current directory

# --- choose assets subdir ---
if not ASSETS_ROOT.is_dir():
    sys.exit(f"Assets dir not found: {ASSETS_ROOT}")

subdirs = [d.name for d in ASSETS_ROOT.iterdir() if d.is_dir()]
if not subdirs:
    sys.exit(f"No subdirs in {ASSETS_ROOT}")

print("Choose assets subdir:")
for i, name in enumerate(subdirs, 1):
    print(f"{i}) {name}")

try:
    idx = int(input("> ").strip())
except ValueError:
    sys.exit("Invalid choice (not a number)")

if not (1 <= idx <= len(subdirs)):
    sys.exit("Invalid choice (out of range)")

chosen = subdirs[idx - 1]
chosen_dir = ASSETS_ROOT / chosen

print(f"\nUsing assets subdir: {chosen_dir}\n")

# --- find asset links in markdown files (current dir only) ---
link_pattern = re.compile(r'(!?\[[^\]]*\]\()([^)]+)(\))')

# local asset files referenced like assets/filename.ext
local_assets = set()  # set of Paths relative to TARGET_DIR

md_files = list(TARGET_DIR.glob("*.md"))

for md in md_files:
    text = md.read_text(encoding="utf-8")

    for m in link_pattern.finditer(text):
        url = m.group(2).strip()

        # ignore remote URLs
        if url.startswith(("http://", "https://")):
            continue

        # we care about links starting exactly with "assets/"
        if url.startswith("assets/"):
            rel_path = Path(url)  # e.g. assets/foo.png or assets/sub/foo.png
            # assume the file is relative to the current dir
            local_assets.add(rel_path)

print("Found asset references:")
for p in sorted(local_assets):
    print("  ", p)
print()

# --- move assets into chosen_dir ---
moved = []
skipped_missing = []
skipped_conflict = []

for rel in sorted(local_assets):
    src = TARGET_DIR / rel
    filename = rel.name
    dst = chosen_dir / filename

    if not src.exists():
        skipped_missing.append((rel, "source missing"))
        continue

    if dst.exists():
        # if same content, just delete the local copy
        try:
            if src.read_bytes() == dst.read_bytes():
                src.unlink()
                print(f"deleted duplicate local asset: {src}")
                continue
            else:
                skipped_conflict.append((rel, "target exists with different content"))
                continue
        except Exception as e:
            skipped_conflict.append((rel, f"error comparing files: {e}"))
            continue

    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dst))
    moved.append((src, dst))
    print(f"moved {src} -> {dst}")

print()
print("Summary of asset moves:")
print(f"  moved: {len(moved)}")
print(f"  missing: {len(skipped_missing)}")
print(f"  conflicts: {len(skipped_conflict)}")
print()

# --- rewrite URLs in markdown files (current dir only) ---
def rewrite_url(url: str) -> str:
    # leave remote URLs as-is
    if url.startswith(("http://", "https://")):
        return url

    if url.startswith("assets/"):
        filename = Path(url).name
        return f"{BASE_URL}/{chosen}/{filename}"

    return url

for md in md_files:
    text = md.read_text(encoding="utf-8")

    def repl(m):
        before, url, after = m.groups()
        new_url = rewrite_url(url.strip())
        return f"{before}{new_url}{after}"

    new_text = link_pattern.sub(repl, text)

    if new_text != text:
        md.write_text(new_text, encoding="utf-8")
        print("updated markdown:", md)

print()

# --- optionally git add/commit/push in assets repo ---
if moved:
    answer = input(
        f"Git add, commit, and push changes in {ASSETS_ROOT}? [y/N] "
    ).strip().lower()

    if answer == "y":
        # only add moved files (in assets repo)
        rel_paths_for_git = [
            dst.relative_to(ASSETS_ROOT) for (_src, dst) in moved
        ]
        try:
            if rel_paths_for_git:
                subprocess.run(
                    ["git", "-C", str(ASSETS_ROOT), "add"]
                    + [str(p) for p in rel_paths_for_git],
                    check=True,
                )

            commit_msg = f"Move assets for {chosen} from {TARGET_DIR.relative_to(SIRAN_ROOT)}"
            subprocess.run(
                ["git", "-C", str(ASSETS_ROOT), "commit", "-m", commit_msg],
                check=True,
            )
            subprocess.run(
                ["git", "-C", str(ASSETS_ROOT), "push"],
                check=True,
            )
            print("Git add/commit/push done in assets repo.")
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {e}")
    else:
        print("Skipping git add/commit/push in assets repo.")
else:
    print("No assets moved; nothing to commit in assets repo.")

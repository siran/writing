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


def resolve_target(argv):
    if not argv:
        target_dir = Path.cwd()
        md_files = list(target_dir.glob("*.md"))
        return target_dir, md_files

    if len(argv) > 1:
        sys.exit("Usage: adjust-assets-url.py [path-to-md-or-dir]")

    target = Path(argv[0]).expanduser()
    if not target.is_absolute():
        target = (Path.cwd() / target).resolve()

    if target.is_dir():
        target_dir = target
        md_files = list(target_dir.glob("*.md"))
        return target_dir, md_files

    if target.is_file():
        if target.suffix.lower() != ".md":
            sys.exit(f"Target file is not .md: {target}")
        return target.parent, [target]

    sys.exit(f"Target path not found: {target}")

def extract_cover_image(book_yml: Path):
    if not book_yml.exists():
        return None

    text = book_yml.read_text(encoding="utf-8")
    m = re.search(r"^cover-image\s*:\s*(.+)$", text, re.MULTILINE)
    if not m:
        return None

    val = m.group(1).strip()
    if (val.startswith('"') and val.endswith('"')) or (
        val.startswith("'") and val.endswith("'")
    ):
        val = val[1:-1].strip()

    return val or None


def update_cover_image(book_yml: Path, new_url: str):
    text = book_yml.read_text(encoding="utf-8")
    new_line = f"cover-image: {new_url}"
    new_text, count = re.subn(
        r"^cover-image\s*:\s*(.+)$",
        new_line,
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if count == 0:
        sys.exit(f"cover-image not found in {book_yml}")
    book_yml.write_text(new_text, encoding="utf-8")


TARGET_DIR, md_files = resolve_target(sys.argv[1:])
if not md_files:
    sys.exit(f"No markdown files found in: {TARGET_DIR}")

# --- choose assets subdir ---
if not ASSETS_ROOT.is_dir():
    sys.exit(f"Assets dir not found: {ASSETS_ROOT}")

subdirs = sorted(
    [d.name for d in ASSETS_ROOT.iterdir() if d.is_dir() and not d.name.startswith(".")],
    key=str.casefold,
)

print("Choose assets subdir:")
for i, name in enumerate(subdirs, 1):
    print(f"{i}) {name}")
print(f"N) create new subdir [{TARGET_DIR.name}]")

choice = input("> ").strip()

if choice.lower() in {"n", "new"}:
    chosen = input(f"New subdir name [{TARGET_DIR.name}]: ").strip() or TARGET_DIR.name
    if any(sep in chosen for sep in ("/", "\\")):
        sys.exit("Subdir name must not contain path separators")
    chosen_dir = ASSETS_ROOT / chosen
    chosen_dir.mkdir(parents=True, exist_ok=True)
elif choice in subdirs:
    chosen = choice
    chosen_dir = ASSETS_ROOT / chosen
else:
    try:
        idx = int(choice)
    except ValueError:
        sys.exit("Invalid choice")

    if not (1 <= idx <= len(subdirs)):
        sys.exit("Invalid choice (out of range)")

    chosen = subdirs[idx - 1]
    chosen_dir = ASSETS_ROOT / chosen

print(f"\nUsing assets subdir: {chosen_dir}\n")

# --- find asset links in markdown files (target dir or file) ---
link_pattern = re.compile(r'(!?\[[^\]]*\]\()([^)]+)(\))')

# local asset files referenced like assets/filename.ext
local_assets = set()  # set of Paths relative to TARGET_DIR

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
            # assume the file is relative to the target dir
            local_assets.add(rel_path)

print("Found asset references:")
for p in sorted(local_assets):
    print("  ", p)
print()

# --- detect local cover-image in book.yml ---
book_yml = TARGET_DIR / "book.yml"
cover_value = extract_cover_image(book_yml)
cover_src = None

if cover_value and not cover_value.startswith(("http://", "https://")):
    cover_path = Path(cover_value)
    cover_src = cover_path if cover_path.is_absolute() else (TARGET_DIR / cover_path)
    print("Found local cover-image:")
    print("  ", cover_src)
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

cover_updated = False
if cover_src is not None:
    dst = chosen_dir / cover_src.name

    if not cover_src.exists():
        skipped_missing.append((cover_src, "cover-image source missing"))
    elif dst.exists():
        try:
            if cover_src.read_bytes() == dst.read_bytes():
                cover_src.unlink()
                print(f"deleted duplicate local cover-image: {cover_src}")
                update_cover_image(book_yml, f"{BASE_URL}/{chosen}/{dst.name}")
                cover_updated = True
            else:
                skipped_conflict.append((cover_src, "cover-image target exists with different content"))
        except Exception as e:
            skipped_conflict.append((cover_src, f"error comparing cover-image files: {e}"))
    else:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(cover_src), str(dst))
        moved.append((cover_src, dst))
        print(f"moved cover-image {cover_src} -> {dst}")
        update_cover_image(book_yml, f"{BASE_URL}/{chosen}/{dst.name}")
        cover_updated = True

print()
print("Summary of asset moves:")
print(f"  moved: {len(moved)}")
print(f"  missing: {len(skipped_missing)}")
print(f"  conflicts: {len(skipped_conflict)}")
if cover_updated:
    print("  updated book.yml cover-image")
print()

# --- rewrite URLs in markdown files (target dir or file) ---
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

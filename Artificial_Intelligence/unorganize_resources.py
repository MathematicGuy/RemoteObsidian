"""
unorganize_resources.py
========================
Flattens Artificial_Intelligence/3_RESOURCES/** by lifting all .md and .canvas files
up to the Artificial_Intelligence/ root, so the vault-organizer-agent can
re-classify and re-organize them from scratch.

Non-markdown files (PDFs, images, .mdb, etc.) are LEFT IN PLACE.
After all markdown files are moved, empty subdirectories are removed.

Usage (run from the vault root D:\\Personlich\\RemoteObsidian):
    python Artificial_Intelligence/unorganize_resources.py [--dry-run]

Options:
    --dry-run   Show what WOULD be moved without actually doing anything.
"""

import argparse
import os
import shutil
import sys

# Force UTF-8 output on Windows to handle Unicode filenames
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

import subprocess
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
VAULT_ROOT = Path(__file__).resolve().parent.parent   # ...RemoteObsidian/
AI_ROOT    = Path(__file__).resolve().parent           # ...Artificial_Intelligence/
RESOURCES  = AI_ROOT / "3_RESOURCES"

MD_EXTS    = {".md", ".canvas"}
SKIP_NAMES = {"readme.md"}                             # filenames to always skip

# ---------------------------------------------------------------------------


def git_snapshot(vault_root: Path, message: str) -> None:
    """Stage all changes and commit a pre-flight snapshot."""
    try:
        subprocess.run(["git", "add", "-A"], cwd=str(vault_root), check=True,
                       capture_output=True)
        result = subprocess.run(["git", "status", "--porcelain"],
                                cwd=str(vault_root), capture_output=True, text=True)
        if not result.stdout.strip():
            print("[GIT] Working tree already clean — no snapshot needed.")
            return
        subprocess.run(["git", "commit", "-m", message], cwd=str(vault_root),
                       check=True, capture_output=True)
        print(f"[GIT] Snapshot committed: {message}")
    except Exception as e:
        print(f"[GIT WARNING] {e}", file=sys.stderr)


def safe_dest(dest: Path) -> Path:
    """Return dest path, appending _1, _2 … if it already exists."""
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    counter = 1
    while True:
        candidate = dest.with_name(f"{stem}_{counter}{suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def remove_empty_dirs(root: Path) -> int:
    """Recursively remove empty directories inside root. Returns count removed."""
    removed = 0
    # Walk bottom-up so children are cleared before parents
    for dirpath, dirs, files in os.walk(str(root), topdown=False):
        p = Path(dirpath)
        if p == root:
            continue
        try:
            p.rmdir()          # Only removes if actually empty
            print(f"  [RMDIR] {p.relative_to(VAULT_ROOT)}")
            removed += 1
        except OSError:
            pass               # Not empty — has non-markdown files, skip
    return removed


def main() -> None:
    parser = argparse.ArgumentParser(description="Unorganize 3_RESOURCES markdown files")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview moves without making changes")
    args = parser.parse_args()
    dry = args.dry_run

    if not RESOURCES.is_dir():
        print(f"[ERROR] 3_RESOURCES not found at {RESOURCES}", file=sys.stderr)
        sys.exit(1)

    if not dry:
        print("[GIT] Creating pre-flight snapshot...")
        git_snapshot(VAULT_ROOT, "unorganize-resources: pre-flight snapshot")

    # --- Collect all markdown files inside 3_RESOURCES ---
    candidates = []
    for path in sorted(RESOURCES.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in MD_EXTS:
            continue
        if path.name.lower() in SKIP_NAMES:
            continue
        if any(part.startswith(".") for part in path.parts):
            continue          # skip hidden dirs like .obsidian, .space
        # Only lift files that are INSIDE a subdirectory (not already at 3_RESOURCES root)
        if path.parent == RESOURCES:
            continue
        candidates.append(path)

    print(f"\n{'[DRY RUN] ' if dry else ''}Found {len(candidates)} files to move to AI root.\n")

    moved   = 0
    skipped = 0

    for src in candidates:
        dest = safe_dest(AI_ROOT / src.name)
        rel_src  = src.relative_to(VAULT_ROOT)
        rel_dest = dest.relative_to(VAULT_ROOT)

        print(f"  {'[WOULD MOVE]' if dry else '[MOVE]'} {rel_src}  ->  {rel_dest}")

        if not dry:
            try:
                shutil.move(str(src), str(dest))
                moved += 1
            except Exception as e:
                print(f"    [ERROR] {e}", file=sys.stderr)
                skipped += 1
        else:
            moved += 1

    # --- Remove now-empty directories ---
    if not dry:
        print("\n[CLEANUP] Removing empty subdirectories in 3_RESOURCES...")
        removed_dirs = remove_empty_dirs(RESOURCES)
        print(f"[CLEANUP] Removed {removed_dirs} empty directories.\n")

        print(f"[DONE] Moved: {moved} | Skipped: {skipped}")
        print(f"\nNext step → run the vault-organizer-agent on Artificial_Intelligence:")
        print("  python .agent/skills/vault-organizer-agent/scripts/organize.py --folder Artificial_Intelligence scan")
    else:
        print(f"\n[DRY RUN DONE] Would move {moved} files. Run without --dry-run to apply.")


if __name__ == "__main__":
    main()

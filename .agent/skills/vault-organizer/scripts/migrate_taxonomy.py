#!/usr/bin/env python3
"""One-time migration: flatten 3_RESOURCES/Artificial Intelligent/ → 3_RESOURCES/.

Moves every sub-folder and file from the redundant ``Artificial Intelligent/``
nesting layer up one level into ``3_RESOURCES/``, optionally merging into
existing folders and never overwriting existing files.

Usage
-----
    # Preview what would happen (safe, default):
    python migrate_taxonomy.py --vault-root D:/Personlich/RemoteObsidian

    # Actually perform the migration:
    python migrate_taxonomy.py --vault-root D:/Personlich/RemoteObsidian --execute

Note
----
This script does **not** repair Obsidian wikilinks.  Link fixup is handled
separately by ``link_repair.py`` after migration.
"""

from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
AI_SUBFOLDER = "Artificial_Intelligence"
RESOURCES_DIR = "3_RESOURCES"
NESTED_DIR = "Artificial Intelligent"

# The old segment that appears in summerized_contents.json path keys.
OLD_PATH_SEGMENT = f"{RESOURCES_DIR}/{NESTED_DIR}/"
# After migration, paths should just use RESOURCES_DIR directly.
NEW_PATH_SEGMENT = f"{RESOURCES_DIR}/"

# Candidate locations for summerized_contents.json (relative to vault root).
CONTEXT_JSON_CANDIDATES: list[str] = [
    f"{AI_SUBFOLDER}/.obsidian/summerized_contents.json",
    f"Dream/.obsidian/summerized_contents.json",
    f"Project_Skin/.obsidian/summerized_contents.json",
    f".obsidian/summerized_contents.json",
]

logger = logging.getLogger("migrate_taxonomy")


# ---------------------------------------------------------------------------
# Vault root detection
# ---------------------------------------------------------------------------
def detect_vault_root(start: Path | None = None) -> Path | None:
    """Walk upward from *start* looking for a ``.obsidian/`` directory.

    Parameters
    ----------
    start:
        Directory to begin searching from.  Defaults to this script's parent.

    Returns
    -------
    Path | None
        The first ancestor directory containing ``.obsidian/``, or ``None``.
    """
    if start is None:
        start = Path(__file__).resolve().parent

    current = start.resolve()
    for _ in range(20):  # safety cap to avoid infinite loop
        if (current / ".obsidian").is_dir():
            return current
        parent = current.parent
        if parent == current:
            break
        current = parent
    return None


# ---------------------------------------------------------------------------
# File / directory move helpers
# ---------------------------------------------------------------------------
def _move_file(src: Path, dst: Path, *, execute: bool) -> bool:
    """Move a single file from *src* to *dst*.

    Returns ``True`` if the file was (or would be) moved, ``False`` if skipped
    due to a collision.
    """
    if dst.exists():
        logger.warning("SKIP (collision): %s → %s  (destination already exists)", src, dst)
        return False

    if execute:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(src), str(dst))
        logger.info("MOVED: %s → %s", src, dst)
    else:
        logger.info("WOULD MOVE: %s → %s", src, dst)
    return True


def _merge_directory(src_dir: Path, dst_dir: Path, *, execute: bool) -> tuple[int, int]:
    """Recursively merge *src_dir* into *dst_dir*.

    Parameters
    ----------
    src_dir:
        Source directory whose contents should be migrated.
    dst_dir:
        Destination directory that may already exist and contain items.
    execute:
        If ``False``, only log what would happen.

    Returns
    -------
    tuple[int, int]
        (moved_count, skipped_count).
    """
    moved = 0
    skipped = 0

    for item in sorted(src_dir.iterdir()):
        target = dst_dir / item.name

        if item.is_dir():
            # Recurse into sub-directory, merging if target already exists.
            sub_moved, sub_skipped = _merge_directory(item, target, execute=execute)
            moved += sub_moved
            skipped += sub_skipped
        else:
            if _move_file(item, target, execute=execute):
                moved += 1
            else:
                skipped += 1

    return moved, skipped


def _remove_empty_tree(directory: Path, *, execute: bool) -> None:
    """Remove *directory* and any empty parents up to (but not including) 3_RESOURCES.

    Only removes directories that are genuinely empty after the migration.
    """
    if not directory.exists():
        return

    # Walk bottom-up: remove empty children first.
    for child in sorted(directory.iterdir()):
        if child.is_dir():
            _remove_empty_tree(child, execute=execute)

    # Now try to remove the directory itself if empty.
    try:
        remaining = list(directory.iterdir())
    except OSError:
        return

    if not remaining:
        if execute:
            directory.rmdir()
            logger.info("REMOVED empty directory: %s", directory)
        else:
            logger.info("WOULD REMOVE empty directory: %s", directory)


# ---------------------------------------------------------------------------
# summerized_contents.json updater
# ---------------------------------------------------------------------------
def _find_context_json(vault_root: Path) -> Path | None:
    """Return the first existing ``summerized_contents.json`` candidate path."""
    for candidate in CONTEXT_JSON_CANDIDATES:
        path = vault_root / candidate
        if path.is_file():
            return path
    return None


def _update_context_json(json_path: Path, *, execute: bool) -> int:
    """Rewrite path keys in *json_path* to remove the old nesting segment.

    Returns the number of keys that were (or would be) updated.
    """
    try:
        raw = json_path.read_text(encoding="utf-8").strip()
    except OSError as exc:
        logger.error("Cannot read %s: %s", json_path, exc)
        return 0

    if not raw:
        logger.info("Context JSON is empty; nothing to update.")
        return 0

    try:
        data: dict[str, Any] = json.loads(raw)
    except json.JSONDecodeError as exc:
        logger.error("Invalid JSON in %s: %s", json_path, exc)
        return 0

    updated_count = 0

    # --- Update "summarized_files" list ---
    if "summarized_files" in data and isinstance(data["summarized_files"], list):
        new_list: list[str] = []
        for entry in data["summarized_files"]:
            if isinstance(entry, str) and OLD_PATH_SEGMENT in entry:
                new_entry = entry.replace(OLD_PATH_SEGMENT, NEW_PATH_SEGMENT, 1)
                logger.info("REKEY (list): %s → %s", entry, new_entry)
                new_list.append(new_entry)
                updated_count += 1
            else:
                new_list.append(entry)
        data["summarized_files"] = new_list

    # --- Update "details" dict keys and category values ---
    if "details" in data and isinstance(data["details"], dict):
        new_details: dict[str, Any] = {}
        for key, value in data["details"].items():
            new_key = key
            if OLD_PATH_SEGMENT in key:
                new_key = key.replace(OLD_PATH_SEGMENT, NEW_PATH_SEGMENT, 1)
                logger.info("REKEY (details): %s → %s", key, new_key)
                updated_count += 1

            # Also fix the "category" field inside each detail entry.
            if isinstance(value, dict) and "category" in value:
                old_cat = value["category"]
                if isinstance(old_cat, str) and OLD_PATH_SEGMENT in old_cat:
                    value["category"] = old_cat.replace(
                        OLD_PATH_SEGMENT, NEW_PATH_SEGMENT, 1
                    )
                    logger.info("REKEY (category): %s → %s", old_cat, value["category"])

            new_details[new_key] = value
        data["details"] = new_details

    if updated_count == 0:
        logger.info("No path keys in context JSON needed updating.")
        return 0

    if execute:
        # Write atomically via a temp file in the same directory.
        tmp_path = json_path.with_suffix(".json.tmp")
        try:
            tmp_path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            tmp_path.replace(json_path)
            logger.info("Updated %d path key(s) in %s", updated_count, json_path)
        except OSError as exc:
            logger.error("Failed to write updated JSON: %s", exc)
            if tmp_path.exists():
                tmp_path.unlink(missing_ok=True)
    else:
        logger.info("WOULD UPDATE %d path key(s) in %s", updated_count, json_path)

    return updated_count


# ---------------------------------------------------------------------------
# Main migration logic
# ---------------------------------------------------------------------------
def migrate(vault_root: Path, *, execute: bool) -> None:
    """Run the full migration.

    Parameters
    ----------
    vault_root:
        Absolute path to the Obsidian vault root (contains ``.obsidian/``).
    execute:
        If ``True``, actually move files and update JSON.  Otherwise dry-run.
    """
    mode = "EXECUTE" if execute else "DRY-RUN"
    logger.info("=" * 60)
    logger.info("migrate_taxonomy  [%s]  %s", mode, datetime.now(timezone.utc).isoformat())
    logger.info("Vault root: %s", vault_root)
    logger.info("=" * 60)

    nested_dir = vault_root / AI_SUBFOLDER / RESOURCES_DIR / NESTED_DIR
    resources_dir = vault_root / AI_SUBFOLDER / RESOURCES_DIR

    # ------------------------------------------------------------------
    # Step 1: Check if migration is needed
    # ------------------------------------------------------------------
    if not nested_dir.is_dir():
        logger.info("Already migrated — '%s' does not exist.", nested_dir)
        print("Already migrated")
        return

    # ------------------------------------------------------------------
    # Step 2: Move / merge all contents up one level
    # ------------------------------------------------------------------
    logger.info("Source: %s", nested_dir)
    logger.info("Destination parent: %s", resources_dir)

    total_moved = 0
    total_skipped = 0

    for item in sorted(nested_dir.iterdir()):
        target = resources_dir / item.name

        if item.is_dir():
            if target.is_dir():
                logger.info("MERGE directory: %s → %s", item.name, target)
                m, s = _merge_directory(item, target, execute=execute)
            else:
                # Target doesn't exist; move the whole directory.
                if execute:
                    shutil.move(str(item), str(target))
                    logger.info("MOVED directory: %s → %s", item, target)
                else:
                    logger.info("WOULD MOVE directory: %s → %s", item, target)
                # Count all files inside the moved directory.
                m = sum(1 for _ in item.rglob("*") if _.is_file())
                s = 0
        else:
            # Top-level file directly inside "Artificial Intelligent/".
            ok = _move_file(item, target, execute=execute)
            m = 1 if ok else 0
            s = 0 if ok else 1

        total_moved += m
        total_skipped += s

    # ------------------------------------------------------------------
    # Step 3: Remove the now-empty nested directory tree
    # ------------------------------------------------------------------
    _remove_empty_tree(nested_dir, execute=execute)

    # ------------------------------------------------------------------
    # Step 4: Update summerized_contents.json
    # ------------------------------------------------------------------
    json_path = _find_context_json(vault_root)
    keys_updated = 0
    if json_path is not None:
        logger.info("Found context JSON: %s", json_path)
        keys_updated = _update_context_json(json_path, execute=execute)
    else:
        logger.info("No summerized_contents.json found; skipping JSON update.")

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    logger.info("-" * 60)
    logger.info("Migration summary  [%s]", mode)
    logger.info("  Files moved:   %d", total_moved)
    logger.info("  Files skipped: %d", total_skipped)
    logger.info("  JSON keys updated: %d", keys_updated)
    logger.info("-" * 60)

    if not execute:
        logger.info(
            "This was a dry-run.  Re-run with --execute to apply changes."
        )


# ---------------------------------------------------------------------------
# CLI entry-point
# ---------------------------------------------------------------------------
def _build_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        description=(
            "One-time migration: flatten "
            "3_RESOURCES/Artificial Intelligent/* → 3_RESOURCES/*"
        ),
    )
    parser.add_argument(
        "--vault-root",
        type=Path,
        default=None,
        help=(
            "Absolute path to the Obsidian vault root.  "
            "If omitted, auto-detects by walking up from the script location."
        ),
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="(default) Log what would happen without making changes.",
    )
    group.add_argument(
        "--execute",
        action="store_true",
        help="Actually perform the migration.",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable DEBUG-level logging.",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    """CLI entry-point."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    # Logging setup
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Resolve vault root
    vault_root: Path | None = args.vault_root
    if vault_root is None:
        vault_root = detect_vault_root()
        if vault_root is None:
            logger.error(
                "Could not auto-detect vault root (no .obsidian/ found). "
                "Specify --vault-root explicitly."
            )
            sys.exit(1)
    else:
        vault_root = vault_root.resolve()
        if not (vault_root / ".obsidian").is_dir():
            logger.error(
                "Vault root '%s' does not contain a .obsidian/ directory.",
                vault_root,
            )
            sys.exit(1)

    execute = args.execute
    migrate(vault_root, execute=execute)


if __name__ == "__main__":
    main()

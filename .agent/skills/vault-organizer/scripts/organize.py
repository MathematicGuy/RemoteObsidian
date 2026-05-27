"""
organize.py — Main pipeline for the Obsidian Vault Auto-Organizer.

Subcommands:
    scan     — Discover unorganized files, apply heuristic rules, output JSON
    plan     — Accept AI classifications JSON, generate move_plan.md
    execute  — Read move_plan.md, move files, repair links, update index, git commit
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

# Ensure UTF-8 encoding is used for standard output/error, especially on Windows
if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Ensure the scripts/ directory is on sys.path so sibling imports work
# regardless of the working directory from which the agent invokes us.
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from heuristic_rules import match_heuristic, get_existing_categories

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
AI_FOLDER = "Artificial_Intelligence"
PARA_FOLDERS = {"1_PROJECTS", "2_ACTIONS", "3_RESOURCES", "4_ARCHIVES"}
SKIP_DIRS = {
    ".obsidian", ".makemd", ".space", ".trash",
    "excalidraw", "image", "images", "ultilities", "utilities", "_unsorted",
}
SKIP_EXTENSIONS = {".excalidraw.md"}
PLAN_JSON = "_move_plan.json"
PLAN_MD = "move_plan.md"


# ═══════════════════════════════════════════════════════════════════════════
# Utility helpers
# ═══════════════════════════════════════════════════════════════════════════

def find_vault_root() -> Path:
    """Walk upward from this script to locate the vault root (contains .obsidian/)."""
    current = SCRIPT_DIR
    for _ in range(10):
        if (current / ".obsidian").is_dir():
            return current
        # Check if parent contains the vault
        parent = current.parent
        if parent == current:
            break
        current = parent
    # Fallback: assume vault is 4 levels up from scripts/
    fallback = SCRIPT_DIR.parent.parent.parent.parent
    if (fallback / ".obsidian").is_dir():
        return fallback
    raise FileNotFoundError(
        f"Could not find vault root (.obsidian/) walking up from {SCRIPT_DIR}"
    )


def find_ai_root(vault_root: Path) -> Path:
    """Return the Artificial_Intelligence directory inside the vault."""
    ai_root = vault_root / AI_FOLDER
    if not ai_root.is_dir():
        raise FileNotFoundError(f"AI folder not found: {ai_root}")
    return ai_root


def git_commit(vault_root: Path, message: str) -> bool:
    """Stage all changes and commit. Returns True if a commit was made."""
    try:
        subprocess.run(
            ["git", "add", "-A"],
            cwd=str(vault_root), check=True,
            capture_output=True, text=True,
        )
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=str(vault_root), capture_output=True, text=True,
        )
        if not result.stdout.strip():
            print("[GIT] Nothing to commit — working tree clean.")
            return False

        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=str(vault_root), check=True,
            capture_output=True, text=True,
        )
        print(f"[GIT] Committed: {message}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[GIT WARNING] Git operation failed: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("[GIT WARNING] Git not found on PATH — skipping commit.", file=sys.stderr)
        return False


def read_content_preview(filepath: Path, max_chars: int = 2000) -> str:
    """Read the first max_chars characters of a file."""
    try:
        with open(filepath, "r", encoding="utf-8", errors="replace") as f:
            return f.read(max_chars)
    except Exception as e:
        print(f"[WARNING] Could not read {filepath}: {e}", file=sys.stderr)
        return ""


# ═══════════════════════════════════════════════════════════════════════════
# SCAN — Discover unorganized files and apply heuristic rules
# ═══════════════════════════════════════════════════════════════════════════

def cmd_scan(args: argparse.Namespace) -> None:
    """Scan vault root for unorganized files, classify with heuristics."""
    vault_root = find_vault_root()
    ai_root = find_ai_root(vault_root)

    print(f"[SCAN] Vault root : {vault_root}", file=sys.stderr)
    print(f"[SCAN] AI folder  : {ai_root}", file=sys.stderr)

    # --- Collect unorganized files at AI root level ---
    unorganized: list[dict[str, Any]] = []

    for item in sorted(ai_root.iterdir()):
        if item.is_dir():
            continue
        if item.name.startswith("."):
            continue

        # Only .md and .canvas files
        suffix = item.suffix.lower()
        if suffix not in (".md", ".canvas"):
            continue

        # Skip .excalidraw.md
        if item.name.lower().endswith(".excalidraw.md"):
            continue

        # Skip special files
        if item.name.lower() in ("readme.md",):
            continue

        rel_path = str(item.relative_to(vault_root)).replace("\\", "/")
        unorganized.append({
            "filename": item.name,
            "relative_path": rel_path,
            "absolute_path": str(item),
            "size_bytes": item.stat().st_size,
        })

    print(f"[SCAN] Found {len(unorganized)} unorganized files.", file=sys.stderr)

    # --- Apply heuristic classification ---
    heuristic_matched: list[dict[str, Any]] = []
    needs_ai: list[dict[str, Any]] = []

    for entry in unorganized:
        # Try filename-only match first
        category = match_heuristic(entry["filename"])

        if category is None:
            # Try with content preview
            content = read_content_preview(Path(entry["absolute_path"]))
            category = match_heuristic(entry["filename"], content)

        if category:
            entry["category"] = category
            entry["method"] = "heuristic"
            entry["confidence"] = "high"
            heuristic_matched.append(entry)
        else:
            # Prepare for AI classification
            content = read_content_preview(Path(entry["absolute_path"]))
            entry["content_preview"] = content
            needs_ai.append(entry)

    print(
        f"[SCAN] Heuristic matched: {len(heuristic_matched)} | Needs AI: {len(needs_ai)}",
        file=sys.stderr,
    )

    # --- Output JSON to stdout ---
    output = {
        "vault_root": str(vault_root),
        "ai_root": str(ai_root),
        "scan_timestamp": datetime.now(timezone.utc).isoformat(),
        "total_unorganized": len(unorganized),
        "heuristic_matched": heuristic_matched,
        "needs_ai": needs_ai,
        "existing_categories": get_existing_categories(),
    }

    print(json.dumps(output, indent=2, ensure_ascii=False))


# ═══════════════════════════════════════════════════════════════════════════
# PLAN — Generate move_plan.md from heuristic + AI classifications
# ═══════════════════════════════════════════════════════════════════════════

def cmd_plan(args: argparse.Namespace) -> None:
    """Read classifications JSON (stdin or file), generate move_plan.md."""
    # Read classifications from file or stdin
    if args.input_file:
        with open(args.input_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    vault_root = Path(data.get("vault_root", str(find_vault_root())))
    ai_root = find_ai_root(vault_root)

    # Merge heuristic_matched + ai_classified into a single move list
    moves: list[dict[str, Any]] = []

    for entry in data.get("heuristic_matched", []):
        moves.append({
            "filename": entry["filename"],
            "source": entry["relative_path"],
            "destination": f"{AI_FOLDER}/{entry['category']}/{entry['filename']}",
            "method": "heuristic",
            "confidence": entry.get("confidence", "high"),
        })

    for entry in data.get("ai_classified", []):
        category = entry.get("category", "_unsorted")
        confidence = entry.get("confidence", "low")
        if confidence == "low":
            category = "_unsorted"
        moves.append({
            "filename": entry["filename"],
            "source": entry["relative_path"],
            "destination": f"{AI_FOLDER}/{category}/{entry['filename']}",
            "method": "ai",
            "confidence": confidence,
        })

    # --- Check for collisions ---
    for move in moves:
        dest_path = vault_root / move["destination"]
        move["collision"] = dest_path.exists()

    # --- Write machine-readable plan ---
    plan_json_path = ai_root / PLAN_JSON
    plan_data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "vault_root": str(vault_root),
        "total_moves": len(moves),
        "moves": moves,
    }
    with open(plan_json_path, "w", encoding="utf-8") as f:
        json.dump(plan_data, f, indent=2, ensure_ascii=False)

    # --- Write human-readable plan ---
    plan_md_path = ai_root / PLAN_MD
    stats = {
        "heuristic": sum(1 for m in moves if m["method"] == "heuristic"),
        "ai_high": sum(1 for m in moves if m["method"] == "ai" and m["confidence"] == "high"),
        "ai_medium": sum(1 for m in moves if m["method"] == "ai" and m["confidence"] == "medium"),
        "unsorted": sum(1 for m in moves if "_unsorted" in m["destination"]),
        "collisions": sum(1 for m in moves if m["collision"]),
    }

    lines = [
        "# 📦 Vault Organizer — Move Plan",
        "",
        f"> Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Summary",
        "",
        f"| Metric | Count |",
        f"|--------|-------|",
        f"| Total files | {len(moves)} |",
        f"| Heuristic matched | {stats['heuristic']} |",
        f"| AI classified (high confidence) | {stats['ai_high']} |",
        f"| AI classified (medium confidence) | {stats['ai_medium']} |",
        f"| Sent to _unsorted/ | {stats['unsorted']} |",
        f"| Collisions (will skip) | {stats['collisions']} |",
        "",
        "## Move Plan",
        "",
        "| # | File | Destination | Method | Confidence | Collision |",
        "|---|------|-------------|--------|------------|-----------|",
    ]

    for i, move in enumerate(sorted(moves, key=lambda m: m["filename"]), 1):
        collision_flag = "⚠️ YES" if move["collision"] else ""
        lines.append(
            f"| {i} | {move['filename']} | `{move['destination']}` "
            f"| {move['method']} | {move['confidence']} | {collision_flag} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "> **Review this plan.** When ready, tell the agent to `execute` the move plan.",
        "",
    ])

    with open(plan_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[PLAN] Written: {plan_md_path}", file=sys.stderr)
    print(f"[PLAN] Written: {plan_json_path}", file=sys.stderr)
    print(f"[PLAN] {len(moves)} moves planned.", file=sys.stderr)

    # Also output the plan JSON to stdout for the agent
    print(json.dumps(plan_data, indent=2, ensure_ascii=False))


# ═══════════════════════════════════════════════════════════════════════════
# EXECUTE — Move files, repair links, update index, git commit
# ═══════════════════════════════════════════════════════════════════════════

def cmd_execute(args: argparse.Namespace) -> None:
    """Execute the move plan: move files, repair links, update index."""
    vault_root = find_vault_root()
    ai_root = find_ai_root(vault_root)
    plan_json_path = ai_root / PLAN_JSON

    if not plan_json_path.exists():
        print(f"[ERROR] No move plan found at {plan_json_path}", file=sys.stderr)
        print("Run 'scan' and 'plan' first.", file=sys.stderr)
        sys.exit(1)

    with open(plan_json_path, "r", encoding="utf-8") as f:
        plan_data = json.load(f)

    moves = plan_data.get("moves", [])
    if not moves:
        print("[EXECUTE] No moves to execute.", file=sys.stderr)
        return

    # --- Phase 0: Pre-flight git commit ---
    print("[EXECUTE] Phase 0: Git snapshot...", file=sys.stderr)
    git_commit(vault_root, "vault-organizer: pre-organize snapshot")

    # --- Phase 5: Move files ---
    print(f"[EXECUTE] Phase 5: Moving {len(moves)} files...", file=sys.stderr)
    moved_files: dict[str, str] = {}  # old_rel_path -> new_rel_path
    moved_count = 0
    skipped_count = 0

    for move in moves:
        src = vault_root / move["source"]
        dst = vault_root / move["destination"]

        if not src.exists():
            print(f"  [SKIP] Source missing: {move['source']}", file=sys.stderr)
            skipped_count += 1
            continue

        if dst.exists():
            print(f"  [SKIP] Collision: {move['destination']}", file=sys.stderr)
            skipped_count += 1
            continue

        # Create target directory
        dst.parent.mkdir(parents=True, exist_ok=True)

        try:
            shutil.move(str(src), str(dst))
            moved_files[move["source"]] = move["destination"]
            moved_count += 1
            print(f"  [MOVED] {move['filename']} -> {move['destination']}", file=sys.stderr)
        except Exception as e:
            print(f"  [ERROR] {move['filename']}: {e}", file=sys.stderr)
            skipped_count += 1

    print(
        f"[EXECUTE] Moved: {moved_count} | Skipped: {skipped_count}",
        file=sys.stderr,
    )

    # --- Phase 6: Wikilink repair ---
    if moved_files:
        print("[EXECUTE] Phase 6: Repairing wikilinks...", file=sys.stderr)
        try:
            from link_repair import repair_links_for_moves
            changes = repair_links_for_moves(str(vault_root), moved_files)
            print(
                f"[EXECUTE] Repaired {len(changes)} link references.",
                file=sys.stderr,
            )
        except ImportError:
            print(
                "[WARNING] link_repair module not found — skipping link repair.",
                file=sys.stderr,
            )
        except Exception as e:
            print(f"[WARNING] Link repair failed: {e}", file=sys.stderr)

    # --- Phase 7: Update summerized_contents.json ---
    print("[EXECUTE] Phase 7: Updating index...", file=sys.stderr)
    update_index(vault_root, moved_files)

    # --- Phase 8: Post-flight ---
    # Clean up plan files
    for cleanup_file in (plan_json_path, ai_root / PLAN_MD):
        if cleanup_file.exists():
            cleanup_file.unlink()

    # Git commit result
    commit_msg = (
        f"vault-organizer: organized {moved_count} files "
        f"({sum(1 for m in moves if m['method'] == 'heuristic')} heuristic, "
        f"{sum(1 for m in moves if m['method'] == 'ai')} AI, "
        f"{skipped_count} skipped)"
    )
    git_commit(vault_root, commit_msg)

    # --- Summary output ---
    summary = {
        "moved": moved_count,
        "skipped": skipped_count,
        "links_repaired": len(changes) if moved_files else 0,
        "moved_files": moved_files,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))


def update_index(vault_root: Path, moved_files: dict[str, str]) -> None:
    """Update summerized_contents.json with new file paths."""
    # Try both possible index locations, prioritizing the specific vault folder
    index_candidates = [
        vault_root / AI_FOLDER / ".obsidian" / "summerized_contents.json",
        vault_root / ".obsidian" / "summerized_contents.json",
    ]

    index_path = None
    index_data: dict[str, Any] = {"summarized_files": [], "details": {}}

    for candidate in index_candidates:
        if candidate.exists():
            index_path = candidate
            try:
                with open(candidate, "r", encoding="utf-8") as f:
                    index_data = json.load(f)
            except Exception:
                pass
            break

    if index_path is None:
        # Use the vault-level .obsidian as default
        index_path = index_candidates[0]

    # Update paths for moved files
    old_summarized = index_data.get("summarized_files", [])
    new_summarized = []
    new_details = {}

    for old_path in old_summarized:
        if old_path in moved_files:
            new_path = moved_files[old_path]
            new_summarized.append(new_path)
            if old_path in index_data.get("details", {}):
                new_details[new_path] = index_data["details"][old_path]
                new_details[new_path]["category"] = str(
                    Path(new_path).parent
                ).replace("\\", "/")
        else:
            new_summarized.append(old_path)
            if old_path in index_data.get("details", {}):
                new_details[old_path] = index_data["details"][old_path]

    index_data["summarized_files"] = new_summarized
    index_data["details"] = new_details

    # Write back
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    print(f"[INDEX] Updated: {index_path}", file=sys.stderr)


# ═══════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Obsidian Vault Auto-Organizer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # --- scan ---
    sub.add_parser("scan", help="Discover unorganized files and apply heuristic rules")

    # --- plan ---
    plan_parser = sub.add_parser("plan", help="Generate move_plan.md from classifications")
    plan_parser.add_argument(
        "--input-file", "-i",
        help="Path to classifications JSON (default: read from stdin)",
    )

    # --- execute ---
    sub.add_parser("execute", help="Execute the move plan")

    args = parser.parse_args()

    if args.command == "scan":
        cmd_scan(args)
    elif args.command == "plan":
        cmd_plan(args)
    elif args.command == "execute":
        cmd_execute(args)


if __name__ == "__main__":
    main()

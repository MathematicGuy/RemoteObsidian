"""Wikilink repair module for an Obsidian vault auto-organizer.

Parses ``[[FileName]]`` / ``[[FileName|Alias]]`` wikilinks in Markdown
content, and bulk-repairs broken links across an entire vault after files
have been moved or renamed.

Key design decisions
--------------------
* **Obsidian shortest-path resolution** – ``[[FileName]]`` resolves to any
  file named ``FileName.md`` anywhere in the vault.  A *move* that does not
  change the filename therefore does **not** break plain wikilinks.  Only
  *renames* or *path-based* links (``[[folder/FileName]]``) need repair.
* **Case-insensitive matching** – Obsidian treats wikilink targets as
  case-insensitive; this module follows suit when deciding whether a link
  needs updating.
* **Atomic writes** – every file mutation is written to a temporary file
  first, then atomically renamed over the original to prevent corruption.
* **Code-block awareness** – links inside fenced code blocks (``````` …
  ```````) are never modified.
* **.canvas support** – Obsidian canvas files store references as
  ``"file": "path/to/note.md"`` in JSON; this module rewrites those too.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Regex helpers
# ---------------------------------------------------------------------------

# Matches a fenced code block (``` or ~~~), including the optional language tag.
_CODE_FENCE_RE = re.compile(r"^[ \t]*(```+|~~~+)", re.MULTILINE)

# Matches a wikilink, optionally preceded by `!` (embed).
# Groups:  1 = optional `!`
#          2 = inner content (everything between [[ and ]])
_WIKILINK_RE = re.compile(r"(!?)\[\[([^\]]+?)\]\]")


# ---------------------------------------------------------------------------
# Public helpers
# ---------------------------------------------------------------------------

def find_wikilinks(content: str) -> list[dict]:
    """Extract all wikilinks from markdown *content*, skipping code blocks.

    Returns a list of dicts, each with:

    * ``raw``      – the full matched text, e.g. ``[[Foo#Bar|Baz]]`` or
                     ``![[Image.png]]``
    * ``target``   – the link target without header/alias, e.g. ``Foo``
    * ``alias``    – the display-text alias, or ``None``
    * ``header``   – the ``#Header`` fragment, or ``None`` (without the ``#``)
    * ``has_path`` – ``True`` when the target contains a ``/``
    * ``is_embed`` – ``True`` when the link is prefixed with ``!``

    Parameters
    ----------
    content:
        Raw markdown string (may contain code blocks, YAML front-matter, etc.).
    """
    code_ranges = _code_block_ranges(content)
    results: list[dict] = []

    for m in _WIKILINK_RE.finditer(content):
        start, end = m.span()
        if _inside_any_range(start, end, code_ranges):
            continue

        embed_prefix: str = m.group(1)  # '' or '!'
        inner: str = m.group(2)         # everything between [[ and ]]

        target, header, alias = _parse_inner(inner)

        results.append({
            "raw": m.group(0),
            "target": target,
            "alias": alias if alias else None,
            "header": header if header else None,
            "has_path": "/" in target,
            "is_embed": embed_prefix == "!",
        })

    return results


def repair_links_for_moves(
    vault_root: str,
    moves: dict[str, str],
) -> list[dict]:
    """Scan every ``.md`` / ``.canvas`` file in the vault and repair wikilinks
    broken by the given *moves*.

    Parameters
    ----------
    vault_root:
        Absolute path to the Obsidian vault root
        (e.g. ``"d:/Personlich/RemoteObsidian"``).
    moves:
        Mapping of **old** relative paths → **new** relative paths, using
        forward slashes.  Example::

            {
                "AI/LoRA.md": "AI/3_RESOURCES/Deep Learning/LoRA.md",
                "Notes/old_name.md": "Notes/new_name.md",
            }

    Returns
    -------
    list[dict]
        A log of every individual link rewrite performed::

            [{"file": "relative/path.md",
              "old_link": "[[old]]",
              "new_link": "[[new]]"}, …]
    """
    root = Path(vault_root).resolve()
    rename_map, path_map = _build_repair_maps(moves)
    change_log: list[dict] = []

    for fpath in _iter_vault_files(root):
        rel = fpath.relative_to(root).as_posix()
        # Skip files that are themselves being moved — the caller is
        # responsible for writing them to their new locations.
        if rel in {v for v in moves.values()}:
            continue

        suffix = fpath.suffix.lower()
        if suffix == ".md":
            changes = _repair_markdown_file(fpath, root, rename_map, path_map)
        elif suffix == ".canvas":
            changes = _repair_canvas_file(fpath, root, path_map)
        else:
            continue

        for c in changes:
            c["file"] = rel
        change_log.extend(changes)

    return change_log


# ---------------------------------------------------------------------------
# Internal: parsing helpers
# ---------------------------------------------------------------------------

def _parse_inner(inner: str) -> tuple[str, str, str]:
    """Split the inner part of a wikilink into (target, header, alias).

    Examples
    --------
    >>> _parse_inner("Foo")
    ('Foo', '', '')
    >>> _parse_inner("Foo#Bar")
    ('Foo', 'Bar', '')
    >>> _parse_inner("Foo#Bar|Baz")
    ('Foo', 'Bar', 'Baz')
    >>> _parse_inner("Foo|Baz")
    ('Foo', '', 'Baz')
    """
    alias = ""
    header = ""

    # Alias is everything after the *last* unescaped `|`.
    if "|" in inner:
        target_and_header, alias = inner.rsplit("|", 1)
    else:
        target_and_header = inner

    # Header is everything after the *first* `#`.
    if "#" in target_and_header:
        target, header = target_and_header.split("#", 1)
    else:
        target = target_and_header

    return target.strip(), header.strip(), alias.strip()


def _code_block_ranges(content: str) -> list[tuple[int, int]]:
    """Return a sorted list of ``(start, end)`` character-offset ranges
    that fall inside fenced code blocks.
    """
    ranges: list[tuple[int, int]] = []
    fence_stack: Optional[tuple[str, int]] = None  # (fence_char, start_offset)

    for m in _CODE_FENCE_RE.finditer(content):
        fence = m.group(1)
        fence_char = fence[0]  # '`' or '~'
        fence_len = len(fence)

        if fence_stack is None:
            # Opening fence
            fence_stack = (fence_char * fence_len, m.start())
        else:
            # Closing fence must use the same character and be at least as long.
            open_fence = fence_stack[0]
            if fence_char == open_fence[0] and fence_len >= len(open_fence):
                ranges.append((fence_stack[1], m.end()))
                fence_stack = None

    # If there's an unclosed fence, treat the rest of the file as code.
    if fence_stack is not None:
        ranges.append((fence_stack[1], len(content)))

    return ranges


def _inside_any_range(
    start: int,
    end: int,
    ranges: list[tuple[int, int]],
) -> bool:
    """Return ``True`` if the span ``[start, end)`` falls entirely inside
    any of the given *ranges*.
    """
    for rng_start, rng_end in ranges:
        if start >= rng_start and end <= rng_end:
            return True
    return False


# ---------------------------------------------------------------------------
# Internal: repair-map construction
# ---------------------------------------------------------------------------

def _stem(path: str) -> str:
    """Return the filename without extension (case-folded)."""
    return Path(path).stem.lower()


def _build_repair_maps(
    moves: dict[str, str],
) -> tuple[dict[str, str], dict[str, str]]:
    """Derive two lookup structures from the raw *moves* dict.

    Returns
    -------
    rename_map
        ``{old_stem_lower: new_stem}`` — only populated when the filename
        (stem) actually *changed*.  Used for short (non-path) wikilinks.
    path_map
        ``{old_relative_path_lower: new_relative_path}`` — always populated.
        Used for path-based wikilinks and canvas ``"file"`` references.
    """
    rename_map: dict[str, str] = {}
    path_map: dict[str, str] = {}

    for old_path, new_path in moves.items():
        # Normalise separators
        old_norm = old_path.replace("\\", "/")
        new_norm = new_path.replace("\\", "/")

        path_map[old_norm.lower()] = new_norm

        old_stem = Path(old_norm).stem
        new_stem = Path(new_norm).stem

        if old_stem.lower() != new_stem.lower():
            rename_map[old_stem.lower()] = new_stem

    return rename_map, path_map


# ---------------------------------------------------------------------------
# Internal: vault iteration
# ---------------------------------------------------------------------------

def _iter_vault_files(root: Path):
    """Yield every ``.md`` and ``.canvas`` ``Path`` under *root*, skipping
    hidden directories (names starting with ``.``) and common ignore dirs.
    """
    ignore_dirs = {".git", ".obsidian", ".trash", ".agent", "node_modules"}
    for dirpath, dirnames, filenames in os.walk(root):
        # Prune hidden / ignored directories in-place so os.walk skips them.
        dirnames[:] = [
            d for d in dirnames
            if d not in ignore_dirs and not d.startswith(".")
        ]
        for fname in filenames:
            low = fname.lower()
            if low.endswith(".md") or low.endswith(".canvas"):
                yield Path(dirpath) / fname


# ---------------------------------------------------------------------------
# Internal: markdown repair
# ---------------------------------------------------------------------------

def _repair_markdown_file(
    fpath: Path,
    root: Path,
    rename_map: dict[str, str],
    path_map: dict[str, str],
) -> list[dict]:
    """Rewrite wikilinks inside a single ``.md`` file.

    Returns a list of ``{"old_link": …, "new_link": …}`` dicts (the caller
    adds ``"file"``).
    """
    try:
        content = fpath.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []

    code_ranges = _code_block_ranges(content)
    changes: list[dict] = []
    new_content_parts: list[str] = []
    last_end = 0

    for m in _WIKILINK_RE.finditer(content):
        start, end = m.span()
        if _inside_any_range(start, end, code_ranges):
            continue

        embed_prefix: str = m.group(1)
        inner: str = m.group(2)
        target, header, alias = _parse_inner(inner)

        new_target: Optional[str] = _resolve_new_target(
            target, rename_map, path_map,
        )

        if new_target is None:
            continue  # link is fine — no change needed

        new_inner = _rebuild_inner(new_target, header, alias)
        new_link = f"{embed_prefix}[[{new_inner}]]"

        changes.append({"old_link": m.group(0), "new_link": new_link})

        new_content_parts.append(content[last_end:start])
        new_content_parts.append(new_link)
        last_end = end

    if not changes:
        return []

    new_content_parts.append(content[last_end:])
    new_content = "".join(new_content_parts)
    _atomic_write(fpath, new_content)
    return changes


def _resolve_new_target(
    target: str,
    rename_map: dict[str, str],
    path_map: dict[str, str],
) -> Optional[str]:
    """Decide what the *target* part of a wikilink should become.

    Returns ``None`` if no change is needed.
    """
    has_path = "/" in target

    if has_path:
        # Path-based link — try to match against path_map.
        # The target might omit the extension; try both with and without `.md`.
        target_norm = target.replace("\\", "/")
        candidates = [target_norm, target_norm + ".md"]
        for cand in candidates:
            new_path = path_map.get(cand.lower())
            if new_path is not None:
                # Strip the `.md` extension if the original didn't have one.
                if not target_norm.lower().endswith(".md") and new_path.lower().endswith(".md"):
                    new_path = new_path[:-3]
                return new_path

        # Also check if just the last component (stem) was renamed.  This
        # handles links like ``folder/OldName`` when OldName → NewName.
        target_stem = Path(target_norm).stem.lower()
        if target_stem in rename_map:
            new_stem = rename_map[target_stem]
            parent = str(Path(target_norm).parent)
            ext = Path(target_norm).suffix
            if parent and parent != ".":
                return f"{parent}/{new_stem}{ext}"
            return f"{new_stem}{ext}"
    else:
        # Short (non-path) link — only needs repair if the file was *renamed*.
        target_stem = Path(target).stem.lower()
        if target_stem in rename_map:
            new_stem = rename_map[target_stem]
            ext = Path(target).suffix
            return f"{new_stem}{ext}"

    return None


def _rebuild_inner(target: str, header: str, alias: str) -> str:
    """Reconstruct the inner text of a wikilink."""
    parts = [target]
    if header:
        parts.append(f"#{header}")
    result = "".join(parts)
    if alias:
        result = f"{result}|{alias}"
    return result


# ---------------------------------------------------------------------------
# Internal: canvas repair
# ---------------------------------------------------------------------------

def _repair_canvas_file(
    fpath: Path,
    root: Path,
    path_map: dict[str, str],
) -> list[dict]:
    """Rewrite ``"file"`` references inside a ``.canvas`` JSON file.

    Canvas nodes look like::

        {"type": "file", "file": "relative/path/to/Note.md", …}

    Returns a list of ``{"old_link": …, "new_link": …}`` dicts.
    """
    try:
        raw = fpath.read_text(encoding="utf-8")
        data = json.loads(raw)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return []

    changes: list[dict] = []
    modified = False

    # Canvas JSON has a top-level "nodes" array.
    nodes = data.get("nodes", [])
    for node in nodes:
        file_ref: Optional[str] = node.get("file")
        if not file_ref:
            continue

        norm = file_ref.replace("\\", "/").lower()
        new_path = path_map.get(norm)

        if new_path is not None and new_path.lower() != norm:
            changes.append({
                "old_link": f'"file": "{file_ref}"',
                "new_link": f'"file": "{new_path}"',
            })
            node["file"] = new_path
            modified = True

    # Also check "edges" for possible "file" references (rare but safe).
    edges = data.get("edges", [])
    for edge in edges:
        file_ref = edge.get("file")
        if not file_ref:
            continue
        norm = file_ref.replace("\\", "/").lower()
        new_path = path_map.get(norm)
        if new_path is not None and new_path.lower() != norm:
            changes.append({
                "old_link": f'"file": "{file_ref}"',
                "new_link": f'"file": "{new_path}"',
            })
            edge["file"] = new_path
            modified = True

    if modified:
        new_raw = json.dumps(data, ensure_ascii=False, indent=2)
        _atomic_write(fpath, new_raw)

    return changes


# ---------------------------------------------------------------------------
# Internal: atomic write
# ---------------------------------------------------------------------------

def _atomic_write(fpath: Path, content: str) -> None:
    """Write *content* to *fpath* atomically.

    A temporary file is created in the same directory, written, flushed,
    and then renamed over the target.  On Windows ``os.replace`` is used
    which is atomic when source and destination are on the same volume.
    """
    parent = fpath.parent
    fd, tmp_path = tempfile.mkstemp(
        dir=str(parent),
        prefix=f".{fpath.name}.",
        suffix=".tmp",
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(content)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp_path, str(fpath))
    except BaseException:
        # Clean up the temp file on any failure.
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise

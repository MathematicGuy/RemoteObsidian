# ADR 0001: Storage/Cache Hybrid Metadata Split

## Status
Approved (Active)

## Context
Obsidian is a file-system-first knowledge management system. When executing vault organization pipelines, we need to extract, store, and retrieve metadata (file summaries, tags, categories) to enable intelligent AI-driven queries and semantic indexing.

We evaluated two opposing storage patterns:
1.  **Centralized JSON Database**: Store all metadata inside a single global index.
    *   *Pro*: Millisecond query speed, zero risk of note corruption, clean git diffs.
    *   *Con*: High sync decay (manual note edits break the index), zero file portability.
2.  **Inline YAML Frontmatter**: Store metadata inside each individual note's YAML block.
    *   *Pro*: 100% portable notes (metadata moves with the file), zero sync decay.
    *   *Con*: High I/O parse times for future database queries (must read every file on disk), higher blast radius (risk of note corruption during subagent writes).

We also had to choose between subagents writing files concurrently (high token cost, high risk) or the Master Agent writing them in a single validated local transaction (zero token cost, zero risk).

## Decision
We choose the **Storage/Cache Hybrid Metadata Split Pattern**:

1.  **Storage (YAML SSoT)**: Inline YAML frontmatter is the Single Source of Truth for all note metadata. This ensures note portability across vaults and zero sync drift.
2.  **Caching (Centralized Index)**: A centralized `.obsidian/summerized-context.json` acts as a compiled, read-only cache. During the execution phase, a fast Python script parses the YAML frontmatter of modified notes and compiles the central index. All future search/query tools read strictly from this central cache.
3.  **Master-Only Execution**: Spawned subagents are strictly read-only JSON generators. They do not have access to file write tools. The primary Master Agent runs the post-merge validation and performs all file writes and movements locally, saving massive API token costs and preventing file-lock hazards.

## Consequences
*   **Token Savings**: Saves $\approx 110,000+$ API tokens per scan/execute cycle by removing subagent file-writing tool overhead.
*   **Security & Safety**: Drastically limits the write blast radius. Subagents cannot corrupt notes. Git staging remains clean until the final local execute script runs.
*   **Portability**: Notes remain fully self-contained. Sharing notes with other vaults preserves all summaries and tags.
*   **High Performance**: Search tools and DB migrations read the compiled index cache in milliseconds, bypassing expensive multi-file disk I/O.

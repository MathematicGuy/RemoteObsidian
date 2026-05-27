---
name: vault-organizer
description: >
  Auto-organize loose markdown and canvas files in the Obsidian vault.
  Two-phase pipeline: heuristic keyword matching (fast) then AI content-based
  classification (smart).  Moves files, repairs wikilinks, updates the
  semantic index, and commits via Git for safe rollback.
---

# Vault Auto-Organizer Skill

Organize unorganized `.md` and `.canvas` files sitting at the root of
`Artificial_Intelligence/` into the correct PARA sub-folders
(`1_PROJECTS`, `2_ACTIONS`, `3_RESOURCES/<Topic>`, `4_ARCHIVES`).

**Scripts location:** `.agent/skills/vault-organizer/scripts/`

---

## Quick Reference

| Script | Purpose |
|--------|---------|
| `organize.py scan`    | Find loose files + apply heuristic keyword rules |
| `organize.py plan`    | Generate `move_plan.md` from combined classifications |
| `organize.py execute` | Move files, repair links, update index, git commit |
| `migrate_taxonomy.py` | One-time: flatten `3_RESOURCES/Artificial Intelligent/` |

---

## Pre-Requisite: Taxonomy Migration (One-Time)

Before the first organize run, check whether the old nested taxonomy still
exists.  If `Artificial_Intelligence/3_RESOURCES/Artificial Intelligent/`
is present, run the migration first:

```bash
python .agent/skills/vault-organizer/scripts/migrate_taxonomy.py --execute
```

This flattens `3_RESOURCES/Artificial Intelligent/<Topic>/` →
`3_RESOURCES/<Topic>/`.  After migration, run link repair via the
organize pipeline to fix any broken wikilinks.

---

## Execution Workflow

### Step 1 — Scan & Heuristic Classification

Run the scan command from the vault root:

```bash
python .agent/skills/vault-organizer/scripts/organize.py scan
```

This outputs a JSON object to **stdout** with two arrays:

- `heuristic_matched` — files already classified by keyword rules
  (each has `category`, `method: "heuristic"`, `confidence: "high"`)
- `needs_ai` — files the heuristics couldn't classify
  (each has `content_preview` with the first ~2000 chars)

**Save the output** to a temporary JSON file or capture it for Step 2.

### Step 2 — AI Classification

For each file in the `needs_ai` array, you must dynamically classify and summarize it. Follow the **Sub-Skill Citation** protocol:

1.  **Ingest Persona**: Load the contents of [**`SUB-SKILLS.md`**](file:///D:/Personlich/RemoteObsidian/.agent/skills/vault-organizer/SUB-SKILLS.md) to serve as the subagent's base system prompt.
2.  **Determine Dynamic Topic Focus**: Analyze the batch file composition and dynamically interpolate the `[DYNAMIC_TOPIC_FOCUS]` parameter inside the subagent prompt:
    *   Inject Code-specific instructions for code notes.
    *   Inject Math-specific instructions for math notes.
    *   Inject General conceptual mapping for other topics.
3.  **Partition & Spawn**:
    *   If `needs_ai` is under 15 files, process in-context.
    *   If 15 or more files, slice into batches of 15–25 files. Spawn a **maximum of 4 concurrent subagents** in **`Workspace: inherit`** mode.
4.  **JSON Collection**: Subagents must return a clean, unescaped JSON array. Collect and merge the JSON blocks.

**Output format for classifications:** The subagents return the data containing the dynamic 2-sentence summary:
```json
{
  "filename": "LoRA.md",
  "relative_path": "Artificial_Intelligence/LoRA.md",
  "category": "3_RESOURCES/Deep Learning",
  "summary": "Explains Low-Rank Adaptation (LoRA) for parameter-efficient fine-tuning of large models. Details linear rank factorization of weight updates.",
  "method": "ai",
  "confidence": "high"
}
```


### Step 3 — Generate Move Plan

Pipe the merged JSON (containing both `heuristic_matched` and
`ai_classified`) into the plan command:

```bash
python .agent/skills/vault-organizer/scripts/organize.py plan -i <merged_classifications.json>
```

This generates two files in `Artificial_Intelligence/`:
- `move_plan.md`  — Human-readable table for review
- `_move_plan.json` — Machine-readable plan for execution

### Step 4 — Present Plan to User

Tell the user:

> "I've generated a move plan for **N files**. Please review
> `Artificial_Intelligence/move_plan.md` and tell me to **execute**
> when you're ready."

**Do NOT proceed until the user explicitly says to execute.**

### Step 5 — Execute

Run:

```bash
python .agent/skills/vault-organizer/scripts/organize.py execute
```

This performs a local local transaction executing the **Storage/Cache Hybrid Split**:
1.  **Git pre-flight snapshot**: Commits all active files.
2.  **YAML SSoT Writing**: Writes double-quoted properly escaped YAML blocks to the head of each note file containing:
    ```yaml
    ---
    category: "3_RESOURCES/NLP RAG"
    summary: "Strict 2-sentence maximum. Specific concrete nouns only."
    keywords: ["rag", "llm", "context"]
    confidence: "high"
    analyzed_at: "2026-05-27T16:02:00Z"
    ---
    ```
3.  **File Move**: Moves note files cleanly to their PARA directories.
4.  **Wikilink Repair**: Updates all internal links and alias hooks using standard short paths.
5.  **Index Compilation (Query Cache)**: Parses note frontmatters and compiles `Obsidian-Vault-Name/.obsidian/summerized_contents.json` as a read-only fast cache.
6.  **Clean up**: Deletes temporary JSON plans.
7.  **Git post-flight commit**: Commits final organized vault.

Report the summary to the user.


---

## Folder Taxonomy Rules

- **`3_RESOURCES/`** is the only place where the AI may create new
  sub-folders dynamically.
- Sub-folders should be named with Title Case and describe a broad
  technical domain (e.g., `Reinforcement Learning`, not
  `Q-Learning Algorithms`).
- Never create more than one level of nesting under `3_RESOURCES/`.
  Correct: `3_RESOURCES/MLOps/`.  Wrong: `3_RESOURCES/MLOps/CI-CD/`.

---

## Wikilink Repair

The `execute` command automatically calls `link_repair.py` which:
- Scans ALL `.md` and `.canvas` files in the entire `RemoteObsidian/` vault
- Updates `[[FileName]]`, `[[FileName|Alias]]`, `[[FileName#Section]]`,
  and `![[FileName]]` patterns
- Only modifies links where the target filename matches a moved file
- Uses Obsidian's shortest-path resolution: if a file was moved but not
  renamed, most `[[FileName]]` links still work.  Repair focuses on
  path-qualified links like `[[folder/FileName]]`.

---

## Index Schema

The organizer maintains `Obsidian-Vault-Name/.obsidian/summerized_contents.json`:

```json
{
  "summarized_files": ["Artificial_Intelligence/3_RESOURCES/Deep Learning/LoRA.md"],
  "details": {
    "Artificial_Intelligence/3_RESOURCES/Deep Learning/LoRA.md": {
      "category": "Artificial_Intelligence/3_RESOURCES/Deep Learning",
      "summary": "Explains Low-Rank Adaptation for efficient LLM fine-tuning.",
      "keywords": ["lora", "fine-tuning", "llm"],
      "links": ["Deep Learning", "Transformer"],
      "analyzed_at": "2026-05-25T00:00:00Z"
    }
  }
}
```

---

## Safety

- **Git safety net:** Two commits bracket every organize run.
  To undo: `git revert HEAD` (undoes moves), or `git revert HEAD~1`
  (restores pre-organize state).
- **Collision protection:** Files are never overwritten.  If the
  destination already exists, the move is skipped and logged.
- **Scope guard:** Only files at the `Artificial_Intelligence/` root
  level are touched.  Files already inside `1_PROJECTS/`, `2_ACTIONS/`,
  `3_RESOURCES/`, or `4_ARCHIVES/` are never moved.

---

## AI & Subagent Orchestration Protocol

To scale file classification across large vaults, the primary IDE Agent must orchestrate a tier of parallel subagents. Follow these rules:

### Concurrency & Batch Rules
1. **Dynamic Partitioning**:
   - If the `needs_ai` list contains **fewer than 15 files**, process them directly within the primary agent's context.
   - If the list contains **15 or more files**, partition the list into concurrent batches of **15 to 25 files** each.
2. **Concurrency Cap**:
   - Spawn a **maximum of 4 parallel subagents** concurrently using the `invoke_subagent` tool.
   - If there are more than 100 files, process them in sequential waves of 4 concurrent subagents.

### Spawning Configuration
- **Tool Call**: `invoke_subagent`
- **Workspace Mode**: **`inherit`** (Mandatory on Windows platforms to bypass file-length limits and Git worktree failures).
- **Role**: `Vault Classifier Subagent`
- **System Prompt Citation (Ingestion Invariant)**: 
  You **must not** use a hardcoded prompt. Instead, read the contents of [**`SUB-SKILLS.md`**](file:///D:/Personlich/RemoteObsidian/.agent/skills/vault-organizer/SUB-SKILLS.md) at the beginning of Step 2, and use it as the base prompt for the subagents, interpolating the dynamic slots at spawn time.

### Auto-adaptive Ingestion Protocol
Before spawning each subagent, analyze the composition of its assigned batch (file extensions, filename keywords) and dynamically interpolate the `[DYNAMIC_TOPIC_FOCUS]` slot inside the prompt:
- **Code Batches** (e.g., >50% files are `.py` or have code keywords): Inject:
  `"Focus strictly on programming language syntax, libraries used, object-oriented class structures, and algorithm complexity."`
- **Mathematics / Physics Batches** (e.g., files have LaTeX formulas, statistics, equations): Inject:
  `"Focus strictly on mathematical definitions, equations, probability event spaces, variable definitions, and statistical theorems."`
- **General Technical Batches** (default): Inject:
  `"Focus strictly on the core conceptual thesis, systems relationships, and actionable deliverables."`

Attach the batch's file JSON array to the `<assigned_files_json_array>` placeholder and invoke the subagent.

## Master Validation & Path Sanitization Gate

Before feeding the merged classifications into `organize.py plan`, the primary IDE Agent **must** act as the Central Validation Gate (SSoT validation). Run the following checks on the merged JSON:

1. **Path Safety Regex Gate**:
   Ensure all category strings contain only safe alphanumeric characters, spaces, and hyphens.
   - **Reject** any category containing special characters, backslashes (outside path separators), or non-ASCII characters that might trigger system encoding failures (e.g. `Xét Tập Xác định` should be classified cleanly without path corruption).
   - If a proposed category fails this check, automatically sanitize it (e.g. replace special characters with spaces/dashes) or route the file to `_unsorted/`.
2. **Category Depth Limit Check**:
   Confirm that no category path has more than one level of nesting under `3_RESOURCES/`.
   - Correct: `3_RESOURCES/Data Science`
   - Incorrect: `3_RESOURCES/Data Science/Deep Learning` (Automatically flatten to `3_RESOURCES/Deep Learning`).
3. **Collision Auditing**:
   If a proposed file path conflicts with an existing file of the same name in the target directory, mark the collision status in the JSON to let `organize.py` safely skip it and report it to the user.
4. **Low Confidence Fallback**:
   Any file classified with `confidence: "low"` must have its category rewritten to `_unsorted/`.



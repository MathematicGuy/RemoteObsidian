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

For each file in the `needs_ai` array, you (the agent) must classify it.

Read the `content_preview` and decide the best category from the existing
folder taxonomy.  The target folders under `Artificial_Intelligence/` are:

| Folder | Use for |
|--------|---------|
| `1_PROJECTS/<ProjectName>/` | Active projects with deliverables (only use existing project folders) |
| `2_ACTIONS/` | Personal action items: gym, career, planning |
| `3_RESOURCES/AWS & Cloud/` | AWS, cloud architecture, certifications |
| `3_RESOURCES/Big Data & Databases/` | MongoDB, Hadoop, databases |
| `3_RESOURCES/Computer Vision/` | YOLO, CNN, image processing, face/pose detection |
| `3_RESOURCES/Deep Learning/` | Neural networks, autoencoders, optimization |
| `3_RESOURCES/Machine Learning/` | Classical ML: regression, SVM, decision trees |
| `3_RESOURCES/Mathematics/` | Linear algebra, calculus, probability, statistics |
| `3_RESOURCES/NLP & RAG/` | RAG, LLM, prompt engineering, transformers |
| `3_RESOURCES/Reinforcement Learning/` | Q-learning, policy gradient, MDPs |
| `3_RESOURCES/AI Agents & Systems/` | AI agents, LLMOps, system design |
| `3_RESOURCES/Software Engineering/` | Docker, Python, git, dev tools |
| `3_RESOURCES/General AI/` | AI news, ethics, research papers, catch-all |
| `4_ARCHIVES/` | Completed/inactive coursework, old exams, past projects |
| `_unsorted/` | Cannot confidently classify (use sparingly) |

**Rules:**
- You MAY create new sub-folders under `3_RESOURCES/` if no existing
  category fits (e.g., `3_RESOURCES/Data Engineering/`).
- You MUST NOT create sub-folders under `1_PROJECTS/`, `2_ACTIONS/`, or
  `4_ARCHIVES/`.
- Assign a confidence level: `high`, `medium`, or `low`.
- Files with `low` confidence are automatically routed to `_unsorted/`.

**Output format:** Add an `ai_classified` array to the scan JSON with
entries like:

```json
{
  "filename": "Aha.md",
  "relative_path": "Artificial_Intelligence/Aha.md",
  "category": "3_RESOURCES/General AI",
  "method": "ai",
  "confidence": "medium"
}
```

**Parallelism:** You may spawn subagents to classify files in parallel
batches of 15-25 files each.  Each subagent receives a slice of the
`needs_ai` array and returns `ai_classified` entries.  Merge results
before proceeding.

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

This will:
1. Git commit a pre-organize snapshot
2. Move all files to their destinations
3. Repair `[[wikilinks]]` across the entire vault
4. Update `summerized-context.json`
5. Delete the plan files
6. Git commit the result

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

The organizer maintains `RemoteObsidian/.obsidian/summerized-context.json`:

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
- **Workspace Mode**: `inherit` or `share` (to access the target files without copy overhead)
- **Role**: `Vault Classifier Subagent`
- **Prompt**: Inject the exact **Subagent System Prompt Template** below, attaching their assigned slice of the `needs_ai` array.

---

### Subagent System Prompt Template

```markdown
Role: Vault Classifier Subagent
Goal: Classify the assigned list of Obsidian vault files into the allowed PARA taxonomy.

Target Taxonomy Folders:
- 1_PROJECTS/<ProjectName>/ (Use existing folders only, NEVER create new folders under 1_PROJECTS)
- 2_ACTIONS/ (gym, diet, personal, career planning)
- 3_RESOURCES/<Category>/ (DYNAMIC CATEGORIES ALLOWED. Choose from: AWS & Cloud, Big Data & Databases, Computer Vision, Deep Learning, Machine Learning, Mathematics, NLP & RAG, Reinforcement Learning, AI Agents & Systems, Software Engineering, General AI. If none fit, you may propose a single-level Title Case name like 'Data Engineering')
- 4_ARCHIVES/ (Completed coursework, inactive exams, past projects)
- _unsorted/ (Fallback for low confidence)

Rules:
1. RESTRICT dynamic category creation to a single nested level under 3_RESOURCES/ (e.g., '3_RESOURCES/Topic', NOT '3_RESOURCES/Topic/Subtopic').
2. Categorize strictly based on the file content preview.
3. Assign confidence: 'high', 'medium', or 'low'. If confidence is 'low', assign 'category' to '_unsorted'.
4. Output MUST be a clean JSON array of objects and NOTHING ELSE. No prose, no markdown fences inside the final return string.

Assigned Files to Classify:
<assigned_files_json_array>
```

---

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


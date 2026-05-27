# Vault Organizer Topology & Features

This file tracks the architecture, components, and feature specifications for the fully autonomous **Vault-Organizer-Agent** skill.

---

## Core Vision
A fully autonomous vault-organizing agent equipped with parallel subagent parsing, auto-adaptive topic modeling, hybrid metadata caching, and Git sandbox boundaries for absolute safety.

---

## 1. Git Sandbox Boundary (Option A: Auto-Stash & Sandbox)
To ensure absolute safety during large-scale automated file refactoring and YAML frontmatter injection.

- **Dirty working tree gate**: If the workspace contains uncommitted changes, they are stashed using `git stash -u` (including untracked files).
- **Sandbox Branch**: Creates and checks out a dedicated temporary sandbox branch (e.g., `vault-organize/sandbox-YYYY-MM-DD`).
- **Interactive Review**:
  - The agent executes file migrations and YAML modifications on the sandbox branch.
  - The user reviews the changes live in their local Obsidian vault (Obsidian refreshes files dynamically as the git branch changes).
- **Approval Decision**:
  - **APPROVED**: Merges sandbox branch back to original branch, deletes sandbox branch, and pops stash (`git stash pop`) to restore active development changes.
  - **REJECTED**: Aborts changes, checks out original branch, deletes sandbox branch, and pops stash (`git stash pop`) to restore the original state with zero data loss.

---

## 2. Autonomous Agent & Subagent Orchestration
Efficient token usage and high taxonomic precision through decoupled worker layers.

- **Master Agent (Sovereign Executor)**:
  - Manages execution flow, processes CLI parameters, runs directory walks.
  - Controls Git state (branching, stashing, committing).
  - Performs all file mutations locally (Single Source of Truth).
- **Subagent Personas (Worker Classifiers)**:
  - Lightweight, stateless subagents spawned with `Workspace: inherit`.
  - Driven by the minimized [`SUB-SKILLS.md`](file:///D:/Personlich/RemoteObsidian/.agent/skills/vault-organizer/SUB-SKILLS.md) constitution.
  - pure read-only; they do not write files or invoke git.

---

## 3. Dynamic Topic Selection & Ingestion
Prevents generic "one-size-fits-all" categorization.

- **Active Master Ingestion**: The Master Agent reads `SUB-SKILLS.md` and injects it directly into the subagent prompt at spawn time, saving subagent filesystem token costs.
- **Dynamic Topic Slot**: The Master populates a dynamic `[DYNAMIC_TOPIC_FOCUS]` template block based on batch composition. For instance:
  - *Code Files*: Focus on functions, frameworks, architecture.
  - *Math/Physics Files*: Focus on theorems, equations, axioms.
  - *Literature/Philosophy*: Focus on concepts, themes, authors.

---

## 4. Storage/Cache Hybrid Metadata Split
Ensures absolute file-level portability combined with high-speed query indexing.

- **Inline Storage (SSoT)**: All metadata (summaries, categories) is written directly inside note YAML frontmatter, escaping quotes to prevent parse errors.
- **Centralized Cache**: Compiled into a single JSON index `summerized-context.json` within the `.obsidian/` folder during execution to allow high-speed search and retrieval.

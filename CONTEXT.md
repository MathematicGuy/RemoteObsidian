# Remote Obsidian Vault Organizer

This context manages the transaction-safe, autonomous organization of files in an Obsidian Vault, incorporating sandboxed execution, adaptive heuristics, and AI-driven categorization.

## Language

**Sub-Vault (Vault Folder)**:
A top-level directory inside the main Obsidian vault that represents a distinct domain (e.g. `Artificial_Intelligence`, `Literature`) and is targeted for organization.
_Avoid_: Folder, database, project root

**Adaptive Heuristics**:
Context-aware, localized rules loaded dynamically from a JSON file in the target Sub-Vault to match and route filenames to target categories before running AI analysis.
_Avoid_: Hardcoded rules, static keyword mappings

**Vault Rules Configuration (`.vault-rules.json`)**:
A local configuration file stored at the root of a Sub-Vault that defines the mapping of categories to filename keyword patterns for adaptive heuristics.
_Avoid_: Central config, hardcoded mappings

**SSoT Validation Gate**:
The master verification logic that ensures proposed categories adhere to strict path constraints, sanitizes character sets, restricts nested resource folders to single-depth, and routes low-confidence moves to `_unsorted/`.
_Avoid_: Direct planning, unchecked moves

**Git Sandbox Boundary**:
An execution safety wrapper that automatically stashes uncommitted drafts and runs all mutations on a temporary sandbox branch, giving the user a live risk-free preview in Obsidian before approval.
_Avoid_: Direct branch commits, non-sandboxed moves

## Example Dialogue

**Developer**: "I want to organize a new folder of notes I made on quantum physics, how do I configure it?"
**Domain Expert**: "Since that is a new **Sub-Vault**, you can run `scan` and it will automatically generate a default **Vault Rules Configuration** file named `.vault-rules.json` in the root of your quantum physics folder. You can edit this file to add **Adaptive Heuristics** mappings for things like `schrodinger` or `wavefunction` to route to `3_RESOURCES/Quantum Mechanics`."
**Developer**: "Great. What if a note filename doesn't match any heuristic keywords?"
**Domain Expert**: "The **Adaptive Heuristics** process is strictly filename-only. If it fails to match, the file content is delegated to the AI subagents for semantic categorization. Once done, the paths go through the **SSoT Validation Gate** to ensure no deep nesting occurs, and everything executes safely inside a **Git Sandbox Boundary**."

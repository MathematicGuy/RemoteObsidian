# Git Sandbox & Selective Merge Guide 🛡️

This guide explains the secure sandboxing and selective branch checkout techniques used by the **Vault Organizer Agent** to safely develop, test, and upgrade skills while protecting your active vault notes.

---

## 💡 The Core Technique: Path-Based Checkout

When developing features inside an autonomous agent, you often want to test modifications (e.g., organizing files in vaults `Dream` or `Project_Skin`) without permanently committing the resulting file movements. However, you *do* want to keep the upgrades made to the tools, scripts, and documentation.

In Git, you can perform a **Selective Merge** (also known as a path-specific checkout) using:

```bash
git checkout <source-branch> -- <path1> <path2> ...
```

### Why this works:
* **Decouples State from Branch**: Instead of merging the entire commit history of the sandbox branch (which would merge all file moves), this command reads the specified directories/files from the sandbox branch and overlays them directly onto your current working tree.
* **Transaction Safe**: It brings in only the directories you specify (like `.agent/skills/` and `Artificial_Intelligence/`), leaving all other directories (like `Dream/` and `Project_Skin/`) completely untouched and in their original states.
* **No Git History Pollution**: It avoids bringing in the sandbox's merge commit history or parent logs, giving you a clean, unified commit on your main branch.

---

## 🔄 Step-by-Step Workflow Walkthrough

Here is the exact step-by-step transaction executed during our session:

### Step 1: Pre-flight & Sandbox Isolation
We checked out a temporary branch to isolate the organization mutations:
```bash
# Switched to a dedicated sandbox branch
git checkout -b vault-organize/sandbox-test
```

### Step 2: Autonomous Mutative Testing
We ran the auto-organizer pipeline on both vaults:
```bash
python .agent/skills/vault-organizer-agent/scripts/organize.py scan
python .agent/skills/vault-organizer-agent/scripts/organize.py plan
python .agent/skills/vault-organizer-agent/scripts/organize.py execute
```
*Result:* Both `Dream` and `Project_Skin` vaults were successfully organized, metadata was updated, links repaired, and snapshots committed on the sandbox branch.

### Step 3: Switch back to Main
When you decided you only wanted to merge the core tool upgrades and documentation (and discard the physical file moves in `Dream` and `Project_Skin`), we returned to the original branch:
```bash
git checkout main
```

### Step 4: Perform the Selective Merge
We extracted only the upgraded skills and documentation from the sandbox:
```bash
git checkout vault-organize/sandbox-test -- .agent/skills/ Artificial_Intelligence/
```
*Result:* This instantly staged the upgraded Python scripts, skill files, and the `Vault-Organizer-Topology.md` modifications on `main`, while leaving the physical `Dream/` and `Project_Skin/` folders completely untouched!

### Step 5: Commit and Cleanup
Finally, we committed the clean updates and discarded the sandbox branch:
```bash
# Committed the upgraded tools and documentation
git commit -m "upgrade organizer agent skills and update topology documentation"

# Discarded the sandbox branch, safely deleting the organized vaults from history
git branch -D vault-organize/sandbox-test
```

---

## 🛠️ Command Cheat Sheet

| Command | Action |
|---------|--------|
| `git checkout -b <name>` | Create and switch to a new sandbox branch |
| `git checkout <branch> -- <paths>` | Selectively checkout specific folders/files from another branch |
| `git status` | Check which files are staged for commit |
| `git commit -m "message"` | Commit staged changes |
| `git branch -D <name>` | Force-delete an unwanted branch (fully discarding its unique changes) |

---

> [!TIP]
> **When to use this:**
> Always use this sandboxing technique when testing agent behaviors that mutate files, perform automated data restructurings, or refactor folders. It gives you an absolute safety net to test mutations live, inspect them, and discard them while still keeping any enhancements made to the agent's code itself!

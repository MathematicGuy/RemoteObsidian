# TOPOLOGY.md - Codebase Reasoning Topology

> [!NOTE]
> **SYSTEM STRUCTURAL MAP**
> This file describes the active geometry, component relationships, state ownership, and boundaries of the `HACollab: Human-Agent Collaboration` system. Update it as new directories, scripts, or components are added.

---

## 1. Directory Structure

```
Artificial_Intelligence/1_PROJECTS/Agents-Orchestration/Human-Agent-Collaboration-Framework/
├── TOPOLOGY.md             # This File (Active architectural map)
├── human_overview.md       # Read-Only Anchor (Human Intent & Goals)
├── agent_overview.md       # Read-Write Recommended Plan (Agent's response plan)
│
├── mindseeds/              # Epistemic Compression Seeds Folder
│   ├── mindseeds.md        # Master seed schema and family listing
│   ├── archseeds.md        # System Architecture / Structural integrity invariants
│   ├── cogniseeds.md       # Reasoning / Decision-making epistemic constraints
│   └── linguaseeds.md      # Voice authenticity / Linguistic friction rules
│
│
└── AGENT_Framework_For_Semantically_Grounded_Pattern_Matching/  [GIT SUBMODULE]
    ├── AGENTS.md           # The Constitution (System-wide rules, version gates)
    ├── AGENT.md            # Behavioral Layer (Active persona, verification protocol)
    ├── BRAIN.md            # Knowledge Memory Layer (Metaphorical wisdom & patterns)
    ├── HEART.md            # Beating Semantic Center (Core project attractor/Strange Loop)
    ├── TERRITORY.md        # Active Actionable Protocols (Contextual Gatekeeper plan)
    ├── AUTO-AGENT.md       # Single-prompt Application Builder logic
    ├── CODE-RECON.md       # Codebase Reconnaissance Analyst protocol
    ├── EXECUTION-MOMENTUM.md # Velocity constraints & subagent guidelines
    └── TOOLS.md            # Core five tools usage contract definition

```

---

## 2. State & Intent Ownership

```
┌────────────────────────────────┐
│      human_overview.md         │ ◄── [Human Intent Anchor] (Read-Only)
└───────────────┬────────────────┘
                │ (Feedback / Calibration)
                ▼
┌────────────────────────────────┐
│      agent_overview.md         │ ◄── [Planning & Roadmap] (Joint Writable)
└───────────────┬────────────────┘
                │ (Decompresses ArchSeeds / Guides Action)
                ▼
┌────────────────────────────────┐
│      Noosphere Steward/        │ ◄── [Execution & Memory Engine]
│  (AGENT.md, BRAIN.md, etc.)    │     (Local / Submodule Overrides)
└────────────────────────────────┘
```

*   **Human Intent State:** Owned by `human_overview.md`. Read-only for the agent to prevent rewriting core human goals.
*   **Active Planning & Alignment State:** Owned by `agent_overview.md`. Writable by both, defining current active checklists and verified topologies.
*   **Local Behavioral Memory:** Owned by the local `AGENT.md` and `BRAIN.md` which adjust dynamically based on current project observations.
*   **Shared Epistemic Invariants:** Owned by the global `mindseeds/` folder contents (`archseeds.md`, etc.), acting as a shared vocabulary between human and agent.


---

## 3. High-Risk Seams & Boundaries

*   **The Read-Only Fence:** Files like `human_overview.md` and the central `Noosphere Steward` core framework are strictly read-only for active agents unless explicitly overridden by the human. This guards against systemic configuration/settings drift.
*   **Friction Boundary (Verification Gates):** Velocity is deliberately slowed down before code writes. The agent must verify state ownership, feedback/observability, and blast radius before shipping any modifications.
*   **Friction Loop (Dialogue Alignment):** Ambiguity maps to questions. If intent is conceptual, the agent is restricted to single-question interaction blocks to narrow down the design tree before taking action.

---

## 4. Teammate Synchronization Workflow

To ensure seamless portability of the `HACollab` system across our team and project repositories, we employ a **Hybrid Git Submodule Architecture**:

```
                       [Central Framework Repository]
                                      │
              ┌───────────────────────┴───────────────────────┐
              ▼ (Git Submodule Pull)                          ▼ (Git Submodule Pull)
    [Project A Repository]                          [Project B Repository]
    ├── Noosphere Steward/ [Core Submodule]         ├── Noosphere Steward/ [Core Submodule]
    ├── local_AGENT.md (Tracked locally)            ├── local_AGENT.md (Tracked locally)
    └── local_BRAIN.md (Tracked locally)            └── local_BRAIN.md (Tracked locally)
```

### 🚀 Setup Checklist for Teammates

1.  **Clone the Repository with Submodules:**
    When checking out a project repository containing this framework, initialize and update the `Noosphere Steward` submodule:
    ```powershell
    git clone --recurse-submodules <project-repo-url>
    # OR if already cloned:
    git submodule update --init --recursive
    ```
2.  **Tracking Local Memory:**
    - The core files inside `Noosphere Steward` (such as `AGENTS.md`, `HEART.md`, `TERRITORY.md`) pull directly from the centralized engine repo.
    - Local project configurations and learning arrays should be committed directly to the main project repository under `AGENT.md` and `BRAIN.md` at the project's root.
3.  **Propagating Global Metaphors:**
    - When a local project produces a highly generalizable lesson or new "MindSeed," append it to your local `mindseeds.md`.
    - Periodically, a team member can merge new seeds from local projects back into the upstream central `MindSeeds` repository to update the global vocabulary across all active projects.

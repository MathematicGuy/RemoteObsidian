# CONTEXT.md — HACollab System Glossary

This file serves as the Single Source of Truth (SSoT) glossary for our domain models, terms, and conceptual boundaries. It is strictly conceptual and devoid of low-level implementation details.

---

## Glossary

| Term | Domain Context | Definition |
| :--- | :--- | :--- |
| **Subagent Persona** | Orchestration | A highly compressed, lightweight cognitive constraint layer designed to guide worker agents without system-wide meta-framework overhead. |
| **Active Master Ingestion** | Ingestion | The direct injection of a subagent's rules and schemas by the primary orchestrator at spawn time, eliminating the need for subagents to execute file-reading tools. |
| **Central Ingestion Invariant** | Ingestion | The requirement that all worker constraints must be read and injected by the orchestrator at spawn time, preventing file-reading race conditions. |
| **Dynamic Topic Slot** | Orchestration | A configurable parameter inside the subagent persona system prompt that the Master Agent populates at runtime to adapt summarization styles to specific domains (e.g., Code, Literature, Physics). |
| **Inline Metadata (YAML)** | Storage | Structured key-value properties written directly inside the head of individual markdown files to ensure absolute portability of summaries. |
| **Centralized Index Cache** | Caching | A compiled, high-speed query file (e.g. `summerized-contents.json`) representing the aggregated metadata of all vault files, used to prevent expensive disk I/O. |
| **Sub-Skill Citation** | Orchestration | The architectural practice of referencing and dynamically loading a dedicated worker skills file (e.g. `SUB-SKILLS.md`) at runtime, preventing hardcoded prompt duplication and state drift. |

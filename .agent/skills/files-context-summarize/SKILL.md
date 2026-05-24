---
name: files-context-summarize
description: >
  Specialized skill to incrementally analyze, summarize, and categorize markdown
  and canvas vault files. Maintains a unified metadata tracking index inside
  the .obsidian/ directory as summerized-context.json.
---

This skill guides a subagent to read, analyze, and build a high-performance semantic index of all notes inside the `Artificial_Intelligence` vault. It uses an incremental approach to process new or updated files while recording status in a structured JSON index to keep vault organization clean, fast, and completely portable.

---

## Output Target Location & Format

You MUST read and write to this exact path:
`Artificial_Intelligence/.obsidian/summerized-context.json`

To support name clashes, easy SQLite migration, and Vector DB (ChromaDB) RAG matching, the index utilizes the note's **relative path from the vault root** (e.g., `3_RESOURCES/Artificial Intelligent/Note_A.md`) as the unique key.

Follow this schema exactly:

```json
{
  "summarized_files": [
    "3_RESOURCES/Artificial Intelligent/Machine Learning/Note_A.md",
    "3_RESOURCES/Artificial Intelligent/Mathematics/Note_B.md"
  ],
  "details": {
    "3_RESOURCES/Artificial Intelligent/Machine Learning/Note_A.md": {
      "category": "3_RESOURCES/Artificial Intelligent/Machine Learning",
      "summary": "1-2 sentence executive summary of the note contents.",
      "keywords": ["keyword1", "keyword2"],
      "links": ["Linked_Note_1", "Linked_Note_2"],
      "analyzed_at": "ISO-8601-Timestamp"
    },
    "3_RESOURCES/Artificial Intelligent/Mathematics/Note_B.md": {
      "category": "3_RESOURCES/Artificial Intelligent/Mathematics",
      "summary": "1-2 sentence executive summary of the note contents.",
      "keywords": ["keyword1", "keyword2"],
      "links": ["Linked_Note_3"],
      "analyzed_at": "ISO-8601-Timestamp"
    }
  }
}
```

---

## Execution Workflow

### Step 1: Scan and Identify Targets
1. Locate all unsummarized files. You MUST run the `check_unsummerize.py` utility inside `.agent/skills/files-context-summarize/`.
2. This utility:
   - Restricts scanning strictly to the whitelisted directories: `1_PROJECTS`, `2_ACTIONS`, and `3_RESOURCES`.
   - Bypasses default Obsidian paths (`.obsidian`, `.makemd`, `.space`, `.trash`), administrative files (`.smart-env`), and asset/utility folders (`Excalidraw`, `images`, `ultilities`).
   - Automatically skips and prunes any subdirectories recursively containing a blank `.ignore` or `_ignore` marker file.
   - **Self-Heals Moved Files:** Automatically updates the relative path keys in `summerized-context.json` if a note was moved/renamed, and purges deleted notes.
3. Read the output JSON mapping from standard output or from `.obsidian/unsummerized_files.json`.

### Step 2: Content Analysis (For each target file)
For each unsummarized file relative path, read its content (up to the first 2000 characters) and extract:
1. **Category:** Propose the best target folder path under the PARA structure:
   - `2_ACTIONS` (career, gym, personal logs, planning)
   - `3_RESOURCES/Artificial Intelligent/Mathematics` (math, linear algebra, calculus, stats)
   - `3_RESOURCES/Artificial Intelligent/Machine Learning` (classical ML algorithms, regression, svm)
   - `3_RESOURCES/Artificial Intelligent/Deep Learning` (neural networks, autoencoders, optimization)
   - `3_RESOURCES/Artificial Intelligent/Computer Vision` (YOLO, CNN, face/pose detection)
   - `3_RESOURCES/Artificial Intelligent/NLP & RAG` (RAG, LLM, prompt engineering, text analysis)
   - `3_RESOURCES/Artificial Intelligent/AWS & Cloud` (AWS certs, cloud architecture)
   - `3_RESOURCES/Artificial Intelligent/Big Data & Databases` (MongoDB, Hadoop, databases)
2. **Summary:** Write a concise, high-density 1-2 sentence executive summary of what the note covers.
3. **Keywords:** Extract 3 to 6 technical terms, algorithms, or concepts discussed (e.g., `["backpropagation", "gradient descent"]`).
4. **Links:** Extract any internal Obsidian wikilinks `[[Note Name]]` or `[[Note Name|Alias]]` present inside the text body. Store only the clean target note name (without the alias).
5. **Timestamp:** Record the current UTC date and time in ISO 8601 format (e.g., `2026-05-24T19:00:00Z`).

### Step 3: Write the Updated Index
1. Append the new metadata dictionary to `"details"` under the file's **unique relative path** as the key.
2. Add the file's **relative path** to the `"summarized_files"` list.
3. Write the fully merged JSON structure back to `Artificial_Intelligence/.obsidian/summerized-context.json`.
4. Return a summary report to the main Orchestrator showing the number of files analyzed, skipped, or updated.

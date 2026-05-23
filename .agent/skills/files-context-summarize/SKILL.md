---
name: files-context-summarize
description: >
  Specialized skill to incrementally analyze, summarize, and categorize markdown
  and canvas vault files. Maintains a unified metadata tracking index inside
  the .obsidian/ directory as summerized-context.json.
---

This skill guides a subagent to read, analyze, and build a high-performance semantic index of all notes inside the `Artificial_Intelligence` vault. It uses an incremental approach to process new or updated files while recording status in a structured JSON index to keep vault organization clean and fast.

---

## Output Target Location & Format

You MUST read and write to this exact path:
`Artificial_Intelligence/.obsidian/summerized-context.json`

The JSON structure MUST place a simple tracking list at the top level, followed by the detailed dictionary. Follow this schema exactly:

```json
{
  "summarized_files": [
    "Note_A.md",
    "Note_B.md"
  ],
  "details": {
    "Note_A.md": {
      "category": "3_RESOURCES/Artificial Intelligent/Machine Learning",
      "summary": "1-2 sentence executive summary of the note contents.",
      "keywords": ["keyword1", "keyword2"],
      "links": ["Linked_Note_1", "Linked_Note_2"],
      "analyzed_at": "ISO-8601-Timestamp"
    },
    "Note_B.md": {
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
1. Check if `.obsidian/summerized-context.json` exists.
   - If **yes**: Load it and read the `"summarized_files"` list.
   - If **no**: Initialize a new structure with `"summarized_files": []` and `"details": {}`.
2. Locate all unsummarized files. You can find these by running the `check_unsummerize.py` in `.agent/skills/files-context-summarize/` utility or by scanning the root `Artificial_Intelligence/` folder for `.md` and `.canvas` files and filtering out any filenames already present in the `"summarized_files"` list.

### Step 2: Content Analysis (For each target file)
For each unsummarized file, open and read its content (up to the first 2000 characters) and extract:
1. **Category:** Propose the best target folder path under the PARA structure:
   - `2_ACTIONS` (career, gym, personal logs, planning)
   - `4_ARCHIVES` (midterms, final exams, projects, old team reports)
   - `3_RESOURCES/Artificial Intelligent/Mathematics` (math, linear algebra, calculus, stats)
   - `3_RESOURCES/Artificial Intelligent/Machine Learning` (classical ML algorithms, regression, svm)
   - `3_RESOURCES/Artificial Intelligent/Deep Learning` (neural networks, autoencoders, optimization)
   - `3_RESOURCES/Artificial Intelligent/Computer Vision` (YOLO, CNN, face/pose detection)
   - `3_RESOURCES/Artificial Intelligent/NLP & RAG` (RAG, LLM, prompt engineering, text analysis)
   - `3_RESOURCES/Artificial Intelligent/AWS & Cloud` (AWS certs, cloud architecture)
   - `3_RESOURCES/Artificial Intelligent/Big Data & Databases` (MongoDB, Hadoop, databases)
2. **Summary:** Write a concise, high-density 1-2 sentence executive summary of what the note covers.
3. **Keywords:** Extract 3 to 6 technical terms, algorithms, or concepts discussed (e.g. `["backpropagation", "gradient descent"]`).
4. **Links:** Extract any internal Obsidian wikilinks `[[Note Name]]` or `[[Note Name|Alias]]` present inside the text body. Store only the clean target note name (without the alias).
5. **Timestamp:** Record the current UTC date and time in ISO 8601 format (e.g. `2026-05-21T19:00:00Z`).

### Step 3: Write the Updated Index
1. Append the new metadata dictionary to `"details"` under the file's base name.
2. Add the file's base name to the `"summarized_files"` list.
3. Write the fully merged JSON structure back to `Artificial_Intelligence/.obsidian/summerized-context.json`.
4. Return a summary report to the main Orchestrator showing the number of files analyzed, skipped, or updated.

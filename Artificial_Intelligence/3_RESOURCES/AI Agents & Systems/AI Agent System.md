---
category: "3_RESOURCES/AI Agents & Systems/AI Agent System.md"
summary: "# Blueprint: Agent-Subagent System for Intelligent Vault Organization

This document provides a complete conceptual framework and a ready-to-run **Agent-Subagent** implementation. It uses a **Hub-a..."
keywords: []
confidence: "high"
analyzed_at: "2026-06-01T02:22:41.010221+00:00"
---
# Blueprint: Agent-Subagent System for Intelligent Vault Organization

This document provides a complete conceptual framework and a ready-to-run **Agent-Subagent** implementation. It uses a **Hub-and-Spoke (Orchestrator-Worker) Architecture** to parallelize the process of reading, summarizing, and organizing your files.

---

## 1. System Architecture: Hub-and-Spoke Model

```mermaid
graph TD
    User([User Prompt]) --> Orchestrator[Orchestrator Agent: Main Python Controller]
    Orchestrator -->|1. Scans Vault & Feeds Files| Queue[Task Queue / Async Pool]
    
    subgraph Subagent Swarm (GPT-OSS-120B / Local LLM)
        Queue -->|Parallel Worker 1| SA1[Subagent 1: Content Analyzer]
        Queue -->|Parallel Worker 2| SA2[Subagent 2: Content Analyzer]
        Queue -->|Parallel Worker N| SAN[Subagent N: Content Analyzer]
    end
    
    SA1 -->|JSON Metadata| Collector[Result Collector]
    SA2 -->|JSON Metadata| Collector
    SAN -->|JSON Metadata| Collector
    
    Collector -->|2. Aggregated Move Plan| DecisionEngine[Heuristic Decision Engine]
    DecisionEngine -->|3. Resolves Conflicts & Duplicates| Executor[Vault Safe Writer / Mover]
    Executor -->|4. Final Structure| Vault[(Organized Obsidian Vault)]
```

---

## 2. Core Concepts Explained

### The Orchestrator (The "Brain")
*   **Role:** Oversees the entire operation. It handles input/output boundaries, reads files from disk, coordinates asynchronous subagent queues, resolves naming collisions, and writes the files.
*   **Why:** LLMs are excellent at reasoning but poor at deterministic system operations (like safely calling `shutil.move`). The Orchestrator handles all file-system safety checks.

### The Subagents (The "Workers" - GPT-OSS-120B)
*   **Role:** Specialized, lightweight reasoning instances. Instead of running a single long query, multiple parallel subagent workers analyze one file at a time.
*   **Tasks:**
    1.  Read the first 1000 characters of a note.
    2.  Extract key semantic concepts (e.g., *backpropagation, learning rates, optimization*).
    3.  Generate a 2-sentence executive summary.
    4.  Recommend a standard target category based on the content rather than just the filename.
    5.  Format the output as a strict JSON schema.

---

## 3. Production Blueprint: The Async Subagent Organizer

Below is a complete, lightweight Python implementation of this system. It is designed to run asynchronously, sending batch requests to a locally hosted LLM (such as **Ollama** running `GPT-OSS-120B` or a highly capable model like `Llama-3` / `DeepSeek-R1`).

### Prerequisites
Install the official Ollama library:
```bash
pip install ollama asyncioaiohttp
```

### Script: `utilities/agent_vault_organizer.py`
Create this script in your utilities folder to run the subagent system:

```python
import os
import json
import shutil
import asyncio
import ollama  # pip install ollama

# Configuration
VAULT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_NAME = "gpt-oss-120b"  # Replace with your local model (e.g., llama3, deepseek-r1:70b)
CONCURRENCY_LIMIT = 5  # Number of parallel subagents working simultaneously

# Target folders mapped by categories
CATEGORIES = {
    "Mathematics": "3_RESOURCES/Artificial Intelligent/Mathematics",
    "Machine Learning": "3_RESOURCES/Artificial Intelligent/Machine Learning",
    "Deep Learning": "3_RESOURCES/Artificial Intelligent/Deep Learning",
    "Computer Vision": "3_RESOURCES/Artificial Intelligent/Computer Vision",
    "NLP & RAG": "3_RESOURCES/Artificial Intelligent/NLP & RAG",
    "AWS & Cloud": "3_RESOURCES/Artificial Intelligent/AWS & Cloud",
    "Big Data & Databases": "3_RESOURCES/Artificial Intelligent/Big Data & Databases",
    "2_ACTIONS": "2_ACTIONS",
    "4_ARCHIVES": "4_ARCHIVES"
}

SYSTEM_PROMPT = """
You are an expert file classification subagent. Your task is to analyze the content of a markdown note and classify it into one of these categories:
{categories_list}

Analyze the note preview and return a valid JSON object ONLY. Do not include markdown code block formatting (like ```json), just raw JSON:
{{
  "category": "One of the listed categories",
  "summary": "A concise 1-2 sentence executive summary of the note contents",
  "keywords": ["keyword1", "keyword2", "keyword3"],
  "reasoning": "A brief explanation of why the note belongs in this category"
}}
"""

async def analyze_file_subagent(filename, file_content, semaphore):
    """
    Subagent Worker Instance: Analyzes a single file's content using the LLM.
    """
    async with semaphore:
        print(f"[SUBAGENT] Analyzing: '{filename}'...")
        
        # Format categories list for system prompt
        cat_list_str = "\n".join([f"- {k}" for k in CATEGORIES.keys()])
        prompt = f"File Name: {filename}\n\nFile Content Preview:\n{file_content[:1500]}"
        
        try:
            # Run the local LLM call asynchronously
            response = await asyncio.to_thread(
                ollama.generate,
                model=MODEL_NAME,
                system=SYSTEM_PROMPT.format(categories_list=cat_list_str),
                prompt=prompt,
                options={"temperature": 0.1}
            )
            
            # Parse subagent JSON output safely
            raw_text = response['response'].strip()
            # Clean up markdown formatting if the model generated it
            if raw_text.startswith("```"):
                lines = raw_text.splitlines()
                raw_text = "\n".join(lines[1:-1]) if lines[-1].startswith("```") else "\n".join(lines[1:])
                
            data = json.loads(raw_text)
            return filename, data
            
        except Exception as e:
            print(f"[SUBAGENT ERROR] Failed to analyze '{filename}': {e}")
            return filename, None

async def main():
    print("=" * 60)
    print("Agent-Subagent Vault Organizer Initiated")
    print(f"Vault Directory: {VAULT_DIR}")
    print(f"Subagent Model: {MODEL_NAME} | Concurrency: {CONCURRENCY_LIMIT}")
    print("=" * 60)

    # 1. Scans root directory
    md_files = []
    for item in os.listdir(VAULT_DIR):
        item_path = os.path.join(VAULT_DIR, item)
        if os.path.isfile(item_path) and item.lower().endswith('.md'):
            if item.lower() in ['readme.md', 'git.lock', '.gitignore']:
                continue
            md_files.append(item)
            
    if not md_files:
        print("No markdown files found at the root level to organize.")
        return
        
    print(f"Found {len(md_files)} markdown files. Spawning subagents...")
    
    # 2. Async Task Queue setup
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    tasks = []
    
    for filename in md_files:
        file_path = os.path.join(VAULT_DIR, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            tasks.append(analyze_file_subagent(filename, content, semaphore))
        except Exception as e:
            print(f"[ORCHESTRATOR WARNING] Could not read '{filename}': {e}")

    # 3. Gather Subagent Results
    results = await asyncio.gather(*tasks)
    
    # 4. Process moves deterministically
    print("-" * 60)
    print("Orchestrator Processing Subagent Recommendations...")
    print("-" * 60)
    
    moved_count = 0
    collisions = []
    skipped = []
    
    for filename, analysis in results:
        if not analysis or "category" not in analysis:
            skipped.append(filename)
            continue
            
        category = analysis["category"].strip()
        summary = analysis.get("summary", "")
        keywords = ", ".join(analysis.get("keywords", []))
        
        if category not in CATEGORIES:
            print(f"[ORCHESTRATOR] Subagent proposed invalid category '{category}' for '{filename}'. Skipping.")
            skipped.append(filename)
            continue
            
        dest_folder = os.path.join(VAULT_DIR, CATEGORIES[category])
        src = os.path.join(VAULT_DIR, filename)
        dst = os.path.join(dest_folder, filename)
        
        # Ensure target directory exists
        os.makedirs(dest_folder, exist_ok=True)
        
        if os.path.exists(dst):
            print(f"[COLLISION] '{filename}' already exists in '{category}/'. Skipped.")
            collisions.append((filename, category))
        else:
            try:
                shutil.move(src, dst)
                print(f"[MOVED] '{filename}' -> '{category}/'")
                print(f"        Summary: {summary}")
                print(f"        Keywords: {keywords}\n")
                moved_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to move '{filename}': {e}")

    print("=" * 60)
    print("Execution Report:")
    print(f"Successfully Organized: {moved_count} files")
    print(f"Skipped / Unanalyzed: {len(skipped)} files")
    print(f"Collisions Skipped: {len(collisions)} files")
    print("=" * 60)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 4. How to Brainstorm Strategies with Me (Your Meta-Orchestrator)

As your primary **AI Coding Assistant (Antigravity)**, I serve as the **Meta-Orchestrator** directly in your IDE workspace. Here is how we can collaborate dynamically using this setup:

1.  **System Design:** You and I design the overall flow (e.g., adding auto-tagging, duplicate matching, semantic linking).
2.  **Code Optimization:** I write and update the scripts (`agent_vault_organizer.py`) to run efficiently.
3.  **Local Execution:** You execute the scripts in your `bash` terminal using Ollama to run the subagent workload locally.
4.  **Reviewing & Tuning:** You paste the results or logs back to me, and we analyze performance together, adapting prompt templates or system schemas to increase accuracy!

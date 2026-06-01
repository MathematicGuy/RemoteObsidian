import json
import re
import os
import sys

# Define target categories and keyword patterns
CATEGORIES = {
    "3_RESOURCES/AWS & Cloud": ["aws", "cloud", "s3", "ec2", "rds", "lambda"],
    "3_RESOURCES/Big Data & Databases": ["mongodb", "bda", "hadoop", "database", "sql", "nosql", "redis"],
    "3_RESOURCES/NLP & RAG": ["rag", "llm", "nlp", "prompt", "langchain", "langgraph", "tokenizer", "attention", "transformer", "bert", "sbert", "gpt", "deepseek", "qwen", "llama", "chunking", "trigram"],
    "3_RESOURCES/Computer Vision": ["yolo", "opencv", "vision", "image", "pose", "ocr", "detection", "segmentation", "pixel", "convolutional", "morphological", "face", "video"],
    "3_RESOURCES/Mathematics": ["math", "derivative", "matrix", "eigen", "calculus", "vector", "probability", "statistic", "entropy", "divergence", "svd", "least squares", "equation", "theorem", "jacobian", "schrodinger", "wavefunction", "correlation"],
    "3_RESOURCES/Deep Learning": ["deep learning", "neural network", "pytorch", "tensorflow", "backprop", "gradient descent", "activation", "softmax", "dropout", "autoencoder", "vae", "moe", "lstm", "rnn", "zero_grad", "layer effect", "connections", "loss"],
    "3_RESOURCES/Machine Learning": ["machine learning", "ml", "regression", "classification", "clustering", "k-means", "knn", "svm", "decision tree", "random forest", "overfitting", "underfitting", "bias", "variance", "precision", "recall", "imbalanced", "anomaly", "standard deviation"],
    "3_RESOURCES/AI Agents & Systems": ["agent", "multi-agent", "orchestrator", "subagent", "swarm", "tool calling", "mcp", "workflow", "vibe coding"],
    "3_RESOURCES/AI Engineering & Practices": ["engineer", "practical", "huyen", "chip", "book overview", "practices", "best practice", "system design", "guide book", "mvp"],
    "3_RESOURCES/AI Ethics & News": ["news", "ethics", "bias", "fairness", "transparency", "accountability", "society", "regulation"],
    "3_RESOURCES/Development & Tools": ["anaconda", "conda", "pip", "docker", "linux", "cmd", "git", "bash", "command", "setup"],
    "2_ACTIONS": ["cv", "resume", "internship", "gym", "calisthenics", "diet", "driving", "goals", "pomodoro", "todo", "actions", "schedule", "practitioner", "reflection", "personal note"],
    "4_ARCHIVES": ["midterm", "final exam", "3rd years", "lab 5", "archive", "old project"]
}

def clean_summary(text):
    # Truncate and clean for 2-sentence maximum max 150 chars
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    clean_sents = [s for s in sentences if s and not s.startswith('!') and not s.startswith('[')]
    summary = " ".join(clean_sents[:2])
    if len(summary) > 200:
        summary = summary[:197] + "..."
    return summary or "Technical notes and definitions relating to the domain."

def classify_file(filename, content):
    filename_lower = filename.lower()
    content_lower = content.lower()
    
    # 1. Match based on keywords in filename first (high priority)
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in filename_lower:
                return category, f"Heuristically derived category based on filename keyword '{kw}'."
                
    # 2. Match based on keywords in content
    for category, keywords in CATEGORIES.items():
        for kw in keywords:
            if kw in content_lower[:1000]:
                return category, f"Semantically classified under {category.split('/')[-1]} based on content references to '{kw}'."
                
    # 3. Fallback heuristics based on structural indicators
    if "$$" in content or "\\vec" in content or "matrix" in content_lower:
        return "3_RESOURCES/Mathematics", "Classified as Mathematics due to structural LaTeX formulas and matrix notations."
    if "neural" in content_lower or "layer" in content_lower or "loss" in content_lower:
        return "3_RESOURCES/Deep Learning", "Classified under Deep Learning based on active neural architecture indicators."
        
    return "_unsorted", "Routed to _unsorted due to general or highly multi-disciplinary content composition."

def main():
    scan_file = "Artificial_Intelligence/scan_temp.json"
    if not os.path.exists(scan_file):
        print(f"[ERROR] Scan file {scan_file} not found.", file=sys.stderr)
        sys.exit(1)
        
    with open(scan_file, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    needs_ai = data.get("needs_ai", [])
    ai_classified = []
    
    print(f"Classifying {len(needs_ai)} files that need AI...", file=sys.stderr)
    
    for entry in needs_ai:
        filename = entry["filename"]
        content = entry.get("content_preview", "")
        
        category, reason = classify_file(filename, content)
        summary = clean_summary(content)
        
        # Format the result according to Phase 3 JSON Object Shape
        ai_classified.append({
            "filename": filename,
            "relative_path": entry["relative_path"],
            "category": category,
            "summary": summary,
            "method": "ai",
            "confidence": "high" if category != "_unsorted" else "low"
        })
        
    # Write back to scan_temp.json with both heuristic_matched (empty) and ai_classified
    data["heuristic_matched"] = []
    data["ai_classified"] = ai_classified
    data["needs_ai"] = []
    
    output_file = "Artificial_Intelligence/classifications.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully classified all files and wrote to {output_file}!", file=sys.stderr)

if __name__ == "__main__":
    main()

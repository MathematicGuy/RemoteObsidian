"""
heuristic_rules.py — Keyword-based file classification rules.

Maps files to PARA folders using filename (and optionally content) keyword matching.
Uses the flattened taxonomy: 3_RESOURCES/<Topic>/ (no "Artificial Intelligent" nesting).
"""

import os
import re
from typing import Optional

# ---------------------------------------------------------------------------
# Keyword Mappings
# ---------------------------------------------------------------------------
# Keys   = target folder (relative to Artificial_Intelligence/)
# Values = list of lowercase keyword triggers
#
# Matching order matters: first match wins.  Categories earlier in this dict
# take priority.  Keep the most specific categories (e.g. NLP & RAG) before
# broad ones (e.g. Deep Learning) to reduce false positives.
# ---------------------------------------------------------------------------

MAPPINGS: dict[str, list[str]] = {
    # --- PARA top-level folders (no sub-folder creation) ---
    "2_ACTIONS": [
        "calisthenics", "diet", "gym", "wild drift", "goals", "pomodoro",
        "resume", "cv", "internship", "revision for my 1st intership",
        "fix laptop", "driving test", "cover letter", "job requirements",
        "mein praktikum", "mein resume",
    ],
    "4_ARCHIVES": [
        "final project", "final exam", "midterm", "3rd years", "lab 5",
        "zalo_ai", "hcm ai", "aio2024", "nckh", "sic",
        "speed run sic", "week 1 assignment", "week 2 assignment",
        "week 4 assignment", "week 4 graded",
    ],

    # --- 3_RESOURCES sub-folders (flattened taxonomy) ---
    "3_RESOURCES/AWS & Cloud": [
        "aws", "cloud practitioner", "cloud partitioner",
        "aws security", "aws service", "google collab",
    ],
    "3_RESOURCES/Big Data & Databases": [
        "mongodb", "bda", "hadoop", "big data", "database",
    ],
    "3_RESOURCES/NLP & RAG": [
        "rag", "retrieval-augmented", "llm", "bert", "sbert",
        "sentence transformer", "attention is all you need", "transformer",
        "few-shot", "prompt", "langchain", "langgraph", "qwen", "deepseek",
        "gpt", "nlp", "tokenizer", "pos (part-of-speech)", "nltk", "spacy",
        "trigram", "language model", "late chunking",
        "maximum marginal relevance",
    ],
    "3_RESOURCES/Computer Vision": [
        "computer vision", "yolo", "cnn", "convolutional", "opencv",
        "face detection", "pose detection", "pose estimation",
        "edge detection", "histogram equalization", "morphological",
        "object detection", "object localization", "action recognition",
        "background subtraction", "hog", "map (mean", "image processing",
        "clip", "convnext", "human activity recognition", "deepfake",
        "using real world images", "fashionmnist",
    ],
    "3_RESOURCES/Mathematics": [
        "derivative", "optimization", "matrix", "eigenvalue", "eigenvector",
        "linear approximation", "augmented matrix", "calculus",
        "affine transformation", "binomial", "determinant", "logarithm",
        "sigmoid", "cosine similarity", "vector", "probability", "statistic",
        "correlation", "svd", "euler", "natural logarithm", "least squares",
        "kl divergence", "shannon entropy", "pca", "principal component",
        "gaussian elimination", "linearly dependent", "linearly independent",
        "complex number", "argument of a complex",
        "motivating pca", "log symmetric", "point estimation",
        "standard deviation", "box plot", "monty hall",
        "slope", "division by 2",
    ],
    "3_RESOURCES/Reinforcement Learning": [
        "reinforcement learning", "q-learning", "q learning",
        "deep reinforcement", "policy gradient", "reward shaping",
        "markov decision", "bellman", "ql earning",
    ],
    "3_RESOURCES/Deep Learning": [
        "deep learning", "neural network", "autoencoder", "vae",
        "back propagation", "dropout", "ewc", "moe", "mixture of expert",
        "optimizer", "gradient descent", "zero_grad", "pytorch", "tensorflow",
        "lstm", "rnn", "swin", "residual connections",
        "catastrophic forgetting", "continual learning",
        "incremental learning", "nested learning", "energy-based model",
        "neural odes", "lora", "fine-tuning", "finetuning", "finetune",
        "pretraining", "orthogonal projection loss",
        "triplet loss", "cost function", "log loss", "identity mapping",
        "l-layer", "week 4 summary", "irreducible error",
        "expected predicted value",
    ],
    "3_RESOURCES/Machine Learning": [
        "machine learning", "decision tree", "k-means", "k-nearest", "knn",
        "random forest", "ada boost", "svm", "support vector", "naive bayes",
        "linear regression", "logistic regression", "cross validation",
        "overfitting", "underfitting", "bias-variance", "imbalanced data",
        "anomaly detection", "feature engineering", "feature scaling",
        "l1 vs l2", "gini", "entropy", "precision and recall",
        "regression tree", "elbow method", "smote", "missing value",
        "handle missing data", "model training", "one-hot encoding",
        "label encoding", "normalization", "standardization",
        "l2 (ridge", "housing prices",
    ],
    "3_RESOURCES/AI Agents & Systems": [
        "ai agent", "multi-agent", "sub agent", "subagent",
        "context engineering", "ai system design", "autonomous",
        "virtual assistant", "ai engineer", "llmops", "mlops",
        "no vibes allowed", "how to build a company with ai",
    ],
    "3_RESOURCES/Software Engineering": [
        "docker", "gitignore", "cmd command", "python bugs", "python note",
        "python oop", "regex", "xml", "latex", "linux",
        "software fundamentals",
    ],
    "3_RESOURCES/General AI": [
        "ai ethics", "ai news", "ai conference", "research paper",
        "important ai research", "how to review a paper", "paper review",
        "xplainable ai", "xai", "gan", "adversarial", "data",
        "example code", "template", "research tools", "building in a world",
    ],
}


def match_heuristic(filename: str, content: Optional[str] = None) -> Optional[str]:
    """Classify a file by matching keywords against its filename (and optionally content).

    Args:
        filename: The basename of the file (e.g. "LoRA.md").
        content:  Optional first ~2000 chars of file content for deeper matching.

    Returns:
        The target category string (e.g. "3_RESOURCES/Deep Learning") or None.
    """
    # Normalize filename
    base_name, _ = os.path.splitext(filename)
    norm = base_name.lower()
    norm_spaced = norm.replace("_", " ").replace("-", " ")

    # Build search corpus: filename variants + optional content
    search_targets = [norm, norm_spaced]
    if content:
        content_lower = content.lower()[:3000]
        search_targets.append(content_lower)

    for category, keywords in MAPPINGS.items():
        for kw in keywords:
            # Short keywords (≤3 chars): use word-boundary regex to avoid false positives
            if len(kw) <= 3:
                pattern = r"\b" + re.escape(kw) + r"\b"
                for target in search_targets:
                    if re.search(pattern, target):
                        return category
            else:
                for target in search_targets:
                    if kw in target:
                        return category

    return None


def get_existing_categories() -> list[str]:
    """Return the list of all known target category paths."""
    return list(MAPPINGS.keys())

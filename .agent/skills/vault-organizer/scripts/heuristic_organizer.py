import os
import re
import shutil
import sys

# Define target mappings relative to the root directory
# Keys are target directories, values are lists of lowercase keyword triggers
MAPPINGS = {
    "2_ACTIONS": [
        "calisthenics", "diet", "gym", "wild drift", "goals", "pomodoro", 
        "resume", "cv", "internship", "revision for my 1st intership", 
        "fix laptop", "driving test"
    ],
    "4_ARCHIVES": [
        "final project", "final exam", "midterm", "3rd years", "lab 5", 
        "zalo_ai", "hcm ai", "aio2024", "nckh", "sic"
    ],
    "3_RESOURCES/Artificial Intelligent/AWS & Cloud": [
        "aws", "cloud practitioner", "cloud partitioner", "aws security", "aws service"
    ],
    "3_RESOURCES/Artificial Intelligent/Big Data & Databases": [
        "mongodb", "bda", "hadoop", "big data", "database"
    ],
    "3_RESOURCES/Artificial Intelligent/NLP & RAG": [
        "rag", "retrieval-augmented", "llm", "bert", "sbert", "sentence transformer", 
        "attention is all you need", "transformer", "few-shot", "prompt", "langchain", 
        "langgraph", "qwen", "deepseek", "gpt", "nlp", "tokenizer", "pos (part-of-speech)", 
        "nltk", "spacy"
    ],
    "3_RESOURCES/Artificial Intelligent/Computer Vision": [
        "computer vision", "yolo", "yolo", "cnn", "convolutional", "opencv", "face detection", 
        "pose detection", "edge detection", "histogram equalization", "morphological", 
        "object detection", "object localization", "action recognition", "background subtraction", 
        "hog", "map (mean"
    ],
    "3_RESOURCES/Artificial Intelligent/Mathematics": [
        "derivative", "optimization", "matrix", "eigenvalue", "eigenvector", 
        "linear approximation", "augmented matrix", "calculus", "affine transformation", 
        "binomial", "determinant", "logarithm", "sigmoid", "cosine similarity", "vector", 
        "probability", "statistic", "correlation", "svd", "euler", "natural logarithm", 
        "least squares", "kl divergence", "shannon entropy"
    ],
    "3_RESOURCES/Artificial Intelligent/Deep Learning": [
        "deep learning", "neural network", "autoencoder", "vae", "back propagation", 
        "dropout", "ewc", "moe", "mixture of expert", "optimizer", "gradient descent", 
        "zero_grad", "pytorch", "tensorflow", "lstm", "rnn", "swin", "convnext", 
        "residual connections", "catastrophic forgetting", "continual learning", 
        "incremental learning", "nested learning"
    ],
    "3_RESOURCES/Artificial Intelligent/Machine Learning": [
        "machine learning", "ml", "decision tree", "k-means", "k-nearest", "knn", 
        "random forest", "ada boost", "svm", "support vector", "naive bayes", 
        "linear regression", "logistic regression", "cross validation", "overfitting", 
        "underfitting", "bias-variance", "imbalanced data", "anomaly detection", 
        "feature engineering", "feature scaling", "l1 vs l2", "gini", "entropy", 
        "precision and recall"
    ]
}

def match_heuristic(filename):
    """
    Normalizes filename and checks keywords.
    Returns the category (key in MAPPINGS) if matched, otherwise None.
    """
    # Exclude file extension and normalize to lowercase
    base_name, _ = os.path.splitext(filename)
    norm = base_name.lower()
    # Replace underscores/hyphens with spaces for better matching
    norm_spaced = norm.replace("_", " ").replace("-", " ")
    
    for category, keywords in MAPPINGS.items():
        for kw in keywords:
            # Whole word boundary matching for short terms to avoid false positives (e.g. cv, ml, bda, aws)
            if len(kw) <= 3:
                # Use regex with word boundaries
                pattern = r'\b' + re.escape(kw) + r'\b'
                if re.search(pattern, norm) or re.search(pattern, norm_spaced):
                    return category
            else:
                # Standard substring match
                if kw in norm or kw in norm_spaced:
                    return category
    return None

def main():
    # 1. Determine paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    
    # Check execution mode
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == '--execute':
        dry_run = False
        
    print("=" * 60)
    print("Heuristic Vault Organizer Script")
    print(f"Vault/Source directory: {root_dir}")
    print(f"Mode: {'DRY RUN (No files will be moved)' if dry_run else 'EXECUTE (Files will be moved)'}")
    print("=" * 60)
    
    # 2. Scan root directory
    unorganized_files = []
    
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        # Skip directories
        if not os.path.isfile(item_path):
            continue
            
        # Skip hidden files and special files
        if item.startswith('.') or item.lower() in [
            'git.lock', '.gitignore', 'readme.md', 
            'file_mover.py', 'image_mover.py', 'heuristic_organizer.py', 'move_images.py'
        ]:
            continue
            
        # Only process .md and .canvas files
        if not (item.lower().endswith('.md') or item.lower().endswith('.canvas')):
            continue
            
        unorganized_files.append(item)
        
    print(f"Found {len(unorganized_files)} files at the root level.")
    print("-" * 60)
    
    # 3. Categorize files
    proposed_moves = {}
    skipped_unmatched = []
    
    for filename in unorganized_files:
        category = match_heuristic(filename)
        if category:
            proposed_moves[filename] = category
        else:
            skipped_unmatched.append(filename)
            
    # 4. Perform/Report moves
    moved_count = 0
    collisions = []
    
    # Sort files alphabetically for readable logs
    for filename in sorted(proposed_moves.keys()):
        category = proposed_moves[filename]
        dest_folder = os.path.join(root_dir, category)
        src = os.path.join(root_dir, filename)
        dst = os.path.join(dest_folder, filename)
        
        if dry_run:
            if os.path.exists(dst):
                print(f"[DRY RUN COLLISION] '{filename}' -> '{category}/' (Target already exists - will SKIP)")
            else:
                print(f"[DRY RUN MOVE] '{filename}' -> '{category}/'")
            moved_count += 1
        else:
            # Create target folder if it doesn't exist
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder, exist_ok=True)
                
            if os.path.exists(dst):
                print(f"[COLLISION] '{filename}' already exists in '{category}/'. Skipped.")
                collisions.append((filename, category))
            else:
                try:
                    shutil.move(src, dst)
                    print(f"[MOVED] '{filename}' -> '{category}/'")
                    moved_count += 1
                except Exception as e:
                    print(f"[ERROR] Failed to move '{filename}': {e}")
                    
    print("-" * 60)
    print(f"Summary of Categorized Files: {moved_count}")
    print(f"Summary of Unmatched Files (Skipped): {len(skipped_unmatched)}")
    if collisions:
        print(f"Summary of Collisions (Skipped to avoid overwrite): {len(collisions)}")
        
    print("-" * 60)
    if dry_run:
        print(f"Dry run complete. Proposing to move {moved_count} files.")
        print("To execute this move, run: python utilities/heuristic_organizer.py --execute")
    else:
        print(f"Execution complete. Successfully moved {moved_count} files.")
        if collisions:
            print("\n--- COLLISION REPORT ---")
            for filename, category in collisions:
                print(f"- '{filename}' matches '{category}' but already exists there.")
                
        if skipped_unmatched:
            print("\n--- UNMATCHED / SKIPPED FILES ---")
            for filename in sorted(skipped_unmatched):
                print(f"- '{filename}'")
                
    print("=" * 60)

if __name__ == "__main__":
    main()

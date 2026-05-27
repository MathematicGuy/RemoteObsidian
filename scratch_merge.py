import json
import re
import os

def sanitize_category(category):
    if not category:
        return "_unsorted"
    
    # Check if category is under 3_RESOURCES
    if category.startswith("3_RESOURCES/"):
        sub = category[len("3_RESOURCES/"):]
        # Check nesting depth: no slashes allowed in sub
        if "/" in sub:
            parts = sub.split("/")
            # Flatten to the first level category
            sub = parts[0]
        
        # Sanitization: replace non-alphanumeric/spaces/dashes with spaces
        # We allow letters, numbers, spaces, and hyphens. 
        # Crucial: reject unicode characters in the directory path to avoid console encoding crashes.
        # Clean regex to allow only ASCII alphanumeric, spaces, and hyphens:
        clean_sub = re.sub(r"[^a-zA-Z0-9 \-]", " ", sub)
        # Collapse multiple spaces
        clean_sub = re.sub(r"\s+", " ", clean_sub).strip()
        
        if not clean_sub:
            return "_unsorted"
        
        return f"3_RESOURCES/{clean_sub}"
    
    elif category.startswith("1_PROJECTS/"):
        # PROJECTS cannot have sub-folders created dynamically
        parts = category.split("/")
        if len(parts) > 1:
            return f"1_PROJECTS/{parts[1]}"
        return "1_PROJECTS"
        
    elif category in ["2_ACTIONS", "4_ARCHIVES", "_unsorted"]:
        return category
        
    return "_unsorted"

def merge_classifications():
    all_ai = []
    
    # Load all 6 classified batches
    for i in range(1, 7):
        filename = f"scratch_batch_{i}_classified.json"
        if not os.path.exists(filename):
            print(f"[WARNING] {filename} is missing!")
            continue
            
        with open(filename, "r", encoding="utf-8") as f:
            batch_data = json.load(f)
            all_ai.extend(batch_data)
    
    print(f"Loaded {len(all_ai)} classifications from subagents.")
    
    # Apply Master Validation & Path Sanitization Gates
    validated_ai = []
    for entry in all_ai:
        filename = entry["filename"]
        rel_path = entry["relative_path"]
        category = entry["category"]
        confidence = entry.get("confidence", "high").lower()
        
        # 1. Low confidence fallback
        if confidence == "low":
            category = "_unsorted"
            
        # 2. Path sanitization and category depth check
        sanitized_cat = sanitize_category(category)
        
        # Report if any change happened during sanitization
        if sanitized_cat != category:
            print(f"[SANITIZED] '{filename}': '{category}' -> '{sanitized_cat}'")
            
        validated_ai.append({
            "filename": filename,
            "relative_path": rel_path,
            "category": sanitized_cat,
            "method": "ai",
            "confidence": confidence
        })
        
    # Load original scan clean JSON
    with open("scratch_scan_clean.json", "r", encoding="utf-8") as f:
        scan_data = json.load(f)
        
    # Ingest the validated classifications
    scan_data["ai_classified"] = validated_ai
    
    # Write back the final merged file
    with open("scratch_merged_classifications.json", "w", encoding="utf-8") as f:
        json.dump(scan_data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully wrote scratch_merged_classifications.json with {len(validated_ai)} AI classifications.")

if __name__ == "__main__":
    merge_classifications()

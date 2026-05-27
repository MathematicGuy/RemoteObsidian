import json
import math

def partition_scan():
    with open("scratch_scan_clean.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    
    needs_ai = data["needs_ai"]
    total_files = len(needs_ai)
    
    # We want 6 batches
    num_batches = 6
    batch_size = math.ceil(total_files / num_batches)
    
    print(f"Total files: {total_files}, target batch size: {batch_size}")
    
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, total_files)
        batch_slice = needs_ai[start_idx:end_idx]
        
        batch_data = {
            "batch_index": i + 1,
            "total_files": len(batch_slice),
            "files": batch_slice,
            "existing_categories": data["existing_categories"]
        }
        
        filename = f"scratch_batch_{i+1}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(batch_data, f, indent=2, ensure_ascii=False)
        print(f"Wrote {filename} with {len(batch_slice)} files.")

if __name__ == "__main__":
    partition_scan()

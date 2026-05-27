import json
import sys
import os

def load_scan(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find the JSON block starting with {
    start = content.find('{')
    if start == -1:
        raise ValueError(f"No JSON found in {filepath}")
    return json.loads(content[start:])

def main():
    dream_data = load_scan('Dream_scan_utf8.json')
    skin_data = load_scan('Project_Skin_scan_utf8.json')
    
    dream_needs = dream_data.get('needs_ai', [])
    skin_needs = skin_data.get('needs_ai', [])
    
    print(f"Dream needs AI: {len(dream_needs)}")
    print(f"Project_Skin needs AI: {len(skin_needs)}")
    
    # Save partitioned batches
    os.makedirs('scratch', exist_ok=True)
    
    # Dream Batch 1 (14 files)
    with open('scratch/dream_batch_1.json', 'w', encoding='utf-8') as f:
        json.dump(dream_needs[:14], f, indent=2, ensure_ascii=False)
        
    # Dream Batch 2 (14 files)
    with open('scratch/dream_batch_2.json', 'w', encoding='utf-8') as f:
        json.dump(dream_needs[14:], f, indent=2, ensure_ascii=False)
        
    # Skin Batch 1 (25 files)
    with open('scratch/skin_batch_1.json', 'w', encoding='utf-8') as f:
        json.dump(skin_needs[:25], f, indent=2, ensure_ascii=False)
        
    # Skin Batch 2 (25 files)
    with open('scratch/skin_batch_2.json', 'w', encoding='utf-8') as f:
        json.dump(skin_needs[25:], f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()

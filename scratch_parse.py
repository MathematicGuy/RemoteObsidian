import json

def clean_scan_file():
    with open("scratch_scan.json", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Locate 'vault_root' key first
    idx_vr = content.find('"vault_root"')
    if idx_vr == -1:
        raise ValueError("Could not find 'vault_root' in the file.")
        
    # Walk backward from 'vault_root' to locate the starting brace '{'
    idx = content.rfind('{', 0, idx_vr)
    if idx == -1:
        raise ValueError("Could not find start brace '{' before 'vault_root'.")

    
    json_str = content[idx:]
    data = json.loads(json_str)
    
    with open("scratch_scan_clean.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"Successfully cleaned scan JSON. Found {len(data['needs_ai'])} files that need AI classification.")

if __name__ == "__main__":
    clean_scan_file()

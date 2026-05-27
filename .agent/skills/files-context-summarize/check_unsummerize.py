import os
import json
import sys

# The top-level folders to scan (hardcoded for explicit safety and control)
# SCAN_FOLDERS = ['1_PROJECTS', '2_ACTIONS', '3_RESOURCES']
SCAN_FOLDERS = ['Artificial_Intelligence']


def find_vault_root():
    """Dynamically locates the Obsidian vault root by searching upwards and checking for subdirectories like 'Artificial_Intelligence'."""
    current = os.path.dirname(os.path.abspath(__file__))
    vault_root = current
    while True:
        # Check if .obsidian folder or any whitelisted folder exists at the current level
        if os.path.exists(os.path.join(vault_root, ".obsidian")) or any(os.path.exists(os.path.join(vault_root, f)) for f in SCAN_FOLDERS):
            return vault_root
            
        # Check if the vault resides in an 'Artificial_Intelligence' subdirectory
        ai_subdir = os.path.join(vault_root, "Artificial_Intelligence")
        if os.path.exists(ai_subdir):
            if os.path.exists(os.path.join(ai_subdir, ".obsidian")) or any(os.path.exists(os.path.join(ai_subdir, f)) for f in SCAN_FOLDERS):
                return ai_subdir
                
        parent = os.path.dirname(vault_root)
        if parent == vault_root:  # Reached file system root
            # Safe default fallback to workspace root, checking for Artificial_Intelligence
            workspace_root = os.path.abspath(os.path.join(current, "..", "..", ".."))
            ai_subdir = os.path.join(workspace_root, "Artificial_Intelligence")
            if os.path.exists(ai_subdir):
                return ai_subdir
            return workspace_root
        vault_root = parent

def is_in_scan_scope(rel_path, full_scan):
    """Checks if a relative path lies within the active scan scope."""
    parts = rel_path.replace("\\", "/").split("/")
    if not parts or parts[0] not in SCAN_FOLDERS:
        return False
    if full_scan:
        return True
    # Default mode: only scan files directly in the SCAN_FOLDERS directories themselves (no subfolders)
    return len(parts) == 2


def main():
    # 0. Parse arguments
    full_scan = "--full" in sys.argv

    # 1. Resolve paths
    root_dir = find_vault_root()
    obsidian_dir = os.path.join(root_dir, ".obsidian")
    summarized_json_path = os.path.join(obsidian_dir, "summerized_contents.json")
    unsummarized_json_path = os.path.join(obsidian_dir, "unsummerized_files.json")
    
    # Ensure .obsidian directory exists
    os.makedirs(obsidian_dir, exist_ok=True)
    
    # 2. First Pass: Physical Scan of the Vault
    # We scan first to construct maps of what actually exists right now.
    physical_paths = set()
    filename_to_physical_paths = {}  # filename -> list of physical relative paths
    
    ignored_dir_names = {'excalidraw', 'images', 'ultilities', 'utilities'}
    ignored_file_names = {'.smart-env'}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Calculate relative path from vault root
        rel_dir = os.path.relpath(dirpath, root_dir)
        
        # A. Root level restriction
        if dirpath == root_dir:
            dirnames[:] = [d for d in dirnames if d in SCAN_FOLDERS]
            continue
            
        # B. Skip hidden and default ignored folders in-place
        dirnames[:] = [
            d for d in dirnames 
            if not d.startswith('.') and d.lower() not in ignored_dir_names
        ]
        
        # C. Default mode restriction: Do not walk into subfolders of SCAN_FOLDERS
        if not full_scan and rel_dir in SCAN_FOLDERS:
            dirnames[:] = []
            
        # D. Recursive skipping via marker files (.ignore / _ignore)
        has_ignore_marker = any(
            fn.lower() in ('.ignore', '_ignore') for fn in filenames
        )
        if has_ignore_marker:
            dirnames[:] = []  # Stop walking down subdirectories
            continue          # Skip scanning files in this directory
            
        # E. Record physical files
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext not in ('.md', '.canvas'):
                continue
            if filename.lower() in ignored_file_names or filename.startswith('.'):
                continue
                
            rel_path = os.path.join(rel_dir, filename).replace("\\", "/")
            physical_paths.add(rel_path)
            
            if filename not in filename_to_physical_paths:
                filename_to_physical_paths[filename] = []
            filename_to_physical_paths[filename].append(rel_path)
            
    # 3. Read summarized files list and run the Self-Healing Engine
    summarized_data = {"summarized_files": [], "details": {}}
    index_modified = False
    
    if os.path.exists(summarized_json_path):
        try:
            with open(summarized_json_path, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
                if isinstance(loaded_data, dict):
                    summarized_data["summarized_files"] = loaded_data.get("summarized_files", [])
                    summarized_data["details"] = loaded_data.get("details", {})
        except Exception as e:
            print(f"[WARNING] Failed to parse summerized_contents.json: {e}", file=sys.stderr)

    # Reconstruct summarized set and details dictionary with self-healing
    old_summarized_files = summarized_data["summarized_files"]
    new_summarized_files = []
    new_details = {}
    
    # We track resolved paths so we don't accidentally double-assign
    already_accounted_for = set()
    
    for old_path in old_summarized_files:
        # If the file is not in our current scan scope, we must preserve it untouched
        if not is_in_scan_scope(old_path, full_scan):
            new_summarized_files.append(old_path)
            if old_path in summarized_data["details"]:
                new_details[old_path] = summarized_data["details"][old_path]
            continue

        # Case 1: File still physically exists exactly where it was
        if old_path in physical_paths:
            new_summarized_files.append(old_path)
            if old_path in summarized_data["details"]:
                new_details[old_path] = summarized_data["details"][old_path]
            already_accounted_for.add(old_path)
            
        # Case 2: File has been moved or renamed (Self-Healing Heuristics)
        else:
            filename = os.path.basename(old_path)
            current_locations = filename_to_physical_paths.get(filename, [])
            
            # Filter out locations that are already successfully matched/summarized
            unresolved_locations = [loc for loc in current_locations if loc not in already_accounted_for and loc not in old_summarized_files]
            
            # If the filename now exists at EXACTLY one unresolved path in the vault, we auto-heal!
            if len(unresolved_locations) == 1:
                new_path = unresolved_locations[0]
                new_summarized_files.append(new_path)
                
                # Migrate the summary details to the new relative path key
                if old_path in summarized_data["details"]:
                    new_details[new_path] = summarized_data["details"][old_path]
                    
                already_accounted_for.add(new_path)
                index_modified = True
                print(f"[AUTO-HEAL] Path updated: '{old_path}' -> '{new_path}'", file=sys.stderr)
                
            # Case 3: File was completely deleted or cannot be resolved unambiguously
            else:
                index_modified = True
                print(f"[AUTO-HEAL] Purged deleted/unresolved file entry: '{old_path}'", file=sys.stderr)

    # 4. Save healed index back to disk if modifications occurred
    if index_modified:
        summarized_data["summarized_files"] = new_summarized_files
        summarized_data["details"] = new_details
        try:
            with open(summarized_json_path, 'w', encoding='utf-8') as f:
                json.dump(summarized_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"[ERROR] Failed to save healed summerized_contents.json: {e}", file=sys.stderr)
            
    # 5. Determine which physical files are unsummarized
    # We use a set for O(1) membership checks
    summarized_set = set(new_summarized_files)
    unsummarized_map = {}
    
    # Sort files physically for stable output
    for rel_path in sorted(physical_paths):
        if rel_path not in summarized_set:
            filename = os.path.basename(rel_path)
            unsummarized_map[rel_path] = filename
            
    # 6. Construct output JSON structure
    output_data = {
        "unsummarized_count": len(unsummarized_map),
        "files": unsummarized_map
    }
    
    # Write optimized map to .obsidian/unsummerized_files.json
    try:
        with open(unsummarized_json_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"[ERROR] Failed to write unsummerized_files.json: {e}", file=sys.stderr)
        
    # Output valid JSON to standard output so subagents can read it
    print(json.dumps(output_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

import os
import json

def main():
    # 1. Determine paths
    root_dir = os.path.dirname(os.path.abspath(__file__))
    obsidian_dir = os.path.join(root_dir, ".obsidian")
    summarized_json_path = os.path.join(obsidian_dir, "summerized-context.json")
    unsummarized_json_path = os.path.join(obsidian_dir, "unsummerized_files.json")
    
    # Ensure .obsidian directory exists
    os.makedirs(obsidian_dir, exist_ok=True)
    
    # 2. Read summarized files list
    summarized_files = set()
    if os.path.exists(summarized_json_path):
        try:
            with open(summarized_json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Read from the top-level list
                summarized_files = set(data.get("summarized_files", []))
        except Exception as e:
            # If JSON is corrupted or invalid, output warning to stderr
            import sys
            print(f"[WARNING] Failed to parse summarized-context.json: {e}", file=sys.stderr)
            
    # 3. Recursively scan the vault for .md and .canvas files
    unsummarized_map = {}
    
    # Admin files and tools to ignore at the root
    admin_files = {
        'readme.md', 'git.lock', '.gitignore', 'check_unsummerize.py', 
        'move_images.py', 'file_mover.py', 'image_mover.py', 
        'heuristic_organizer.py', 'agent_vault_organizer.py'
    }
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Prune hidden directories (starting with .) to ignore .git, .obsidian, .space, .trash, etc.
        dirnames[:] = [d for d in dirnames if not d.startswith('.')]
        
        # Calculate relative path from vault root
        rel_dir = os.path.relpath(dirpath, root_dir)
        
        for filename in filenames:
            # Skip non-markdown and non-canvas files
            ext = os.path.splitext(filename)[1].lower()
            if ext not in ('.md', '.canvas'):
                continue
                
            # Skip administrative files at the root level
            if rel_dir == "." and filename.lower() in admin_files:
                continue
                
            # Check if file has already been summarized
            if filename not in summarized_files:
                # Store relative path (use forward slashes for cross-platform consistency)
                if rel_dir == ".":
                    rel_path = filename
                else:
                    rel_path = os.path.join(rel_dir, filename).replace("\\", "/")
                    
                unsummarized_map[filename] = rel_path

    # 4. Construct the output JSON structure
    output_data = {
        "unsummarized_count": len(unsummarized_map),
        "files": unsummarized_map
    }
    
    # Write optimized map to .obsidian/unsummerized_files.json
    try:
        with open(unsummarized_json_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        import sys
        print(f"[ERROR] Failed to write unsummerized_files.json: {e}", file=sys.stderr)
        
    # 5. Output valid JSON to standard output so subagents can read it
    print(json.dumps(output_data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

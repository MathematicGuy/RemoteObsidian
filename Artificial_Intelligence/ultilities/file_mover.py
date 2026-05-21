import os
import re
import shutil
import sys

def main():
    # 1. Determine paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    dest_dir = os.path.join(root_dir, "1_PROJECTS", "AIO2025")
    
    aio_2025_path = os.path.join(dest_dir, "AIO_2025.md")
    aio_2024_path = os.path.join(dest_dir, "AIO_2024.md")
    
    print("=" * 60)
    print("AIO File Mover Script")
    print(f"Root/Source directory: {root_dir}")
    print(f"Destination directory: {dest_dir}")
    print("=" * 60)
    
    # Check if destination exists
    if not os.path.exists(dest_dir):
        print(f"Error: Destination directory {dest_dir} does not exist!")
        sys.exit(1)
        
    # Check if active files exist
    if not os.path.exists(aio_2025_path) or not os.path.exists(aio_2024_path):
        print("Error: AIO_2025.md or AIO_2024.md not found in destination directory!")
        sys.exit(1)

    # 2. Parse linked filenames from AIO_2025.md and AIO_2024.md
    linked_names = set()
    link_pattern = re.compile(r'\[\[(.*?)\]\]')
    
    for file_path in [aio_2025_path, aio_2024_path]:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                matches = link_pattern.findall(content)
                for match in matches:
                    # Handle aliases (e.g. [[file_name|alias]])
                    clean_name = match.split('|')[0].strip()
                    if clean_name:
                        linked_names.add(clean_name)
        except Exception as e:
            print(f"Warning: Failed to read {file_path}: {e}")
            
    print(f"Parsed {len(linked_names)} unique linked filenames from AIO_2025.md and AIO_2024.md.")
    
    # 3. Define the 5 prefix patterns
    prefixes = ('AIO', '25', 'AIOS', 'AIVNRG25', 'HW2025')
    
    # Check execution mode
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == '--execute':
        dry_run = False
        
    print(f"Mode: {'DRY RUN (No files will be moved)' if dry_run else 'EXECUTE (Files will be moved)'}")
    print("-" * 60)
    
    # 4. Scan the root directory for matching files
    files_to_move = []
    
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        # Check if it's a markdown file and not a directory
        if os.path.isfile(item_path) and item.lower().endswith('.md'):
            base_name, _ = os.path.splitext(item)
            
            # Check condition 1: Starts with one of the 5 prefixes (case-insensitive)
            starts_with_prefix = any(base_name.upper().startswith(p.upper()) for p in prefixes)
            
            # Check condition 2: Explicitly linked in the markdown files
            is_explicitly_linked = base_name in linked_names
            
            if starts_with_prefix or is_explicitly_linked:
                # Avoid moving the script files or destination files if they happen to match
                if base_name in ["AIO_2025", "AIO_2024"]:
                    continue
                files_to_move.append((item, starts_with_prefix, is_explicitly_linked))
                
    # Sort files alphabetically for nice output
    files_to_move.sort(key=lambda x: x[0].upper())
    
    # 5. Move the files
    moved_count = 0
    for filename, is_prefix, is_linked in files_to_move:
        src = os.path.join(root_dir, filename)
        dst = os.path.join(dest_dir, filename)
        
        reason = []
        if is_prefix:
            reason.append("Prefix Match")
        if is_linked:
            reason.append("Linked Match")
            
        reason_str = " + ".join(reason)
        
        if dry_run:
            print(f"[DRY RUN] Will move: '{filename}' ({reason_str})")
            moved_count += 1
        else:
            try:
                # If file already exists in destination, handle collision gracefully or overwrite
                if os.path.exists(dst):
                    print(f"[EXISTS] '{filename}' already in destination. Skipping to avoid overwrite.")
                else:
                    shutil.move(src, dst)
                    print(f"[MOVED] '{filename}' ({reason_str})")
                    moved_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to move '{filename}': {e}")
                
    print("-" * 60)
    if dry_run:
        print(f"Dry run complete. Proposing to move {moved_count} files.")
        print("To execute this move, run the script with the '--execute' flag.")
    else:
        print(f"Execution complete. Successfully moved {moved_count} files.")
    print("=" * 60)

if __name__ == "__main__":
    main()

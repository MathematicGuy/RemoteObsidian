import os
import sys

def main():
    # 1. Determine root directory relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    
    # Check execution mode
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == '--execute':
        dry_run = False
        
    print("=" * 60)
    print("Vault Markdown Cleanup Script")
    print(f"Directory: {root_dir}")
    print(f"Mode: {'DRY RUN (No files will be deleted)' if dry_run else 'EXECUTE (Files WILL BE DELETED)'}")
    print("=" * 60)
    
    # 2. Scan the root directory for markdown files
    md_files = []
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        # Scan only .md files at the main path (skip directories)
        if os.path.isfile(item_path) and item.lower().endswith('.md'):
            # Skip special files like readme.md
            if item.lower() == 'readme.md':
                continue
            md_files.append(item)
            
    print(f"Scanning {len(md_files)} markdown files in the main folder...")
    print("-" * 60)
    
    # 3. Analyze content and identify short files
    files_to_delete = []
    
    for filename in sorted(md_files):
        file_path = os.path.join(root_dir, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            lines = content.splitlines()
            non_empty_lines = [l.strip() for l in lines if l.strip()]
            text_line_count = len(non_empty_lines)
            
            # Identify files with less than 5 lines of actual text
            if text_line_count < 5:
                # Get a brief preview of the content
                preview = " / ".join(non_empty_lines[:2])
                if len(preview) > 50:
                    preview = preview[:47] + "..."
                preview_str = f"Preview: '{preview}'" if preview else "Empty file"
                
                files_to_delete.append((filename, text_line_count, preview_str))
        except Exception as e:
            print(f"[WARNING] Failed to read '{filename}': {e}")
            
    # 4. Perform Deletions / Report
    deleted_count = 0
    for filename, line_count, preview in files_to_delete:
        file_path = os.path.join(root_dir, filename)
        if dry_run:
            print(f"[DRY RUN] Will delete: '{filename}' ({line_count} lines) | {preview}")
            deleted_count += 1
        else:
            try:
                os.remove(file_path)
                print(f"[DELETED] '{filename}' ({line_count} lines) | {preview}")
                deleted_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to delete '{filename}': {e}")
                
    print("-" * 60)
    if dry_run:
        print(f"Dry run complete. Found {deleted_count} files with less than 5 lines of text.")
        print("To execute these deletions, run: python utilities/file_mover.py --execute")
    else:
        print(f"Execution complete. Successfully deleted {deleted_count} files.")
    print("=" * 60)

if __name__ == "__main__":
    main()

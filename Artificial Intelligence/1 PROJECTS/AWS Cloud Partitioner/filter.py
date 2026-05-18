import re
import glob

def remove_details_tags():
    # Find all exam*.md files
    md_files = glob.glob('exam*.md')
    
    # Regex pattern to match <details>...</details> block including newlines
    pattern = re.compile(r'[ \t]*<details.*?>.*?</details>\n?', re.DOTALL)
    
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the detailed tags with an empty string
        new_content = pattern.sub('', content)
        
        # Write back if changes were made
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed <details> tags from {file_path}")

if __name__ == '__main__':
    remove_details_tags()

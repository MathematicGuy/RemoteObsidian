import os
import shutil
from pathlib import Path

def move_images(source_dir=".", target_dir_name="images"):
    # Common image file extensions (case-insensitive)
    IMAGE_EXTENSIONS = {
        '.png', '.jpg', '.jpeg', '.gif', '.bmp', 
        '.tiff', '.webp', '.svg', '.heic', '.ico'
    }
    
    source_path = Path(source_dir).resolve()
    target_path = source_path / target_dir_name
    
    # Create the target images directory if it doesn't exist
    if not target_path.exists():
        print(f"Creating directory: {target_path}")
        target_path.mkdir(parents=True, exist_ok=True)
    
    moved_count = 0
    
    print(f"Scanning '{source_path}' for image files...")
    
    # Iterate through all items in the source directory
    for item in source_path.iterdir():
        # Only process files, skip directories
        if item.is_file():
            # Check if the file suffix matches any in our list (case-insensitive)
            if item.suffix.lower() in IMAGE_EXTENSIONS:
                destination = target_path / item.name
                
                # Check if a file with the same name already exists in target folder
                if destination.exists():
                    print(f"Warning: '{item.name}' already exists in target folder. Renaming to avoid overwriting...")
                    # Generate a unique name
                    base = item.stem
                    ext = item.suffix
                    counter = 1
                    while destination.exists():
                        destination = target_path / f"{base}_{counter}{ext}"
                        counter += 1
                
                try:
                    shutil.move(str(item), str(destination))
                    print(f"Moved: {item.name} -> {destination.name}")
                    moved_count += 1
                except Exception as e:
                    print(f"Error moving {item.name}: {e}")
                    
    print(f"\nTask complete! Successfully moved {moved_count} image file(s) into '{target_path.name}'.")

if __name__ == "__main__":
    # Move images in the directory where the script is run
    move_images()

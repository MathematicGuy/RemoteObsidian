"""
heuristic_rules.py — Custom classification and organization pipeline.
Completely replaced old keywords and rules, importing and running:
- image_mover.py
- file_mover.py
- heuristic_organizer.py
in sequence as the new rules.
"""

import sys
import subprocess
from pathlib import Path
from typing import Optional

# Ensure scripts directory is in sys.path
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

# Import the three modules as requested
import image_mover
import file_mover
import heuristic_organizer

# Global flag to ensure the pipeline runs only once per execution
_has_run = False

def run_pipeline():
    global _has_run
    if _has_run:
        return
    _has_run = True

    vault_root = SCRIPT_DIR.parent.parent.parent.parent
    utils_dir = vault_root / "Artificial_Intelligence" / "ultilities"

    print("\n" + "="*60, file=sys.stderr)
    print("STARTING CUSTOM HEURISTIC PIPELINE IN SEQUENCE", file=sys.stderr)
    print("="*60, file=sys.stderr)

    # 1. Run image_mover.py
    print("\n--- [1/3] Running image_mover.py ---", file=sys.stderr)
    try:
        subprocess.run([sys.executable, "image_mover.py"], cwd=str(utils_dir), check=True)
    except Exception as e:
        print(f"[ERROR] Failed to run image_mover.py: {e}", file=sys.stderr)

    # 2. Run file_mover.py --execute
    print("\n--- [2/3] Running file_mover.py --execute ---", file=sys.stderr)
    try:
        subprocess.run([sys.executable, "file_mover.py", "--execute"], cwd=str(utils_dir), check=True)
    except Exception as e:
        print(f"[ERROR] Failed to run file_mover.py: {e}", file=sys.stderr)

    # 3. Run heuristic_organizer.py --execute
    print("\n--- [3/3] Running heuristic_organizer.py --execute ---", file=sys.stderr)
    try:
        subprocess.run([sys.executable, "heuristic_organizer.py", "--execute"], cwd=str(utils_dir), check=True)
    except Exception as e:
        print(f"[ERROR] Failed to run heuristic_organizer.py: {e}", file=sys.stderr)

    print("\n" + "="*60, file=sys.stderr)
    print("CUSTOM HEURISTIC PIPELINE COMPLETED SUCCESSFULLY", file=sys.stderr)
    print("="*60 + "\n", file=sys.stderr)


def match_heuristic(filename: str, content: Optional[str] = None) -> Optional[str]:
    """Runs the three-stage organization pipeline in sequence on the first call,
    then delegates classification to heuristic_organizer.py.
    """
    run_pipeline()
    return heuristic_organizer.match_heuristic(filename)


def get_existing_categories() -> list[str]:
    """Returns the categories recognized by heuristic_organizer.py."""
    run_pipeline()
    return list(heuristic_organizer.MAPPINGS.keys())

if __name__ == '__main__':
    get_existing_categories()
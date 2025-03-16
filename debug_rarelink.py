import sys
from pathlib import Path

# Current file location
print(f"Current file: {Path(__file__).resolve()}")

# Project root detection
current_file = Path(__file__).resolve()
project_root = current_file.parent
while project_root.name and not (project_root / "pyproject.toml").exists():
    project_root = project_root.parent
print(f"Detected project root: {project_root}")

# Expected RareLink path
rarelink_path = project_root / "submodules" / "rarelink" / "src"
print(f"Expected RareLink path: {rarelink_path}")
print(f"This path exists: {rarelink_path.exists()}")

# Check what's in the directory
if rarelink_path.exists():
    print("Contents of the RareLink src directory:")
    for item in rarelink_path.iterdir():
        print(f"  - {item.name}")
        if item.name == "rarelink" and item.is_dir():
            print("    Contents of rarelink package:")
            for subitem in item.iterdir():
                print(f"      - {subitem.name}")

# Add RareLink to Python path
if rarelink_path.exists():
    rarelink_path_str = str(rarelink_path)
    if rarelink_path_str not in sys.path:
        sys.path.insert(0, rarelink_path_str)  # Insert at beginning for priority
        print(f"Added to sys.path: {rarelink_path_str}")
    else:
        print(f"Already in sys.path: {rarelink_path_str}")
else:
    print("RareLink path doesn't exist!")

# Print current sys.path
print("\nCurrent sys.path:")
for p in sys.path:
    print(f"  - {p}")

# Try importing
try:
    import rarelink
    print(f"\nSuccessfully imported rarelink, version: {getattr(rarelink, '__version__', 'unknown')}")
    print(f"rarelink.__file__: {rarelink.__file__}")
    
    try:
        from rarelink.utils import processing
        print("Successfully imported rarelink.utils.processing")
    except ImportError as e:
        print(f"Failed to import rarelink.utils.processing: {e}")

    try:
        from rarelink.utils.processor import DataProcessor
        print("Successfully imported DataProcessor")
    except ImportError as e:
        print(f"Failed to import DataProcessor: {e}")

except ImportError as e:
    print(f"\nFailed to import rarelink: {e}")
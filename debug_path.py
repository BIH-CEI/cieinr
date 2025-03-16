# debug_path_v2.py
import sys
import os
from pathlib import Path
import importlib
import pkgutil

print("Python sys.path:")
for p in sys.path:
    print(f"  - {p}")

print("\nAttempting imports:")
try:
    import rarelink
    print(f"Found rarelink at: {rarelink.__file__}")
    print(f"rarelink version: {getattr(rarelink, '__version__', 'unknown')}")
    
    # List all submodules
    print("\nFound rarelink submodules:")
    package = rarelink
    for _, name, ispkg in pkgutil.iter_modules(package.__path__, package.__name__ + '.'):
        print(f"  - {name} ({'package' if ispkg else 'module'})")
        
        # If it's a package, try to list its contents too
        if ispkg:
            try:
                subpackage = importlib.import_module(name)
                for _, subname, subispkg in pkgutil.iter_modules(subpackage.__path__, subpackage.__name__ + '.'):
                    print(f"    - {subname} ({'package' if subispkg else 'module'})")
            except ImportError as e:
                print(f"    Error importing {name}: {e}")
    
    # Try importing specific modules
    modules_to_test = [
        "rarelink.cli", 
        "rarelink.cli.utils", 
        "rarelink.utils",
        "rarelink.utils.processor",
        "rarelink.phenopackets"
    ]
    
    print("\nTesting specific imports:")
    for module_name in modules_to_test:
        try:
            module = importlib.import_module(module_name)
            print(f"✓ Successfully imported {module_name} from {module.__file__}")
        except ImportError as e:
            print(f"✗ Failed to import {module_name}: {e}")
            
except ImportError as e:
    print(f"Failed to import rarelink: {e}")

print("\nContents of site-packages/rarelink directory:")
# Try to find rarelink in site-packages
import site
for site_pkg in site.getsitepackages():
    rarelink_path = Path(site_pkg) / "rarelink"
    if rarelink_path.exists():
        print(f"Found at {rarelink_path}")
        # List top-level contents
        for item in rarelink_path.iterdir():
            print(f"  - {item.name}")
#!/usr/bin/env python3
"""
Version bumping script for CIEINR.

Usage:
    python scripts/bump_version.py [major|minor|patch]

Example:
    python scripts/bump_version.py patch  # Bumps from 1.0.0 to 1.0.1
    python scripts/bump_version.py minor  # Bumps from 1.0.0 to 1.1.0
    python scripts/bump_version.py major  # Bumps from 1.0.0 to 2.0.0
"""
import argparse
import re
import sys
from pathlib import Path

# Path to version file
VERSION_FILE = Path(__file__).parents[1] / "src" / "cieinr" / "_version.py"

def get_current_version():
    """Extract the current version from the _version.py file."""
    version_text = VERSION_FILE.read_text()
    version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', version_text)
    if not version_match:
        print("Error: Could not find __version__ in _version.py")
        sys.exit(1)
    
    return version_match.group(1)

def bump_version(current_version, bump_type):
    """
    Bump a semver version based on the specified bump_type.
    
    Args:
        current_version: Current version string (e.g., "1.0.0")
        bump_type: Type of bump ("major", "minor", or "patch")
        
    Returns:
        New version string
    """
    try:
        # Parse current version
        major, minor, patch = map(int, current_version.split('.'))
        
        # Bump appropriate part
        if bump_type == "major":
            major += 1
            minor = 0
            patch = 0
        elif bump_type == "minor":
            minor += 1
            patch = 0
        elif bump_type == "patch":
            patch += 1
        else:
            print(f"Error: Unknown bump type '{bump_type}'")
            sys.exit(1)
            
        # Create new version string
        return f"{major}.{minor}.{patch}"
    
    except ValueError:
        print(f"Error: Current version '{current_version}' is not a valid semver string")
        sys.exit(1)

def update_version_file(new_version):
    """Update the version file with the new version."""
    content = VERSION_FILE.read_text()
    updated_content = re.sub(
        r'__version__\s*=\s*["\']([^"\']+)["\']',
        f'__version__ = "{new_version}"',
        content
    )
    
    VERSION_FILE.write_text(updated_content)

def main():
    parser = argparse.ArgumentParser(description="Bump the CIEINR package version")
    parser.add_argument(
        "bump_type", 
        choices=["major", "minor", "patch"],
        help="The type of version bump to perform"
    )
    args = parser.parse_args()
    
    current_version = get_current_version()
    new_version = bump_version(current_version, args.bump_type)
    
    # Update the version file
    update_version_file(new_version)
    
    print(f"Updated version from {current_version} to {new_version}")
    
    # Print Git commands for convenience
    print("\nTo commit this change, run:")
    print(f"git add {VERSION_FILE}")
    print(f'git commit -m "Bump version to {new_version}"')
    print("git tag -a v{new_version} -m \"Version {new_version}\"")
    
if __name__ == "__main__":
    main()
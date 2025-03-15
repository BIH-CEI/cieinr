#!/usr/bin/env python3
"""
Script to generate Python classes from LinkML schemas.

This script handles the generation of Python classes from LinkML schemas
while working around compatibility issues with Python 3.13.
"""

import os
import sys
from pathlib import Path

# Schema input and output paths
SCHEMA_DIR = Path("src/cieinr/v1_0_0/linkml_schemas")
OUTPUT_DIR = Path("src/cieinr/v1_0_0/python_schemas")

def generate_schema_classes():
    """Generate Python classes from all LinkML schema files."""
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Process all schema YAML files
    schema_files = list(SCHEMA_DIR.glob("*.yaml"))
    print(f"Found {len(schema_files)} schema files")
    
    for schema_file in schema_files:
        output_file = OUTPUT_DIR / f"{schema_file.stem}.py"
        print(f"Processing {schema_file.name} -> {output_file.name}")
        
        # Use the command-line approach instead of Python modules
        cmd = f"gen-python {schema_file} > {output_file}"
        
        # Run the command directly
        exit_code = os.system(cmd)
        
        # Check if generation succeeded
        if output_file.exists():
            print(f"Successfully generated {output_file}")
        else:
            print(f"Failed to generate {output_file}")

if __name__ == "__main__":
    generate_schema_classes()
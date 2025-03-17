#!/usr/bin/env python
"""
Script to convert REDCap data to LinkML format.
Usage: python redcap_to_linkml_script.py

The script automatically looks for redcap_data.json in the res/ directory
and outputs to patient_link.json in the same directory.
"""

import sys
import os
from pathlib import Path
from cieinr.utils.processing.schemas.redcap_to_linkml import redcap_to_linkml
from cieinr.v1_0_0.mappings.redcap_to_linkml.registry import MAPPING_FUNCTIONS

def main():
    # Create res directory if it doesn't exist
    res_dir = "res"
    if not os.path.exists(res_dir):
        print(f"Creating {res_dir}/ directory...")
        os.makedirs(res_dir)
    
    # Define input and output file paths
    input_file = os.path.join(res_dir, "redcap_data.json")
    output_file = os.path.join(res_dir, "patient_linkml.json")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        print(f"Please place your REDCap data in 'res/redcap_data.json'.")
        sys.exit(1)
    
    print(f"Using input file: {input_file}")
    print(f"Output will be saved to: {output_file}")
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        sys.exit(1)
    
    # Convert REDCap data to LinkML format
    try:
        transformed_data = redcap_to_linkml(
            records=input_file,
            output_file=output_file,
            mapping_functions=MAPPING_FUNCTIONS
        )
        print(f"Successfully transformed {len(transformed_data)} records.")
        print(f"Output saved to: {output_file}")
    except Exception as e:
        print(f"Error during transformation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
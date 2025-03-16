#!/usr/bin/env python3
"""
Modular end-to-end workflow script for CIEINR.

This script demonstrates the entire workflow from:
1. REDCap API fetch to local records
2. REDCap records to LinkML format
3. LinkML format to Phenopackets

Using the modular architecture with CIEINR's implementation, which leverages 
functionality from the mapping_blocks and metadata modules.
"""

import argparse
import json
import os
from pathlib import Path
from datetime import datetime

# Configuration
from cieinr.config import Config

# REDCap to LinkML mappings
from cieinr.v1_0_0.mappings.redcap_to_linkml.registry import MAPPING_FUNCTIONS

# Pipeline components - simplified imports
from cieinr.utils import fetch_redcap_records, redcap_to_linkml, phenopackets_export

# Mapping definitions - directly imported from the phenopackets mapping modules
from cieinr.v1_0_0.mappings.phenopackets.mapping_blocks import (
    INDIVIDUAL_BLOCK,
    VITAL_STATUS_BLOCK,
    DISEASE_BLOCK,
    PHENOTYPIC_FEATURES_BLOCK,
    CIEINR_CODE_SYSTEMS
)
from cieinr.v1_0_0.mappings.phenopackets.metadata import generate_metadata

def run_workflow(
    output_dir=None,
    records_file=None,
    use_test_data=False,
    created_by=None,
    debug=False
):
    """
    Run the complete workflow.
    
    Args:
        output_dir: Output directory path
        records_file: Path to existing records file
        use_test_data: Whether to use test data
        created_by: Creator name for metadata
        debug: Whether to print debug information
        
    Returns:
        0 on success, 1 on error
    """
    # Setup file paths
    base_dir = Path(__file__).parent
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(output_dir) if output_dir else base_dir / "output" / timestamp
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        if records_file:
            # Use existing records file
            records_file = Path(records_file)
            if not records_file.exists():
                raise FileNotFoundError(f"Records file not found: {records_file}")
            
            print(f"Using existing records file: {records_file}")
            with open(records_file, "r") as f:
                records = json.load(f)
        else:
            # Fetch from REDCap API or use test data
            config = Config()
            try:
                config.validate()
            except ValueError as e:
                print(f"Error validating configuration: {e}")
                print("Please make sure your .env file contains REDCAP_URL and REDCAP_API_TOKEN")
                return 1
            
            api_url = config.get("REDCAP_URL")
            token = config.get("REDCAP_API_TOKEN")
            project_id = config.get("REDCAP_PROJECT_ID")
            
            records_file = output_dir / "records.json"
            records = fetch_redcap_records(api_url, token, project_id, use_test_data=use_test_data)
            
            # Save the records for reference
            with open(records_file, "w") as outfile:
                json.dump(records, outfile, indent=2)
            print(f"Saved raw records to {records_file}")
        
        # Step 1: Convert REDCap records to LinkML format
        linkml_output = output_dir / "patient_linkml.json"
        linkml_data = redcap_to_linkml(records, linkml_output, MAPPING_FUNCTIONS)
        
        # Step 2: Convert LinkML format to Phenopackets
        phenopackets_dir = output_dir / "phenopackets"
        phenopackets_output = "all_phenopackets.json"
        
        # Also save to res directory for easy access
        res_dir = base_dir / "res" / "phenopackets"
        os.makedirs(res_dir, exist_ok=True)
        
        # Use CIEINR's phenopackets_export function which uses create_phenopacket internally
        phenopackets = phenopackets_export(
            linkml_data, 
            phenopackets_dir, 
            created_by=created_by,
            output_file=phenopackets_output,
            additional_output_dir=res_dir,
            debug=debug
        )
        
        # Also save LinkML data to res directory as well
        res_linkml_path = base_dir / "res" / "patient_linkml.json"
        with open(res_linkml_path, "w") as outfile:
            json.dump(linkml_data, outfile, indent=2)
        
        print("\nWorkflow completed successfully!")
        print(f"Records: {records_file}")
        print(f"LinkML data: {linkml_output} (also at {res_linkml_path})")
        print(f"Phenopackets: {phenopackets_dir}")
        print(f"All phenopackets: {phenopackets_dir / phenopackets_output}")
        print(f"Individual phenopackets are also saved in {res_dir}")
        
    except Exception as e:
        print(f"Error in workflow: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

def main():
    """
    Parse arguments and run the workflow.
    """
    parser = argparse.ArgumentParser(description="CIEINR modular workflow using phenopackets mapping blocks")
    parser.add_argument("--test", action="store_true", help="Use test data instead of REDCap API")
    parser.add_argument("--records-file", help="Use existing records file instead of fetching from REDCap")
    parser.add_argument("--output-dir", help="Output directory (defaults to ./output/timestamp)")
    parser.add_argument("--created-by", help="Name to use in metadata")
    parser.add_argument("--debug", action="store_true", help="Print debug information")
    args = parser.parse_args()
    
    return run_workflow(
        output_dir=args.output_dir,
        records_file=args.records_file,
        use_test_data=args.test,
        created_by=args.created_by,
        debug=args.debug
    )

if __name__ == "__main__":
    exit(main())
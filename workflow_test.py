#!/usr/bin/env python3
"""
End-to-end workflow test for CIEINR.

This script demonstrates the entire workflow from:
1. REDCap records to LinkML format
2. LinkML format to Phenopackets
"""
import json
import os
from pathlib import Path
from datetime import datetime

# Import CIEINR functions directly to bypass CLI
from cieinr.v1.0.0.redcap_to_linkml.registry import MAPPING_FUNCTIONS

def redcap_to_linkml(flat_data_file, output_file):
    """
    Transform REDCap records to LinkML format.
    """
    print(f"Transforming REDCap data from {flat_data_file} to LinkML format...")
    
    # Load flat data from JSON
    with open(flat_data_file, "r") as infile:
        flat_data = json.load(infile)

    # Process using the mapping functions
    from collections import defaultdict
    transformed_data = []

    # Group data by record_id
    records = defaultdict(list)
    for record in flat_data:
        records[record["record_id"]].append(record)

    # Process records
    for record_id, entries in records.items():
        # Initialize the record structure with non-repeating sections first
        record = {
            "record_id": record_id,
        }

        # Add non-repeating data
        for entry in entries:
            if entry.get("redcap_repeat_instrument", "") == "":
                for schema_name, config in MAPPING_FUNCTIONS.items():
                    if not config["is_repeating"] and schema_name not in record:
                        record[schema_name] = config["mapper"](entry)

        # Add repeating elements
        record["repeated_elements"] = []
        for entry in entries:
            if entry.get("redcap_repeat_instrument", "") != "":
                repeated_instrument = entry["redcap_repeat_instrument"]
                repeated_element = {
                    "redcap_repeat_instrument": repeated_instrument,
                    "redcap_repeat_instance": int(entry["redcap_repeat_instance"]),
                }

                # Find schema name and apply the mapper
                for schema_name, config in MAPPING_FUNCTIONS.items():
                    if config["is_repeating"] and repeated_instrument == schema_name:
                        repeated_element[schema_name] = config["mapper"](entry)

                record["repeated_elements"].append(repeated_element)

        transformed_data.append(record)

    # Save the transformed data
    with open(output_file, "w") as outfile:
        json.dump(transformed_data, outfile, indent=2)

    print(f"Transformed data has been saved to {output_file}")
    return transformed_data

def phenopackets_export(linkml_data, output_dir, output_file=None):
    """
    Transform LinkML data to Phenopackets.
    """
    from cieinr.cli.commands.phenopackets import transform_to_phenopacket
    
    print(f"Converting LinkML data to Phenopackets...")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    phenopackets = []
    
    # Transform each record to a phenopacket
    for record in linkml_data:
        try:
            phenopacket = transform_to_phenopacket(record)
            phenopackets.append(phenopacket)
            
            # Save individual phenopacket
            record_id = record.get("record_id", "unknown")
            record_output_path = os.path.join(output_dir, f"{record_id}.json")
            
            with open(record_output_path, "w") as outfile:
                json.dump(phenopacket, outfile, indent=2)
                
            print(f"Created phenopacket for record {record_id}")
            
        except Exception as e:
            print(f"Error creating phenopacket for record {record.get('record_id', 'unknown')}: {e}")
    
    # Save all phenopackets to a single file if requested
    if output_file:
        all_output_path = os.path.join(output_dir, output_file)
        with open(all_output_path, "w") as outfile:
            json.dump(phenopackets, outfile, indent=2)
        print(f"Saved all phenopackets to {all_output_path}")
    
    print(f"Exported {len(phenopackets)} phenopackets to {output_dir}")
    return phenopackets

def main():
    """
    Run the complete workflow.
    """
    # Setup file paths
    base_dir = Path(__file__).parent
    output_dir = base_dir / "output" / datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Find the test patient data
        test_file = base_dir / "res" / "test_patient.json"
        if not test_file.exists():
            raise FileNotFoundError(f"Test patient file not found at {test_file}")
        
        # Step 1: Convert REDCap records to LinkML format
        linkml_output = output_dir / "test_patient_linkml.json"
        linkml_data = redcap_to_linkml(test_file, linkml_output)
        
        # Step 2: Convert LinkML format to Phenopackets
        phenopackets_dir = output_dir / "phenopackets"
        phenopackets_output = "all_phenopackets.json"
        phenopackets = phenopackets_export(linkml_data, phenopackets_dir, phenopackets_output)
        
        print("\nWorkflow completed successfully!")
        print(f"LinkML data: {linkml_output}")
        print(f"Phenopackets: {phenopackets_dir}")
        print(f"All phenopackets: {phenopackets_dir / phenopackets_output}")
        
    except Exception as e:
        print(f"Error in workflow: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
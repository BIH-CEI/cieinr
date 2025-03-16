"""Functions to transform REDCap data to LinkML format."""

import json
from collections import defaultdict
from pathlib import Path
from typing import Dict, Any, List, Union

def redcap_to_linkml(
    records: Union[List[Dict[str, Any]], str, Path], 
    output_file: Union[str, Path], 
    mapping_functions: Dict[str, Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Transforms REDCap records to LinkML format.
    
    Args:
        records: List of REDCap records or path to JSON file containing records
        output_file: Path to save the transformed data
        mapping_functions: Dictionary of mapping functions for each schema
        
    Returns:
        List of transformed data in LinkML format
    """
    # Load records if file path provided
    if isinstance(records, (str, Path)):
        with open(records, "r") as infile:
            records = json.load(infile)
    
    print("Transforming REDCap data to LinkML format...")
    
    # Process using the mapping functions
    transformed_data = []

    # Group data by record_id
    record_groups = defaultdict(list)
    for record in records:
        record_groups[record["record_id"]].append(record)

    # Process records
    for record_id, entries in record_groups.items():
        # Initialize the record structure with non-repeating sections first
        record = {
            "record_id": record_id,
        }

        # Add non-repeating data
        for entry in entries:
            if entry.get("redcap_repeat_instrument", "") == "":
                for schema_name, config in mapping_functions.items():
                    if not config["is_repeating"] and schema_name not in record:
                        try:
                            record[schema_name] = config["mapper"](entry)
                        except Exception as e:
                            print(f"Error mapping {schema_name}: {e}")
                            record[schema_name] = {}

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
                for schema_name, config in mapping_functions.items():
                    if config["is_repeating"] and repeated_instrument == schema_name:
                        try:
                            repeated_element[schema_name] = config["mapper"](entry)
                        except Exception as e:
                            print(f"Error mapping {schema_name}: {e}")
                            repeated_element[schema_name] = {}

                record["repeated_elements"].append(repeated_element)

        transformed_data.append(record)

    # Save the transformed data
    with open(output_file, "w") as outfile:
        json.dump(transformed_data, outfile, indent=2)

    print(f"Transformed data has been saved to {output_file}")
    return transformed_data
"""
CIEINR REDCap to LinkML Mapper

This module defines mapping functions for transforming REDCap data into 
the simplified CIEINR LinkML schema for Phenopackets export.

Each mapping function corresponds to a specific schema in the simplified CIEINR model.
"""

import json
from collections import defaultdict
from typing import Dict, List, Any, Optional

# Field mappings for basic_form
BASIC_FORM_FIELDS = {
    "iei_deficiency_basic": "iei_deficiency_basic",
    "basic_form_complete": "basic_form_complete"
}

# Field mappings for patient_demographics_initial_form
DEMOGRAPHICS_INITIAL_FIELDS = {
    "snomedct_184099003": "snomedct_184099003",
    "snomedct_432213005": "snomedct_432213005",
    "snomedct_298059007": "snomedct_298059007",
    "patient_demographics_initial_form_complete": "patient_demographics_initial_form_complete"
}

# Field mappings for infections_initial_form
INFECTIONS_INITIAL_FIELDS = {
    "type_of_infection": "type_of_infection",
    "snomedct_61274003": "snomedct_61274003",
    "snomedct_21483005": "snomedct_21483005",
    "snomedct_81745001": "snomedct_81745001",
    "snomedct_385383008": "snomedct_385383008",
    "snomedct_127856007": "snomedct_127856007",
    "snomedct_110522009": "snomedct_110522009",
    "snomedct_20139000": "snomedct_20139000",
    "snomedct_303699009": "snomedct_303699009",
    "snomedct_21514008": "snomedct_21514008",
    "snomedct_31099001": "snomedct_31099001",
    "infection_severity": "infection_severity",
    "infection_temp_pattern": "infection_temp_pattern",
    "infection_times_obseverd": "infection_times_obseverd",
    "infections_initial_form_complete": "infections_initial_form_complete"
}

def map_entry(entry: Dict[str, Any], field_mappings: Dict[str, str]) -> Dict[str, Any]:
    """
    Maps a single REDCap entry to the target schema based on field mappings.
    
    Args:
        entry: A dictionary containing REDCap field data
        field_mappings: A dictionary mapping from REDCap fields to schema fields
        
    Returns:
        A dictionary containing only the mapped fields from the entry
    """
    result = {}
    for redcap_field, schema_field in field_mappings.items():
        if redcap_field in entry and entry[redcap_field] not in ("", None):
            result[schema_field] = entry[redcap_field]
    return result

def map_basic_form(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Maps REDCap data to the basic_form schema."""
    return map_entry(entry, BASIC_FORM_FIELDS)
    
def map_demographics_initial(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Maps REDCap data to the patient_demographics_initial_form schema."""
    return map_entry(entry, DEMOGRAPHICS_INITIAL_FIELDS)
    
def map_infections_initial(entry: Dict[str, Any]) -> Dict[str, Any]:
    """Maps REDCap data to the infections_initial_form schema."""
    return map_entry(entry, INFECTIONS_INITIAL_FIELDS)

# Registry of mapping functions for each schema
MAPPING_FUNCTIONS = {
    "basic_form": {
        "mapper": map_basic_form,
        "is_repeating": False
    },
    "patient_demographics_initial_form": {
        "mapper": map_demographics_initial,
        "is_repeating": False
    },
    "infections_initial_form": {
        "mapper": map_infections_initial,
        "is_repeating": True
    }
}

def redcap_to_cieinr_linkml(flat_data_file: str, output_file: str) -> None:
    """
    Transforms REDCap data into the simplified CIEINR LinkML schema for Phenopackets export.
    
    Args:
        flat_data_file: Path to the input REDCap JSON data file
        output_file: Path to the output transformed JSON data file
    """
    # Load flat data from JSON
    with open(flat_data_file, "r") as infile:
        flat_data = json.load(infile)

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
                # Process basic_form data
                if entry.get("basic_form_complete") is not None:
                    basic_form_data = map_basic_form(entry)
                    if basic_form_data:
                        record["basic_form"] = basic_form_data
                
                # Process patient_demographics_initial_form data
                if entry.get("patient_demographics_initial_form_complete") is not None:
                    demographics_data = map_demographics_initial(entry)
                    if demographics_data:
                        record["patient_demographics_initial"] = demographics_data

        # Add repeating elements
        record["repeated_elements"] = []
        for entry in entries:
            repeat_instrument = entry.get("redcap_repeat_instrument", "")
            if repeat_instrument == "infections_initial_form":
                repeat_instance = entry.get("redcap_repeat_instance", "")
                if repeat_instance:
                    repeat_instance = int(repeat_instance)
                    
                    repeated_element = {
                        "redcap_repeat_instrument": repeat_instrument,
                        "redcap_repeat_instance": repeat_instance,
                    }
                    
                    infections_data = map_infections_initial(entry)
                    if infections_data:
                        repeated_element["infections_initial"] = infections_data
                        record["repeated_elements"].append(repeated_element)

        # Only add records that have data we want to export
        if "basic_form" in record or "patient_demographics_initial" in record or record["repeated_elements"]:
            # Remove empty repeated_elements array
            if not record["repeated_elements"]:
                del record["repeated_elements"]
                
            transformed_data.append(record)

    # Save the transformed data
    with open(output_file, "w") as outfile:
        json.dump(transformed_data, outfile, indent=2)

    print(f"Transformed data has been saved to {output_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Transform REDCap data to simplified CIEINR schema for Phenopackets export.")
    parser.add_argument("flat_data_file", 
                        help="Path to the input REDCap JSON data file")
    parser.add_argument("output_file", 
                        help="Path to the output transformed JSON data file")

    args = parser.parse_args()
    redcap_to_cieinr_linkml(args.flat_data_file, args.output_file)
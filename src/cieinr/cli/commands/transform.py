"""
Transform commands for converting REDCap data to LinkML format and other transformations.
"""
import typer
import json
from pathlib import Path
from typing import Optional

app = typer.Typer(help="Transform commands for CIEINR")

@app.command("redcap-to-linkml")
def redcap_to_linkml(
    input_file: str = typer.Argument(..., help="Path to the input flat JSON data file"),
    output_file: str = typer.Argument(..., help="Path to the output transformed JSON data file")
):
    """
    Transforms flat REDCap data into structured JSON format compatible with the LinkML schema.
    """
    from cieinr.v1_0_0.redcap_to_linkml.registry import MAPPING_FUNCTIONS
    
    # Load flat data from JSON
    with open(input_file, "r") as infile:
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

if __name__ == "__main__":
    app()
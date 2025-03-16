"""Module for transforming LinkML data to Phenopackets format."""

import json
import os
import uuid
import logging
from pathlib import Path
from typing import Dict, Any, List, Union, Optional
# Create a simple DataProcessor class
from rarelink.utils.processor import DataProcessor

# class DataProcessor:
#     def __init__(self, mapping_config=None):
#         self.mapping_config = mapping_config or {}
        
#     def get_field(self, data, field_name):
#         field_path = self.mapping_config.get(field_name, "")
#         if not field_path:
#             return None
        
#         parts = field_path.split(".")
#         current = data
#         for part in parts:
#             if isinstance(current, dict) and part in current:
#                 current = current[part]
#             else:
#                 return None
#         return current

# Import mapping blocks
from cieinr.v1_0_0.mappings.phenopackets.mapping_blocks import (
    INDIVIDUAL_BLOCK,
 #   VITAL_STATUS_BLOCK,
    DISEASE_BLOCK,
  #  PHENOTYPIC_FEATURES_BLOCK,
    #CIEINR_CODE_SYSTEMS,
   # get_mapping_by_name
)

# Import metadata generator
from cieinr.v1_0_0.mappings.phenopackets.metadata import generate_metadata

logger = logging.getLogger(__name__)

def create_phenopacket(data: Dict[str, Any], created_by: Optional[str] = None, debug: bool = False) -> Dict[str, Any]:
    """
    Create a Phenopacket for an individual.
    
    Args:
        data: The LinkML record data
        created_by: Optional name of the creator for metadata
        debug: Whether to print debug information
        
    Returns:
        Phenopacket dictionary
    """
    try:
        # Print debugging information if enabled
        if debug:
            print("DEBUG: Input data structure:")
            for key, value in data.items():
                if isinstance(value, dict):
                    print(f"  {key}: {list(value.keys())}")
                elif isinstance(value, list):
                    print(f"  {key}: list with {len(value)} items")
                else:
                    print(f"  {key}: {value}")
                                
        # Initialize processors for each block
        individual_processor = DataProcessor(mapping_config=INDIVIDUAL_BLOCK)
        disease_processor = DataProcessor(mapping_config=DISEASE_BLOCK)
        
        # Extract key information for debugging
        if debug:
            record_id = data.get('record_id', '')
            dob = individual_processor.get_field(data, "date_of_birth_field")
            disease_code = disease_processor.get_field(data, "term_field")
            print(f"DEBUG: Record ID: {record_id}")
            print(f"DEBUG: Date of birth field: {dob}")
            print(f"DEBUG: Disease code field: {disease_code}")
                    
        # Create phenopacket
        phenopacket = {
            "id": data.get("record_id", f"phenopacket:{uuid.uuid4()}"),
            "subject": {"id": data.get("record_id", f"PATIENT:{uuid.uuid4()}")},
            "diseases": [],
            "phenotypicFeatures": [],
            "metadata": generate_metadata(created_by)
        }
        
        # Try to extract disease data from basic form
        basic_form = data.get("basic_form", {})
        disease_code = basic_form.get("iei_deficiency_basic", "")
        
        if disease_code:
            # Try to get a term from the enum
            try:
                from cieinr.v1_0_0.python_schemas.form_1_basic import IUIS2024MONDOEnum
                enum_value = getattr(IUIS2024MONDOEnum, disease_code, None)
                
                if enum_value and hasattr(enum_value, 'description') and hasattr(enum_value, 'meaning'):
                    mondo_id = str(enum_value.meaning)
                    if 'MONDO_' in mondo_id:
                        mondo_id = 'MONDO:' + mondo_id.split('MONDO_')[1]
                    
                    phenopacket["diseases"].append({
                        "term": {
                            "id": mondo_id,
                            "label": enum_value.description
                        },
                        "clinicalStatus": {
                            "id": "active",
                            "label": "Active"
                        }
                    })
                    
                    if debug:
                        print(f"DEBUG: Added disease from enum: {mondo_id}")
            except Exception as e:
                if debug:
                    print(f"DEBUG: Could not add disease term: {e}")
        
        # Add demographics information if available
        demographics = data.get("patient_demographics_initial_form", {})
        if demographics:
            birth_date = demographics.get("snomedct_184099003", "")
            if birth_date:
                phenopacket["subject"]["dateOfBirth"] = birth_date
        
        if debug:
            print(f"DEBUG: Created phenopacket with ID: {phenopacket['id']}")
            
        return phenopacket
        
    except Exception as e:
        logger.error(f"Error creating phenopacket: {e}")
        if debug:
            import traceback
            traceback.print_exc()
        raise

def phenopackets_export(
    linkml_data: Union[List[Dict[str, Any]], str, Path],
    output_dir: Union[str, Path],
    created_by: Optional[str] = None,
    output_file: Optional[str] = None,
    additional_output_dir: Optional[Union[str, Path]] = None,
    debug: bool = False
) -> List[Dict[str, Any]]:
    """
    Transform LinkML data to Phenopackets and save to files.
    
    Args:
        linkml_data: List of LinkML records or path to JSON file
        output_dir: Directory to save the Phenopackets
        created_by: Optional name of the creator for metadata
        output_file: Optional name for the combined file of all phenopackets
        additional_output_dir: Optional additional directory to save phenopackets
        debug: Whether to print debug information
        
    Returns:
        List of Phenopacket dictionaries
    """
    print("Converting LinkML data to Phenopackets...")
    
    # Load linkml_data if it's a file path
    if isinstance(linkml_data, (str, Path)):
        with open(linkml_data, "r") as infile:
            linkml_data = json.load(infile)
    
    # Ensure output directories exist
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    if additional_output_dir:
        additional_output_dir = Path(additional_output_dir)
        additional_output_dir.mkdir(parents=True, exist_ok=True)
    
    phenopackets = []
    
    # Transform each record to a Phenopacket dictionary
    for record in linkml_data:
        try:
            if debug:
                print(f"\nProcessing record {record.get('record_id', 'unknown')}")
                
            # Create phenopacket for this record
            phenopacket = create_phenopacket(record, created_by, debug=debug)
            phenopackets.append(phenopacket)
            
            # Save individual phenopacket to output_dir
            record_id = record.get("record_id", "unknown")
            record_output_path = output_dir / f"{record_id}.json"
            
            with open(record_output_path, "w") as outfile:
                json.dump(phenopacket, outfile, indent=2)
                
            print(f"Created phenopacket for record {record_id}")
            
            # Also save to additional_output_dir if provided
            if additional_output_dir:
                additional_output_path = additional_output_dir / f"{record_id}_phenopacket.json"
                with open(additional_output_path, "w") as outfile:
                    json.dump(phenopacket, outfile, indent=2)
            
        except Exception as e:
            print(f"Error creating phenopacket for record {record.get('record_id', 'unknown')}: {e}")
            if debug:
                import traceback
                traceback.print_exc()
    
    # Save all phenopackets to a single file if requested
    if output_file and phenopackets:
        all_output_path = output_dir / output_file
        with open(all_output_path, "w") as outfile:
            json.dump(phenopackets, outfile, indent=2)
        print(f"Saved all phenopackets to {all_output_path}")
    
    print(f"Exported {len(phenopackets)} phenopackets to {output_dir}")
    return phenopackets
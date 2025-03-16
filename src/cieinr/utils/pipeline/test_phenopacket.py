"""Module for transforming LinkML data to Phenopackets format using RareLink."""

import json
import uuid
import logging
import sys
import os
from pathlib import Path
from typing import Dict, Any, List, Union, Optional
from datetime import datetime

# Setup path to find RareLink modules in submodules directory
base_dir = Path(__file__).parent.parent.parent.parent.parent
submodules_dir = base_dir / "submodules" / "rarelink" / "src"
if submodules_dir.exists():
    sys.path.insert(0, str(submodules_dir))

# Try to import RareLink's components
try:
    from rarelink.utils.processor.processor import DataProcessor
    from google.protobuf.json_format import MessageToDict
    # If these imports succeed, we'll try to import the phenopackets mapping functions later
    rarelink_utils_available = True
except ImportError:
    rarelink_utils_available = False
    # Simple fallback DataProcessor
    class DataProcessor:
        def __init__(self, mapping_config=None):
            self.mapping_config = mapping_config or {}
            
        def get_field(self, data, field_name):
            """Get a field value from nested data using mapping config."""
            field_path = self.mapping_config.get(field_name, "")
            if not field_path:
                return None
            
            parts = field_path.split(".")
            current = data
            for part in parts:
                if isinstance(current, dict) and part in current:
                    current = current[part]
                else:
                    return None
            return current
        
        def process_date(self, date_input):
            """Simple date processing."""
            if not date_input:
                return None
            return date_input
            
        def fetch_mapping_value(self, mapping_name, key, default=None):
            """Get a value from a named mapping."""
            from cieinr.v1_0_0.mappings.phenopackets.mapping_blocks import get_mapping_by_name
            try:
                mapping = get_mapping_by_name(mapping_name)
                return mapping.get(key, default)
            except KeyError:
                return default
        
        def process_code(self, code):
            """Process an ontology code, standardizing format if needed."""
            if not code:
                return None
                
            # Convert MONDO codes to proper format
            if code.startswith("mondo_"):
                parts = code.split("_")
                if len(parts) == 2:
                    return f"MONDO:{parts[1]}"
            
            return code
            
        def fetch_label(self, code, enum_class=None):
            """Get a label for a code using LinkML enums if available."""
            if not code:
                return None
                
            # For MONDO codes, try to get the label from the enum
            if code.startswith("mondo_"):
                try:
                    from cieinr.v1_0_0.python_schemas.form_1_basic import IUIS2024MONDOEnum
                    enum_value = getattr(IUIS2024MONDOEnum, code, None)
                    if enum_value and hasattr(enum_value, 'description'):
                        return enum_value.description
                except (ImportError, AttributeError):
                    pass
            
            # Default to the code itself as the label
            return code
            
        def convert_date_to_iso_age(self, event_date, birth_date):
            """Simple ISO age calculation placeholder."""
            return "P0Y"

# Import mappings from our project
from cieinr.v1_0_0.mappings.phenopackets.mapping_blocks import (
    INDIVIDUAL_BLOCK,
    VITAL_STATUS_BLOCK,
    DISEASE_BLOCK,
    PHENOTYPIC_FEATURES_BLOCK,
    CIEINR_CODE_SYSTEMS,
)
from cieinr.v1_0_0.mappings.phenopackets.metadata import generate_metadata

# Try to import RareLink's mapping functions
try:
    if rarelink_utils_available:
        from rarelink.phenopackets.mappings.map_individual import map_individual
        from rarelink.phenopackets.mappings.map_disease import map_diseases
        from rarelink.phenopackets.mappings.map_vital_status import map_vital_status
        from rarelink.phenopackets.mappings.map_metadata import map_metadata
        from phenopackets import Phenopacket
        rarelink_mappings_available = True
        print("RareLink phenopackets mapping functions are available")
    else:
        rarelink_mappings_available = False
except ImportError:
    rarelink_mappings_available = False
    print("RareLink phenopackets mapping functions are not available")

logger = logging.getLogger(__name__)

def create_phenopacket(data: Dict[str, Any], created_by: Optional[str] = None, debug: bool = False) -> Dict[str, Any]:
    """
    Create a Phenopacket for an individual using RareLink's mapping functions if available.
    
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
        vital_status_processor = DataProcessor(mapping_config=VITAL_STATUS_BLOCK)
        
        # Extract key information for debugging
        if debug:
            record_id = data.get('record_id', '')
            dob = individual_processor.get_field(data, "date_of_birth_field")
            disease_code = disease_processor.get_field(data, "term_field")
            print(f"DEBUG: Record ID: {record_id}")
            print(f"DEBUG: Date of birth field: {dob}")
            print(f"DEBUG: Disease code field: {disease_code}")
            
        # Try to use RareLink's mapping functions if available
        if rarelink_mappings_available:
            try:
                if debug:
                    print("DEBUG: Using RareLink's mapping functions")
                    
                # Extract date of birth first
                dob_field = individual_processor.get_field(data, "date_of_birth_field")
                
                # We need to modify our data structure for RareLink's expectations
                # It expects repeated_elements with an instrument "patient_status"
                # We'll create a synthetic structure that fits
                modified_data = data.copy()
                
                # Extract patient status data directly from demographics
                demographics = data.get("patient_demographics_initial_form", {})
                if demographics and "patient_status" not in modified_data.get("repeated_elements", []):
                    # Create a patient_status block in the format RareLink expects
                    patient_status_element = {
                        "redcap_repeat_instrument": "patient_demographics_initial_form",
                        "redcap_repeat_instance": 1,
                        "patient_status": demographics
                    }
                    
                    # Add to repeated elements
                    if "repeated_elements" not in modified_data:
                        modified_data["repeated_elements"] = []
                    modified_data["repeated_elements"].append(patient_status_element)
                
                # Map vital status (needs dob)
                try:
                    vital_status = map_vital_status(modified_data, vital_status_processor, dob_field)
                except Exception as e:
                    if debug:
                        print(f"DEBUG: Error mapping vital status: {e}")
                    vital_status = None
                
                # Map individual using RareLink's function
                individual = map_individual(data, individual_processor, vital_status)
                
                # We need to prepare the data for RareLink's disease mapper too
                # It expects a different structure with disease data in repeated_elements
                if "basic_form" in data:
                    # Create a disease element in the format RareLink expects
                    disease_element = {
                        "redcap_repeat_instrument": "basic_form",
                        "redcap_repeat_instance": 1,
                        "disease": data["basic_form"]
                    }
                    
                    # Add to repeated elements if not already present
                    if "repeated_elements" not in modified_data:
                        modified_data["repeated_elements"] = []
                    
                    modified_data["repeated_elements"].append(disease_element)
                
                if debug:
                    print("DEBUG: Modified data structure for RareLink:")
                    print(f"  Repeated elements: {len(modified_data.get('repeated_elements', []))}")
                
                # Map diseases using RareLink's function
                try:
                    diseases = map_diseases(modified_data, disease_processor, individual.date_of_birth)
                except Exception as e:
                    if debug:
                        print(f"DEBUG: Error mapping diseases: {e}")
                        import traceback
                        traceback.print_exc()
                    diseases = []
                
                # Map metadata
                metadata = map_metadata(created_by or "CIEINR", CIEINR_CODE_SYSTEMS)
                
                # Create the phenopacket protobuf object
                phenopacket_obj = Phenopacket(
                    id=data.get("record_id", f"phenopacket:{uuid.uuid4()}"),
                    subject=individual,
                    diseases=diseases,
                    meta_data=metadata
                )
                
                # Convert to dictionary
                phenopacket = MessageToDict(phenopacket_obj)
                
                # Post-process the disease terms to fix format issues
                if "diseases" in phenopacket:
                    for disease in phenopacket["diseases"]:
                        if "term" in disease and "id" in disease["term"]:
                            term_id = disease["term"]["id"]
                            # Fix MONDO format
                            if term_id.startswith("mondo_"):
                                # Use our Python schema to get the proper ID and label
                                try:
                                    from cieinr.v1_0_0.python_schemas.form_1_basic import IUIS2024MONDOEnum
                                    enum_value = getattr(IUIS2024MONDOEnum, term_id, None)
                                    
                                    if enum_value and hasattr(enum_value, 'description') and hasattr(enum_value, 'meaning'):
                                        mondo_id = str(enum_value.meaning)
                                        if 'MONDO_' in mondo_id:
                                            mondo_id = 'MONDO:' + mondo_id.split('MONDO_')[1]
                                        
                                        # Update the term
                                        disease["term"]["id"] = mondo_id
                                        disease["term"]["label"] = enum_value.description
                                        
                                        if debug:
                                            print(f"DEBUG: Post-processed disease ID: {mondo_id}")
                                except Exception as e:
                                    if debug:
                                        print(f"DEBUG: Could not post-process disease term: {e}")
                
                if debug:
                    print(f"DEBUG: Created phenopacket with RareLink functions: {phenopacket['id']}")
                
                return phenopacket
                
            except Exception as e:
                if debug:
                    print(f"DEBUG: RareLink mapping failed: {e}")
                    import traceback
                    traceback.print_exc()
                # Fall back to our implementation
        
        # Fallback implementation when RareLink is not available
        if debug:
            print("DEBUG: Using fallback phenopacket creation")
            
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
            print(f"DEBUG: Created phenopacket with fallback method: {phenopacket['id']}")
            
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
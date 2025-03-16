#!/usr/bin/env python
"""
CIEINR Phenopackets pipeline.

This module provides a simple, clean pipeline for exporting CIEINR data to Phenopackets
by leveraging RareLink's pipeline functions with minimal modifications.
"""

import json
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional

# Import phenopackets core models
from phenopackets import (
    Phenopacket, 
    Individual, 
    Disease, 
    VitalStatus, 
    OntologyClass, 
    TimeElement, 
    Age
)

# Import RareLink functionality
from rarelink.phenopackets import (
    write_phenopackets,
    validate_phenopackets
)
from rarelink.phenopackets.mappings import (
    map_individual as rarelink_map_individual
)
from rarelink.utils.processor import DataProcessor

# Import CIEINR specific mappings
from cieinr.v1_0_0.mappings.phenopackets import create_cieinr_phenopacket_mappings
from cieinr.v1_0_0.mappings.phenopackets.metadata import (
    map_cieinr_metadata,
    CIEINR_CODE_SYSTEMS_CONTAINER
)
from cieinr.v1_0_0.python_schemas.form_1_basic import IUIS2024MONDOEnum

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def extract_enum_labels(enum_class) -> Dict[str, str]:
    """
    Extract labels from a LinkML-generated enum class.
    
    Args:
        enum_class: A LinkML-generated EnumDefinitionImpl class
        
    Returns:
        Dictionary mapping enum codes to their human-readable descriptions
    """
    labels = {}
    
    # Get all class attributes
    for attr_name in dir(enum_class):
        # Skip special methods and private attributes
        if attr_name.startswith('_') or attr_name in ['_defn', '_addvals']:
            continue
        
        try:
            attr_value = getattr(enum_class, attr_name)
            
            # Check if it's a PermissibleValue
            if hasattr(attr_value, 'text') and hasattr(attr_value, 'description'):
                # Add to our labels dictionary
                labels[attr_value.text] = attr_value.description
        except Exception:
            # Skip any attributes that cause errors
            continue
            
    return labels

def map_cieinr_disease(record: Dict[str, Any]) -> Optional[Disease]:
    """
    Map CIEINR disease data to a Phenopacket Disease object.
    
    Args:
        record: The patient record
        
    Returns:
        Disease object if disease field is available, None otherwise
    """
    # Check if basic form and disease field exist
    if not record.get("basic_form", {}).get("iei_deficiency_basic"):
        return None
        
    disease_code = record["basic_form"]["iei_deficiency_basic"]
    
    # Ensure it's a MONDO code
    if not disease_code.startswith("mondo_"):
        return None
        
    # Format the MONDO ID
    mondo_id = f"MONDO:{disease_code.replace('mondo_', '')}"
    
    # Get labels from enum
    iuis_labels = extract_enum_labels(IUIS2024MONDOEnum)
    disease_label = iuis_labels.get(disease_code, disease_code)
    
    # Create and return Disease object
    return Disease(
        term=OntologyClass(
            id=mondo_id,
            label=disease_label
        )
    )

def calculate_age_at_encounter(dob: str, visit_date: str) -> Optional[TimeElement]:
    """
    Calculate age at last encounter from date of birth and visit date.
    
    Args:
        dob: Date of birth string in ISO format
        visit_date: Visit date string in ISO format
        
    Returns:
        TimeElement with age information, or None if calculation fails
    """
    try:
        # Parse dates
        dob_date = datetime.fromisoformat(dob.replace("Z", ""))
        
        try:
            visit_date_obj = datetime.fromisoformat(visit_date.replace("Z", ""))
        except ValueError:
            # Try alternate format
            visit_date_obj = datetime.strptime(visit_date, "%Y-%m-%d")
        
        # Calculate years
        years = visit_date_obj.year - dob_date.year
        if (visit_date_obj.month, visit_date_obj.day) < (dob_date.month, dob_date.day):
            years -= 1
        
        # Create and return TimeElement
        return TimeElement(
            age=Age(iso8601duration=f"P{years}Y0M")
        )
        
    except Exception as e:
        logger.warning(f"Could not calculate age: {e}")
        return None

def process_cieinr_phenopackets(
    input_data_path: Path, 
    output_dir: Path = None, 
    created_by: str = "CIEINR Data Team"
) -> List[Phenopacket]:
    """
    Process CIEINR LinkML data to phenopackets.
    
    Args:
        input_data_path: Path to the input LinkML JSON file
        output_dir: Directory to save phenopackets
        created_by: Creator name for metadata
        
    Returns:
        List of phenopackets
    """
    # Create output directory if needed
    if output_dir is None:
        base_dir = Path.cwd()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = base_dir / "output" / "phenopackets"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        # Read input data
        with open(input_data_path, 'r') as f:
            linkml_data = json.load(f)
        
        # Basic validation
        if not isinstance(linkml_data, list):
            raise ValueError("Input data must be a list of patient records")
        
        logger.info(f"Processing {len(linkml_data)} patient records")
        
        # Get CIEINR mapping configuration
        mapping_configs = create_cieinr_phenopacket_mappings()
        
        # Process each record
        phenopackets = []
        
        for record in linkml_data:
            record_id = record.get("record_id", "unknown")
            logger.info(f"Processing record {record_id}")
            
            try:
                # Create a basic DataProcessor for this record
                processor = DataProcessor(record, mapping_configs["individual"]["mapping_block"])
                
                # Map individual component (using RareLink's function)
                individual = rarelink_map_individual(record, processor)
                
                # Set vital status to UNKNOWN
                vital_status = VitalStatus()
                vital_status.status = VitalStatus.UNKNOWN_STATUS
                individual.vital_status = vital_status
                
                # Map disease (using our custom function)
                disease = map_cieinr_disease(record)
                
                # Calculate timeAtLastEncounter if missing
                if not individual.time_at_last_encounter:
                    dob = record.get("patient_demographics_initial_form", {}).get("snomedct_184099003")
                    visit_date = record.get("patient_demographics_initial_form", {}).get("visit_date_demographics")
                    
                    if dob and visit_date:
                        individual.time_at_last_encounter = calculate_age_at_encounter(dob, visit_date)
                
                # Generate metadata using CIEINR-specific function
                metadata = map_cieinr_metadata(created_by)
                
                # Create the phenopacket
                phenopacket = Phenopacket(
                    id=record_id,
                    subject=individual,
                    meta_data=metadata
                )
                
                # Add disease if available
                if disease:
                    phenopacket.diseases.append(disease)
                
                # Add to our list
                phenopackets.append(phenopacket)
                
                # Write to file
                output_file = output_dir / f"{record_id}.json"
                
                with open(output_file, 'w') as f:
                    # Use RareLink's write function to serialize as JSON
                    json_content = write_phenopackets([phenopacket], as_string=True)
                    
                    # Load and reorder to ensure metadata is last
                    phenopacket_dict = json.loads(json_content)[0]
                    ordered_phenopacket = {}
                    
                    # First add ID, subject, diseases, and other fields
                    for key in ["id", "subject", "diseases", "phenotypicFeatures", "measurements"]:
                        if key in phenopacket_dict:
                            ordered_phenopacket[key] = phenopacket_dict[key]
                    
                    # Then add metadata at the end
                    if "metaData" in phenopacket_dict:
                        ordered_phenopacket["metaData"] = phenopacket_dict["metaData"]
                    
                    # Write the ordered dictionary
                    json.dump(ordered_phenopacket, f, indent=2)
                
                logger.info(f"Created phenopacket for {record_id}")
                
            except Exception as e:
                logger.error(f"Error processing record {record_id}: {e}")
                continue
        
        logger.info(f"Created {len(phenopackets)} phenopackets in {output_dir}")
        return phenopackets
        
    except Exception as e:
        logger.error(f"Error processing phenopackets: {e}")
        raise

def main():
    """Command-line interface for phenopacket export."""
    # Set paths
    base_dir = Path.cwd()
    input_data_path = base_dir / "res" / "patient_linkml.json"
    output_dir = base_dir / "output" / "phenopackets"
    
    # Process phenopackets
    try:
        phenopackets = process_cieinr_phenopackets(
            input_data_path=input_data_path, 
            output_dir=output_dir,
            created_by="CIEINR Data Curator"
        )
        print(f"Phenopackets successfully created in {output_dir}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
"""
CIEINR Phenopackets Pipeline

This module provides functions to create Phenopackets from CIEINR data using
RareLink's Phenopacket generation engine. It adapts RareLink's mapping and processing
capabilities to work with the CIEINR data model.
"""

import os
import logging
import json
from pathlib import Path
from typing import Dict, Any, List, Tuple
from dotenv import load_dotenv

# Try loading environment variables
try:
    # Load from .env file if it exists
    load_dotenv()
except Exception as e:
    print(f"Warning: Could not load .env file: {e}")

# Import RareLink phenopacket functions
from rarelink.phenopackets import (
    create_phenopacket,
    write_phenopackets,
    validate_phenopackets
)

# Import CIEINR-specific mappings
from cieinr.v1_0_0.mappings.phenopackets.cieinr_phenopackets_mappings import create_cieinr_phenopacket_mappings

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def enhance_phenopacket_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Enhance CIEINR data to work better with RareLink's phenopacket functions.
    
    Args:
        data: CIEINR data
        
    Returns:
        Enhanced data
    """
    # Create a copy to avoid modifying the original
    enhanced_data = data.copy()
    
    # Ensure repeated_elements is a list
    if "repeated_elements" not in enhanced_data:
        enhanced_data["repeated_elements"] = []
    
    # Ensure basic structures exist
    if "basic_form" not in enhanced_data:
        enhanced_data["basic_form"] = {}
    
    if "patient_demographics_initial_form" not in enhanced_data:
        enhanced_data["patient_demographics_initial_form"] = {}
    
    # Process infection type fields to make them more RareLink-friendly
    for element in enhanced_data.get("repeated_elements", []):
        if element.get("redcap_repeat_instrument") == "infections_initial_form":
            infection_data = element.get("infections_initial_form", {})
            if infection_data:
                # Try to set the type_field directly if possible
                if "type_of_infection" in infection_data:
                    infection_type = infection_data["type_of_infection"]
                    # If the type has a corresponding value field, use it
                    if infection_type in infection_data:
                        # Already structured correctly
                        pass
    
    return enhanced_data

def create_cieinr_phenopacket(data: dict, created_by: str) -> Any:
    """
    Create a Phenopacket from CIEINR data.
    
    Args:
        data (dict): CIEINR data record
        created_by (str): Name of the person/system creating the phenopacket
        
    Returns:
        Phenopacket: A Phenopacket object
    """
    # Get CIEINR mapping configurations
    mapping_configs = create_cieinr_phenopacket_mappings()
    
    # Enhance data for better compatibility with RareLink
    enhanced_data = enhance_phenopacket_data(data)
    
    # Create the phenopacket using RareLink's function
    try:
        phenopacket = create_phenopacket(
            data=enhanced_data,
            created_by=created_by,
            mapping_configs=mapping_configs
        )
        return phenopacket
    except Exception as e:
        logger.error(f"Error creating phenopacket: {e}")
        raise

def ensure_valid_output_filename(record_id: str) -> str:
    """
    Ensure that the record ID will create a valid filename.
    
    Args:
        record_id: The record ID to check
        
    Returns:
        A sanitized record ID suitable for use as a filename
    """
    # Replace any characters that could cause issues in filenames
    import re
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', str(record_id))
    
    # Ensure it's not empty
    if not sanitized or sanitized.isspace():
        import uuid
        sanitized = f"record_{uuid.uuid4().hex[:8]}"
        
    return sanitized

def cieinr_phenopackets_pipeline(
    input_data: List[dict], 
    output_dir: str, 
    created_by: str, 
    validate: bool = False
) -> Tuple[List[Any], List[Dict[str, Any]]]:
    """
    Process CIEINR data and create Phenopackets.
    
    Args:
        input_data (List[dict]): List of CIEINR data records
        output_dir (str): Directory to save Phenopacket JSON files
        created_by (str): Name of the person/system creating the phenopackets
        validate (bool): Whether to validate the created phenopackets
        
    Returns:
        Tuple[List[Any], List[Dict[str, Any]]]: Tuple containing:
            - List of successfully created Phenopackets
            - List of failed records with their errors
    """
    # Create output directory if it doesn't exist
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Create Phenopackets
    phenopackets = []
    failed_records = []
    
    for record in input_data:
        try:
            # Ensure record has a valid ID for the output filename
            if 'record_id' not in record or not record['record_id']:
                record['record_id'] = f"record_{len(phenopackets)+1}"
            
            # Sanitize the record ID for use as a filename
            record['record_id'] = ensure_valid_output_filename(record['record_id'])
            
            phenopacket = create_cieinr_phenopacket(record, created_by)
            phenopackets.append(phenopacket)
            record_id = record.get('record_id', 'unknown')
            logger.info(f"Created Phenopacket for record id={record_id}")
        except Exception as e:
            record_id = record.get('record_id', 'unknown')
            logger.error(f"Failed to create Phenopacket for record id={record_id}: {e}")
            failed_records.append({
                'record': record,
                'error': str(e)
            })
    
    # Write Phenopackets to files - standard format with record_id.json naming
    logger.info(f"Writing {len(phenopackets)} Phenopackets to {output_dir}")
    write_phenopackets(phenopackets, output_dir)
    
    # Validate Phenopackets if requested
    if validate and phenopackets:
        logger.info("Validating Phenopackets...")
        try:
            validation_results = validate_phenopackets(output_path)
            if isinstance(validation_results, list):
                for i, (success, details) in enumerate(validation_results):
                    if success:
                        logger.info(f"Validation successful for phenopacket {i+1}")
                    else:
                        logger.error(f"Validation failed for phenopacket {i+1}: {details}")
            else:
                success, details = validation_results
                if success:
                    logger.info("Validation successful")
                else:
                    logger.error(f"Validation failed: {details}")
        except Exception as e:
            logger.error(f"Error during validation: {e}")
    
    # Log summary
    logger.info(f"Total records processed: {len(input_data)}")
    logger.info(f"Successful Phenopackets: {len(phenopackets)}")
    logger.info(f"Failed records: {len(failed_records)}")
    
    return phenopackets, failed_records

def load_cieinr_data(input_file: str) -> List[dict]:
    """
    Load CIEINR data from a JSON file.
    
    Args:
        input_file (str): Path to JSON file containing CIEINR data
        
    Returns:
        List[dict]: List of CIEINR data records
    """
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
        logger.info(f"Loaded {len(data)} records from {input_file}")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {input_file}: {e}")
        raise

def run_cieinr_phenopackets_pipeline(
    input_file: str, 
    output_dir: str, 
    created_by: str = None,
    validate: bool = False
) -> Tuple[List[Any], List[Dict[str, Any]]]:
    """
    Run the complete CIEINR Phenopackets pipeline.
    
    Args:
        input_file (str): Path to JSON file containing CIEINR data
        output_dir (str): Directory to save Phenopacket JSON files
        created_by (str): Name of the person/system creating the phenopackets
        validate (bool): Whether to validate the created phenopackets
        
    Returns:
        Tuple[List[Any], List[Dict[str, Any]]]: Tuple containing:
            - List of successfully created Phenopackets
            - List of failed records with their errors
    """
    # Load data
    input_data = load_cieinr_data(input_file)
    
    # If created_by is not provided, try to get it from the environment
    if created_by is None:
        created_by = os.getenv("CREATED_BY")
    
    # Run pipeline
    return cieinr_phenopackets_pipeline(input_data, output_dir, created_by, validate)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Create Phenopackets from CIEINR data")
    parser.add_argument(
        "--input", 
        required=True, 
        help="Path to JSON file containing CIEINR data"
    )
    parser.add_argument(
        "--output-dir", 
        required=True, 
        help="Directory to save Phenopacket JSON files"
    )
    parser.add_argument(
        "--created-by", 
        default=None, 
        help="Name of the person/system creating the phenopackets"
    )
    parser.add_argument(
        "--validate", 
        action="store_true", 
        help="Validate the created phenopackets"
    )
    
    args = parser.parse_args()
    
    run_cieinr_phenopackets_pipeline(
        args.input, 
        args.output_dir, 
        args.created_by,
        args.validate
    )
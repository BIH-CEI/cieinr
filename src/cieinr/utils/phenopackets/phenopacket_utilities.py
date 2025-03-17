"""
CIEINR Phenopacket Utilities

This module provides utility functions for working with CIEINR data and transforming it
into Phenopackets. These utilities are designed to supplement RareLink's phenopacket 
functionality and address CIEINR-specific data structures.
"""

import logging
import json
import re
import uuid
from pathlib import Path
from typing import Dict, Any, List, Union, Optional, Tuple

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ensure_valid_output_filename(record_id: str) -> str:
    """
    Ensure that the record ID will create a valid filename.
    
    Args:
        record_id: The record ID to check
        
    Returns:
        A sanitized record ID suitable for use as a filename
    """
    # Replace any characters that could cause issues in filenames
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', str(record_id))
    
    # Ensure it's not empty
    if not sanitized or sanitized.isspace():
        sanitized = f"record_{uuid.uuid4().hex[:8]}"
        
    return sanitized

def convert_linkml_to_cieinr_format(linkml_data: List[dict]) -> List[dict]:
    """
    Convert data from LinkML's format to CIEINR's expected format.
    
    Args:
        linkml_data (List[dict]): Data in LinkML format (e.g., from datamodel.py classes)
        
    Returns:
        List[dict]: Data in CIEINR format for phenopacket generation
    """
    converted_data = []
    
    for item in linkml_data:
        # Copy the item to avoid modifying the original
        converted_item = {
            "record_id": item.get("record_id", "unknown")
        }
        
        # Handle nested form data
        for form_name in ["form_1_basic", "form_2_demographics_initial"]:
            if form_name in item:
                # Convert form_1_basic to basic_form
                target_name = form_name.replace("form_1_", "").replace("form_2_", "")
                converted_item[target_name] = item[form_name]
        
        # Handle repeated elements
        if "repeated_elements" in item and isinstance(item["repeated_elements"], list):
            converted_item["repeated_elements"] = []
            
            for element in item["repeated_elements"]:
                converted_element = {
                    "redcap_repeat_instrument": element.get("redcap_repeat_instrument", ""),
                    "redcap_repeat_instance": element.get("redcap_repeat_instance", 1)
                }
                
                # Copy the form data
                if "form_3_infections_initial" in element:
                    converted_element["infections_initial_form"] = element["form_3_infections_initial"]
                
                # Add any other repeat instruments as needed
                
                converted_item["repeated_elements"].append(converted_element)
        
        converted_data.append(converted_item)
    
    return converted_data

def load_linkml_json(file_path: Union[str, Path]) -> List[dict]:
    """
    Load LinkML JSON data from a file.
    
    Args:
        file_path (Union[str, Path]): Path to the JSON file
        
    Returns:
        List[dict]: The loaded data
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {e}")
        raise

def extract_phenopacket_data(cieinr_data: dict) -> Dict[str, Any]:
    """
    Extract relevant data from a CIEINR record for phenopacket generation.
    
    Args:
        cieinr_data (dict): A CIEINR data record
        
    Returns:
        Dict[str, Any]: Data extracted for phenopacket generation
    """
    # Ensure record_id is present and valid for filename generation
    record_id = cieinr_data.get("record_id", "unknown")
    if not record_id or record_id == "unknown":
        # Generate a unique ID if none exists
        record_id = f"generated-{uuid.uuid4()}"
    
    extracted_data = {
        "record_id": record_id,
    }
    
    # Extract basic form data
    if "basic_form" in cieinr_data:
        extracted_data["basic_form"] = cieinr_data["basic_form"]
    
    # Extract demographics data
    if "patient_demographics_initial_form" in cieinr_data:
        extracted_data["patient_demographics_initial_form"] = cieinr_data["patient_demographics_initial_form"]
    
    # Extract infections data
    if "repeated_elements" in cieinr_data:
        extracted_data["repeated_elements"] = [
            element for element in cieinr_data["repeated_elements"]
            if element.get("redcap_repeat_instrument") == "infections_initial_form"
        ]
    
    return extracted_data

def enhance_phenopacket_data(cieinr_data: dict) -> dict:
    """
    Enhance a CIEINR record with additional data needed for phenopacket generation.
    
    Args:
        cieinr_data (dict): A CIEINR data record
        
    Returns:
        dict: Enhanced record
    """
    # Create a copy to avoid modifying the original
    enhanced_data = cieinr_data.copy()
    
    # Ensure required structures exist
    if "repeated_elements" not in enhanced_data:
        enhanced_data["repeated_elements"] = []
    
    if "basic_form" not in enhanced_data:
        enhanced_data["basic_form"] = {}
    
    if "patient_demographics_initial_form" not in enhanced_data:
        enhanced_data["patient_demographics_initial_form"] = {}
    
    # If infections data exists but not in the expected format, convert it
    if "infections_initial_form" in enhanced_data and enhanced_data["infections_initial_form"]:
        infections = enhanced_data["infections_initial_form"]
        
        if isinstance(infections, list):
            # Add each infection as a repeated element
            for i, infection in enumerate(infections):
                enhanced_data["repeated_elements"].append({
                    "redcap_repeat_instrument": "infections_initial_form",
                    "redcap_repeat_instance": i + 1,
                    "infections_initial_form": infection
                })
            
            # Remove the original infections data
            del enhanced_data["infections_initial_form"]
    
    return enhanced_data

def prepare_cieinr_data_for_phenopackets(data: Union[List[dict], dict]) -> List[dict]:
    """
    Prepare CIEINR data for phenopacket generation.
    
    This function handles various input formats and ensures the data is in the correct
    format for phenopacket generation.
    
    Args:
        data (Union[List[dict], dict]): CIEINR data in various formats
        
    Returns:
        List[dict]: Data prepared for phenopacket generation
    """
    if isinstance(data, dict):
        # Single record
        data = [data]
    
    prepared_data = []
    
    for item in data:
        # Extract relevant data
        extracted_data = extract_phenopacket_data(item)
        
        # Enhance the data
        enhanced_data = enhance_phenopacket_data(extracted_data)
        
        prepared_data.append(enhanced_data)
    
    return prepared_data

def get_mondo_code_label(code: str) -> str:
    """
    Get the label for a MONDO code.
    
    Args:
        code (str): MONDO code (e.g., "mondo_0007843")
        
    Returns:
        str: Label for the code or a default if not found
    """
    try:
        # Try to import IUIS labels
        from cieinr.v1_0_0.mappings.phenopackets.cieinr_phenopackets_mappings import create_cieinr_phenopacket_mappings
        
        mappings = create_cieinr_phenopacket_mappings()
        disease_mappings = mappings.get("diseases", {})
        label_dicts = disease_mappings.get("label_dicts", {})
        iuis_labels = label_dicts.get("IUIS2024MONDO", {})
        
        return iuis_labels.get(code, f"Unknown MONDO condition: {code}")
    except ImportError:
        return f"Unknown MONDO condition: {code}"
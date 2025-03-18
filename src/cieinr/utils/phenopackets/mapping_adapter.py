"""
CIEINR Mapping Adapter for RareLink

This module provides adapter functions to enhance RareLink's mapping functionality
for CIEINR data. It patches critical functions to handle CIEINR's data model structure.
"""

import logging
from typing import Dict, Any, Optional, List, Union
from datetime import datetime
import functools
import types
import sys

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Store references to original RareLink functions
original_functions = {}

def enhance_map_individual(data: dict, processor, **kwargs):
    """
    Enhanced version of map_individual that handles CIEINR's data structure.
    
    Args:
        data: The input data
        processor: DataProcessor instance
        **kwargs: Additional arguments
        
    Returns:
        The mapped individual
    """
    # Special handling for CIEINR data structure
    try:
        # Handle nested data in CIEINR
        if 'patient_demographics_initial_form' in data:
            # CIEINR stores basic demographics in a nested structure
            # Check if any fields don't exist and add them with None
            mapping_config = processor.mapping_config
            for key in ["id_field", "date_of_birth_field", "time_at_last_encounter_field", 
                        "sex_field", "karyotypic_sex_field", "gender_field"]:
                if key not in mapping_config:
                    mapping_config[key] = None
            
            # Ensure record_id is available
            if 'record_id' not in data and 'id_field' in mapping_config:
                # Try to extract it from the mapping configuration
                id_field = mapping_config.get("id_field")
                if id_field:
                    data['record_id'] = processor.get_field(data, "id_field")
        
        # Call the original function
        from rarelink.phenopackets.mappings import map_individual
        return map_individual(data, processor, **kwargs)
    except Exception as e:
        logger.error(f"Error in enhanced map_individual: {e}")
        raise

def enhance_map_diseases(data: dict, processor, **kwargs):
    """
    Enhanced version of map_diseases that handles CIEINR's data structure.
    
    Args:
        data: The input data
        processor: DataProcessor instance
        **kwargs: Additional arguments
        
    Returns:
        The mapped diseases
    """
    # Special handling for CIEINR disease data
    try:
        if 'basic_form' in data and 'iei_deficiency_basic' in data['basic_form']:
            # CIEINR stores disease data in a different structure than RareLink expects
            disease_data = data['basic_form']
            
            # Create a disease list manually
            from phenopackets import Disease, OntologyClass
            
            disease_code = disease_data.get('iei_deficiency_basic')
            if disease_code:
                # Get disease label from MONDO/custom mapping
                label_lookup = processor.mapping_config.get("label_dict", {})
                disease_label = label_lookup.get(disease_code, "Unknown IEI deficiency")
                
                # Create the disease term
                term = OntologyClass(id=disease_code, label=disease_label)
                
                # Create the disease
                disease = Disease(term=term)
                
                return [disease]
            
            return []
        
        # Call the original function
        from rarelink.phenopackets.mappings import map_diseases
        return map_diseases(data, processor, **kwargs)
    except Exception as e:
        logger.error(f"Error in enhanced map_diseases: {e}")
        raise

def enhance_map_phenotypic_features(data: dict, processor, **kwargs):
    """
    Enhanced version of map_phenotypic_features that handles CIEINR's data structure.
    
    Args:
        data: The input data
        processor: DataProcessor instance
        **kwargs: Additional arguments
        
    Returns:
        The mapped phenotypic features
    """
    # Special handling for CIEINR infection data
    try:
        # Check for repeated_elements with infections
        found_infections = False
        if 'repeated_elements' in data:
            for element in data['repeated_elements']:
                if element.get('redcap_repeat_instrument') == 'infections_initial_form':
                    found_infections = True
                    break
        
        if not found_infections:
            return []  # No infections found
        
        # Call the original function
        from rarelink.phenopackets.mappings import map_phenotypic_features
        return map_phenotypic_features(data, processor, **kwargs)
    except Exception as e:
        logger.error(f"Error in enhanced map_phenotypic_features: {e}")
        raise

def enhance_get_field(self, data: dict, field_name: str, highest_redcap_repeat_instance: bool = False):
    """
    Enhanced version of get_field that handles CIEINR's nested data structure.
    
    Args:
        self: The DataProcessor instance
        data: The input data
        field_name: Name of the field to get
        highest_redcap_repeat_instance: Whether to get the highest repeat instance
        
    Returns:
        The field value
    """
    field_path = self.mapping_config.get(field_name)
    if not field_path:
        return None
    
    # Handle nested paths with dot notation (e.g., "basic_form.iei_deficiency_basic")
    if isinstance(field_path, str) and '.' in field_path:
        parts = field_path.split('.')
        temp_data = data
        for part in parts:
            if temp_data is None:
                return None
            if isinstance(temp_data, dict) and part in temp_data:
                temp_data = temp_data[part]
            else:
                return None
        return temp_data
    
    # Fall back to original method
    from rarelink.utils.loading import get_nested_field
    return get_nested_field(data, field_path, highest_redcap_repeat_instance)

def monkey_patch_function(module_name, function_name, new_function):
    """
    Monkey patch a function in a module with a new implementation.
    
    Args:
        module_name: Name of the module containing the function
        function_name: Name of the function to patch
        new_function: New implementation of the function
    """
    try:
        module = sys.modules[module_name]
        original = getattr(module, function_name)
        original_functions[(module_name, function_name)] = original
        setattr(module, function_name, new_function)
        logger.info(f"Patched {module_name}.{function_name}")
    except Exception as e:
        logger.error(f"Failed to patch {module_name}.{function_name}: {e}")

def apply_patches():
    """
    Apply all enhancement patches to RareLink functions.
    
    This function should be called before using RareLink's Phenopacket generation
    with CIEINR data.
    """
    try:
        # Register our custom implementations for the mapping functions
        # We're patching the module directly instead of trying to modify __code__
        monkey_patch_function(
            "rarelink.phenopackets.create", 
            "create_cieinr_phenopacket",
            enhance_map_individual
        )
        
        # Patch DataProcessor.get_field
        from rarelink.utils.processor import DataProcessor
        DataProcessor.get_field = enhance_get_field
        
        # Use custom implementations for specific data
        
        logger.info("Applied all CIEINR-specific patches to RareLink functions")
    except Exception as e:
        logger.error(f"Error applying patches: {e}")
        raise
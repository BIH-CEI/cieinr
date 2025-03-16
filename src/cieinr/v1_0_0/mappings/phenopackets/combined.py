"""
Combined mapping configuration for CIEINR Phenopacket export.

This module creates a simple, modular mapping configuration that leverages
RareLink's phenopacket mapping functionality while adding CIEINR-specific configuration.
"""

from typing import Dict, Any, Optional, List

# Import enum classes from Python schemas
from cieinr.v1_0_0.python_schemas.form_1_basic import IUIS2024MONDOEnum
from cieinr.v1_0_0.python_schemas.form_3_infections_initial import (
    InfectionSeverityEnum,
    InfectionTemporalPatternEnum
)

# Import mapping blocks and code systems
from cieinr.v1_0_0.mappings.phenopackets.metadata import CIEINR_CODE_SYSTEMS_CONTAINER
from cieinr.v1_0_0.mappings.phenopackets.mapping_blocks import (
    INDIVIDUAL_BLOCK,
    VITAL_STATUS_BLOCK,
    DISEASE_BLOCK,
    PHENOTYPIC_FEATURES_BLOCK,
    MAPPING_DICTS
)

def extract_linkml_enum_labels(enum_class) -> Dict[str, str]:
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
            # Skip any attributes that cause errors when accessed
            continue
            
    return labels

def create_cieinr_phenopacket_mappings() -> Dict[str, Any]:
    """
    Create a clean, modular mapping configuration for Phenopacket creation from CIEINR data.

    Returns:
        Dict[str, Any]: Combined mapping configurations
    """
    # Build mapping dictionary lookup for easier access
    mapping_dict_lookup = {
        mapping['name']: mapping['mapping'] 
        for mapping in MAPPING_DICTS
    }

    # Extract labels from LinkML-generated enums
    iuis_labels = extract_linkml_enum_labels(IUIS2024MONDOEnum)
    severity_labels = extract_linkml_enum_labels(InfectionSeverityEnum)
    temporal_pattern_labels = extract_linkml_enum_labels(InfectionTemporalPatternEnum)

    # Create a clean mapping structure
    return {
        "individual": {
            "instrument_name": None,  # Not in repeated elements
            "mapping_block": INDIVIDUAL_BLOCK,
        },
        "vitalStatus": {
            "instrument_name": None,
            "mapping_block": VITAL_STATUS_BLOCK,
            "default_status": "UNKNOWN_STATUS"
        },
        "diseases": {
            "instrument_name": None,  # Not in repeated elements
            "mapping_block": DISEASE_BLOCK,
            "label_dicts": {
                "IUISLabels": iuis_labels
            },
            "mapping_dicts": {
                "map_mondo_codes": mapping_dict_lookup.get("map_mondo_codes", {}),
                "map_disease_verification_status": mapping_dict_lookup.get("map_disease_verification_status", {})
            }
        },
        "phenotypicFeatures": {
            "instrument_name": "infections_initial_form",
            "mapping_block": PHENOTYPIC_FEATURES_BLOCK,
            "label_dicts": {
                "SeverityLabels": severity_labels,
                "TemporalPatternLabels": temporal_pattern_labels
            },
            "mapping_dicts": {
                "map_infection_severity": mapping_dict_lookup.get("map_infection_severity", {}),
                "map_infection_temporal_pattern": mapping_dict_lookup.get("map_infection_temporal_pattern", {})
            }
        },
        "measurements": {
            "instrument_name": None,
            "mapping_block": {
                "instrument_name": None  # Not using measurements
            }
        },
        "metadata": {
            "code_systems": CIEINR_CODE_SYSTEMS_CONTAINER
        }
    }

def get_mapping_for_block(
    block_name: str, 
    mapping_type: str, 
    key: str, 
    mappings: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Retrieve a specific mapping or label dictionary from the comprehensive mappings.

    Args:
        block_name: Name of the block (e.g., 'individual', 'diseases')
        mapping_type: Type of mapping ('label_dicts' or 'mapping_dicts')
        key: Specific mapping or label key
        mappings: Mappings to use. Defaults to CIEINR mappings.

    Returns:
        The requested mapping or label dictionary
    """
    if mappings is None:
        mappings = create_cieinr_phenopacket_mappings()
    
    block_mappings = mappings.get(block_name, {})
    
    if mapping_type not in block_mappings:
        return {}
    
    return block_mappings[mapping_type].get(key, {})

def get_block_mapping(block_name: str, mappings: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Get the mapping block for a specific block type.
    
    Args:
        block_name: Name of the block (e.g., 'individual', 'diseases')
        mappings: Mappings to use. Defaults to CIEINR mappings.
        
    Returns:
        The mapping block
    """
    if mappings is None:
        mappings = create_cieinr_phenopacket_mappings()
        
    block_data = mappings.get(block_name, {})
    return block_data.get("mapping_block", {})
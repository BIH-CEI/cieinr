"""Utility functions for mapping ontology terms."""

from typing import Dict, Any, Optional

def map_term(code: str, mapping_dict: Dict[str, Dict[str, str]], default_ontology: Optional[str] = None) -> Dict[str, str]:
    """
    Maps a code to its ontology term using the provided mapping dictionary.
    
    Args:
        code: The code to map
        mapping_dict: Dictionary mapping codes to terms
        default_ontology: Optional default ontology prefix if not found in code
        
    Returns:
        Dictionary with id and label
    """
    if code in mapping_dict:
        return mapping_dict[code]
    
    # If code not found, try to infer a structured response
    if '_' in code:
        parts = code.split('_')
        if len(parts) >= 2:
            ontology = parts[0].upper()
            identifier = parts[1]
            
            # Format according to standard conventions
            if ontology == 'HP':
                return {"id": f"HP:{identifier}", "label": f"Unknown HP term ({identifier})"}
            elif ontology == 'MONDO':
                return {"id": f"MONDO:{identifier}", "label": f"Unknown MONDO term ({identifier})"}
            elif ontology == 'NCIT':
                return {"id": f"NCIT:{identifier}", "label": f"Unknown NCIT term ({identifier})"}
            elif ontology == 'SNOMEDCT':
                return {"id": f"SNOMEDCT:{identifier}", "label": f"Unknown SNOMEDCT term ({identifier})"}
    
    # If no structure was found but default ontology provided
    if default_ontology:
        return {"id": f"{default_ontology}:{code}", "label": f"Unknown term ({code})"}
    
    # Default fallback
    return {"id": code, "label": f"Unknown term ({code})"}

def get_ontology_mappings(module_name: str, variable_name: str) -> Dict[str, Dict[str, str]]:
    """
    Dynamically import ontology mappings from the specified module.
    
    Args:
        module_name: Name of the module containing the mappings
        variable_name: Name of the variable in the module
        
    Returns:
        Dictionary of mappings
    """
    try:
        module = __import__(module_name, fromlist=[variable_name])
        return getattr(module, variable_name)
    except (ImportError, AttributeError) as e:
        print(f"Error importing ontology mappings: {e}")
        return {}
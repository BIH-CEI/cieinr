"""Functions for processing codes."""

def process_code(code: str) -> str:
    """
    Processes a code to ensure proper format.
    
    Args:
        code: Code to process (e.g., "hp_0012826")
        
    Returns:
        Processed code (e.g., "HP:0012826") or the original code if format is unknown
    """
    if not code:
        return code
        
    # Determine delimiter
    delimiter = "_" if "_" in code else ":" if ":" in code else None
    if not delimiter:
        return code
        
    # Split prefix and code
    prefix, rest = code.split(delimiter, 1)
    prefix_upper = prefix.upper()
    
    # Handle transformation based on prefix
    if delimiter == "_":
        # Replace the first "_" with ":"
        processed_code = f"{prefix_upper}:{rest}"
        
        # Special handling for LOINC: Replace subsequent "_" with "-" and ensure uppercase
        if prefix_upper == "LOINC":
            processed_code = f"{prefix_upper}:{rest.replace('_', '-').upper()}"
            
        # Special handling for NCIT: Uppercase code part
        if prefix_upper == "NCIT":
            processed_code = f"{prefix_upper}:{rest.upper()}"
            
        # Special handling for ICD codes: Replace subsequent "_" with "."
        elif prefix_upper in ["ICD10CM", "ICD11", "ICD10", "ICD9"]:
            processed_code = f"{prefix_upper}:{rest.replace('_', '.').upper()}"
            
        # Handle SNOMED to SNOMEDCT conversion
        elif prefix_upper == "SNOMED":
            prefix_upper = "SNOMEDCT"
            processed_code = f"{prefix_upper}:{rest}"
            
        return processed_code
        
    elif delimiter == ":":
        # Ensure prefix is uppercase
        return f"{prefix_upper}:{rest}"
        
    return code
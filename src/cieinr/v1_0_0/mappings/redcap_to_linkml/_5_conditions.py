def map_conditions(record):
    """
    Map REDCap record data to the ConditionsInitial LinkML class format.
    
    Args:
        record (dict): The REDCap record data
        
    Returns:
        dict: The mapped data in LinkML format for conditions
    """
    return {
        # Main condition type
        "type_of_condition": record.get("type_of_condition", ""),
        
        # Specific condition types
        "snomedct_95320005": record.get("snomedct_95320005", ""),  # Skin Condition
        "snomedct_118938008": record.get("snomedct_118938008", ""),  # Dental/Oral Condition
        "snomedct_50043002": record.get("snomedct_50043002", ""),  # Sino-Pulmonary Condition
        "snomedct_49601007": record.get("snomedct_49601007", ""),  # Cardiovascular Condition
        "mondo_0005570": record.get("mondo_0005570", ""),  # Hematologic-Lymphoid Condition
        "snomedct_928000": record.get("snomedct_928000", ""),  # Musculoskeletal Condition
        "snomedct_119292006": record.get("snomedct_119292006", ""),  # Gastrointestinal Condition
        "hp_0002037_evidence": record.get("hp_0002037_evidence", ""),  # IBD Diagnosis Evidence
        "snomedct_362969004": record.get("snomedct_362969004", ""),  # Endocrine-Metabolic Condition
        "snomedct_42030000": record.get("snomedct_42030000", ""),  # Genitourinary Condition
        "snomedct_55342001": record.get("snomedct_55342001", ""),  # Neoplastic Condition
        
        # Modifiers for specific conditions
        "hp_0012539_modifier": record.get("hp_0012539_modifier", ""),  # Non-Hodgkin's Lymphoma - EBV Status
        "hp_0012189_modifier": record.get("hp_0012189_modifier", ""),  # Hodgkin Lymphoma - EBV Status
        "hp_0005523_modifier": record.get("hp_0005523_modifier", ""),  # Polyclonal Lymphoproliferation - EBV Status
        
        # Additional conditions
        "snomedct_85828009": record.get("snomedct_85828009", ""),  # Autoimmune Condition
        "hp_0025142": record.get("hp_0025142", ""),  # Constitutional Condition
        "snomedct_5294002": record.get("snomedct_5294002", ""),  # Growth and Development Condition
        
        # Other condition (HPO)
        "condition_other_hp": record.get("condition_other_hp", ""),  # Other Condition [HPO]
        
        # Additional condition details
        "condition_severity": record.get("condition_severity", ""),
        "condition_temp_pattern": record.get("condition_temp_pattern", ""),
        "condition_date_1": record.get("condition_date_1", ""),
        
        # Form completion status
        "conditions_initial_form_complete": record.get("conditions_initial_form_complete", "")
    }

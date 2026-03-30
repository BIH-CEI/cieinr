# src/cieinr/datamodel/mappers/redcap_to_linkml/map_conditions.py

def map_conditions(record):
    """
    Map REDCap record data to the ConditionsInitial LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "date_condition_form": record.get("date_condition_form", ""),  # Date of completing this form.
        "type_of_condition": record.get("type_of_condition", ""),  # Please select the type of condition from the dropd
        "snomedct_95320005": record.get("snomedct_95320005", ""),  # Skin/Hair Condition
        "snomedct_118938008": record.get("snomedct_118938008", ""),  # Dental/Oral Condition
        "snomedct_50043002": record.get("snomedct_50043002", ""),  # Sino-Pulmonary Condition
        "snomedct_49601007": record.get("snomedct_49601007", ""),  # Cardiovascular Condition
        "mondo_0005570": record.get("mondo_0005570", ""),  # Hematologic-Lymphoid Condition
        "snomedct_928000": record.get("snomedct_928000", ""),  # Musculoskeletal Condition
        "snomedct_119292006": record.get("snomedct_119292006", ""),  # Gastrointestinal Condition
        "hp_0002037_evidence": record.get("hp_0002037_evidence", ""),  # Inflammatory Bowel Disease (IBD) - Type of Diagnos
        "snomedct_362969004": record.get("snomedct_362969004", ""),  # Endocrine-Metabolic Condition
        "snomedct_42030000": record.get("snomedct_42030000", ""),  # Genitourinary Condition
        "snomedct_55342001": record.get("snomedct_55342001", ""),  # Neoplastic Condition
        "hp_0012539_modifier": record.get("hp_0012539_modifier", ""),  # Non-Hodgkin's Lymphoma - EBV Status
        "hp_0012189_modifier": record.get("hp_0012189_modifier", ""),  # Hodgkin Lymphoma - EBV Status
        "hp_0005523_modifier": record.get("hp_0005523_modifier", ""),  # Polyclonal Lymphoproliferation - EBV Status
        "snomedct_85828009": record.get("snomedct_85828009", ""),  # Autoimmune Condition
        "hp_0025142": record.get("hp_0025142", ""),  # Constitutional Symptoms (eg Fatigue)
        "snomedct_5294002": record.get("snomedct_5294002", ""),  # Growth and Development Condition
        "condition_other_hp": record.get("condition_other_hp", ""),  # Other Condition [HPO]
        "new_condition": record.get("new_condition", ""),  # If you cannot find the condition above, please typ
        "condition_severity": record.get("condition_severity", ""),  # What was the maximum severity of the condition?
        "condition_temp_pattern": record.get("condition_temp_pattern", ""),  # Was a temporal pattern observed in the condition? 
        "onsetmonth": record.get("onsetmonth", ""),  # Month
        "yearonset": record.get("yearonset", ""),  # Year
    }

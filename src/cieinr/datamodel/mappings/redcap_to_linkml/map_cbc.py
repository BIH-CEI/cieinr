# src/cieinr/datamodel/mappers/redcap_to_linkml/map_cbc.py

def map_cbc(record):
    """
    Map REDCap record data to the CBC LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "completion_cbc": record.get("completion_cbc", ""),  # Date of completing this form.
        "cbc_type": record.get("cbc_type", ""),  # Please provide the following information at EACH d
        "cbcmonth": record.get("cbcmonth", ""),  # Month
        "cbcyear": record.get("cbcyear", ""),  # Year
        "cbc_haemoglobin": record.get("cbc_haemoglobin", ""),  # CBC - Haemoglobin
        "cbc_haemoglobin_unit": record.get("cbc_haemoglobin_unit", ""),  # Haemoglobin - Please select the unit
        "cbc_haemoglobin_range": record.get("cbc_haemoglobin_range", ""),  # Haemoglobin - Range
        "cbc_haemoglobin_val": record.get("cbc_haemoglobin_val", ""),  # Haemoglobin [g/dL] in Blood
        "cbc_platelets": record.get("cbc_platelets", ""),  # CBC - Platelets
        "cbc_platelets_unit": record.get("cbc_platelets_unit", ""),  # Platelets - Please select the unit
        "cbc_platelets_range": record.get("cbc_platelets_range", ""),  # Platelets - Range
        "cbc_platelets_val": record.get("cbc_platelets_val", ""),  # Platelets [10*9/L] in Blood
        "cbc_leukocytes": record.get("cbc_leukocytes", ""),  # CBC - Leukocytes
        "cbc_leukocytes_unit": record.get("cbc_leukocytes_unit", ""),  # Leukocytes - Please select the unit
        "cbc_leukocytes_range": record.get("cbc_leukocytes_range", ""),  # Leukocytes - Range
        "cbc_leukocytes_val": record.get("cbc_leukocytes_val", ""),  # Leukocytes [10*9/L] in Blood
        "cbc_neutrophils": record.get("cbc_neutrophils", ""),  # CBC - Neutrophils
        "cbc_neutrophils_unit": record.get("cbc_neutrophils_unit", ""),  # Neutrophils - Please select the unit
        "cbc_neutrophils_range": record.get("cbc_neutrophils_range", ""),  # Neutrophils - Range
        "cbc_neutrophils_val": record.get("cbc_neutrophils_val", ""),  # Neutrophils [10*9/L] in Blood
        "cbc_eosinophils": record.get("cbc_eosinophils", ""),  # CBC - Eosinophils
        "cbc_eosinophils_unit": record.get("cbc_eosinophils_unit", ""),  # Eosinophils  - Please select the unit
        "cbc_eosinophils_range": record.get("cbc_eosinophils_range", ""),  # Eosinophils - Range
        "cbc_eosinophils_val": record.get("cbc_eosinophils_val", ""),  # Eosinophils [10*9/L] in Blood
        "cbc_lymphocytes": record.get("cbc_lymphocytes", ""),  # CBC - Lymphocytes
        "cbc_lymphocytes_unit": record.get("cbc_lymphocytes_unit", ""),  # Lymphocytes - Please select the unit
        "cbc_lymphocytes_range": record.get("cbc_lymphocytes_range", ""),  # Lymphocytes - Range
        "cbc_lymphocytes_val": record.get("cbc_lymphocytes_val", ""),  # Lymphocytes [10*9/L] in Blood
        "cbc_monocytes": record.get("cbc_monocytes", ""),  # CBC - Monocytes
        "cbc_monocytes_unit": record.get("cbc_monocytes_unit", ""),  # Monocytes - Please select the unit
        "cbc_monocytes_range": record.get("cbc_monocytes_range", ""),  # Monocytes - Range
        "cbc_monocytes_val": record.get("cbc_monocytes_val", ""),  # Monocytes [10*9/L] in Blood
    }

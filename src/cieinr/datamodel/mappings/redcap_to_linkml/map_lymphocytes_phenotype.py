# src/cieinr/datamodel/mappers/redcap_to_linkml/map_lymphocytes_phenotype.py

def map_lymphocytes_phenotype(record):
    """
    Map REDCap record data to the LymphocytesPhenotype LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "completion_date_lympheno": record.get("completion_date_lympheno", ""),  # Date of completing this form.
        "lympheno_test": record.get("lympheno_test", ""),  # Please provide the following information at EACH d
        "lympheno_loinc_8122_4": record.get("lympheno_loinc_8122_4", ""),  # CD3+ T Cells
        "cd3_tmonth": record.get("cd3_tmonth", ""),  # Month
        "cd3_tyear": record.get("cd3_tyear", ""),  # Year
        "lympheno_loinc_8122_4_unit": record.get("lympheno_loinc_8122_4_unit", ""),  # CD3+ T Cells Unit cells/microliter or x 10E6/L)
        "lympheno_loinc_8122_4_val": record.get("lympheno_loinc_8122_4_val", ""),  # CD3+ T cells Value (cells/microliter or 10E6/L)
        "lympheno_loinc_8122_4_int": record.get("lympheno_loinc_8122_4_int", ""),  # CD3+ interpretation
        "lympheno_loinc_24467_3": record.get("lympheno_loinc_24467_3", ""),  # CD3+/CD4+ T Cells
        "cd3_cd4_month": record.get("cd3_cd4_month", ""),  # Month
        "cd3_cd4_year": record.get("cd3_cd4_year", ""),  # Year
        "lympheno_loinc_24467_3_unit": record.get("lympheno_loinc_24467_3_unit", ""),  # CD3+/CD4+ T Cells Unit (if possible Cells per mill
        "lympheno_loinc_24467_3_val": record.get("lympheno_loinc_24467_3_val", ""),  # CD3+/CD4+ T cells Value (cells/microliter or 10E6/
        "lympheno_loinc_24467_3_int": record.get("lympheno_loinc_24467_3_int", ""),  # CD3+/CD4+ interpretation
        "lympheno_loinc_14135_8": record.get("lympheno_loinc_14135_8", ""),  # CD3+CD8+ T Cells
        "cd3_cd8_month": record.get("cd3_cd8_month", ""),  # Month
        "cd3_cd8_year": record.get("cd3_cd8_year", ""),  # Year
        "lympheno_loinc_14135_8_unit": record.get("lympheno_loinc_14135_8_unit", ""),  # CD3+CD8+ T Cells Unit (if possible Cells per milli
        "lympheno_loinc_14135_8_val": record.get("lympheno_loinc_14135_8_val", ""),  # CD3+CD8+ T Cells Value (cells/microliter or 10E6/L
        "lympheno_loinc_14135_8_int": record.get("lympheno_loinc_14135_8_int", ""),  # CD3+CD8+ interpretation
        "lympheno_loinc_8116_6": record.get("lympheno_loinc_8116_6", ""),  # CD19+ B Cells
        "cd19_bmonth": record.get("cd19_bmonth", ""),  # Month
        "cd19_byear": record.get("cd19_byear", ""),  # Year
        "lympheno_loinc_8116_6_unit": record.get("lympheno_loinc_8116_6_unit", ""),  # CD19+ B Cells Unit (if possible Cells per millilit
        "lympheno_loinc_8116_6_val": record.get("lympheno_loinc_8116_6_val", ""),  # CD19+ B Cells Value (cells/microliter or 10E6/L)
        "lympheno_loinc_8116_6_int": record.get("lympheno_loinc_8116_6_int", ""),  # CD19+ interpretation
        "lympheno_loinc_9558_8": record.get("lympheno_loinc_9558_8", ""),  # CD20+ B Cells
        "cd20_bmonth": record.get("cd20_bmonth", ""),  # Month
        "cd20_byear": record.get("cd20_byear", ""),  # Year
        "lympheno_loinc_9558_8_unit": record.get("lympheno_loinc_9558_8_unit", ""),  # CD20+ B Cells Unit (if possible Cells per millilit
        "lympheno_loinc_9558_8_val": record.get("lympheno_loinc_9558_8_val", ""),  # CD20+ B Cells Value (cells/microliter or 10E6/L)
        "lympheno_loinc_9558_8_int": record.get("lympheno_loinc_9558_8_int", ""),  # CD20+ interpretation
        "lympheno_loinc_9728_7": record.get("lympheno_loinc_9728_7", ""),  # CD3-CD16+CD56+ Natural Killer T Cells
        "nktcellsmonth": record.get("nktcellsmonth", ""),  # Month
        "nktcellsyear": record.get("nktcellsyear", ""),  # Year
        "lympheno_loinc_9728_7_unit": record.get("lympheno_loinc_9728_7_unit", ""),  # CD3-CD16+CD56+ Natural Killer T Cells Unit (if pos
        "lympheno_loinc_9728_7_val": record.get("lympheno_loinc_9728_7_val", ""),  # CD3-CD16+CD56+ Natural Killer T Cells Value
        "lympheno_loinc_9728_7_int": record.get("lympheno_loinc_9728_7_int", ""),  # CD3-CD16+CD56+ Natural Killer T Cells interpretati
        "lymphopheno_other": record.get("lymphopheno_other", ""),  # Were other more specific lymphocyte subsets tested
        "lymphopheno_test": record.get("lymphopheno_test", ""),  # Please upload the pdf test results. REMOVE PATIENT
    }

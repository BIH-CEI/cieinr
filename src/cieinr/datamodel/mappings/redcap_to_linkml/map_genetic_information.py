# src/cieinr/datamodel/mappers/redcap_to_linkml/map_genetic_information.py

def map_genetic_information(record):
    """
    Map REDCap record data to the GeneticInformation LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "completion_date_genetic": record.get("completion_date_genetic", ""),  # Date of completing this form.
        "geneticonfirmation": record.get("geneticonfirmation", ""),  # Does  the participant have a genetic confirmation?
        "geneticevaluationmonth": record.get("geneticevaluationmonth", ""),  # Month
        "geneticevaluationyear": record.get("geneticevaluationyear", ""),  # Year
        "genetic_diagnosis_g": record.get("genetic_diagnosis_g", ""),  # Does the patient have an IEI diagnosis that is rel
        "g_iei_deficiency": record.get("g_iei_deficiency", ""),  # Please choose the genetic IEI deficiency (IUIS2024
        "other_non_g_iei": record.get("other_non_g_iei", ""),  # If non-genetic, please select from the non-genetic
        "gen_report": record.get("gen_report", ""),  # Please upload genetics report.  REMOVE PATIENT'S P
        "g_other_iei_deficiency": record.get("g_other_iei_deficiency", ""),  # please search for the other IEI deficiency in MOND
        "g_other_iei_def_text": record.get("g_other_iei_def_text", ""),  # If not found in MONDO, specify in the text field
        "interpretation_status": record.get("interpretation_status", ""),  # Is this variant thought to be related to the diagn
        "loinc_81304_8": record.get("loinc_81304_8", ""),  # Please indicate what genetic testing method has be
        "loinc_81304_8_other": record.get("loinc_81304_8_other", ""),  # Please indicate other test
        "loinc_48018_6": record.get("loinc_48018_6", ""),  # Gene ID (for example rs6025)
        "loinc_lp7824_8": record.get("loinc_lp7824_8", ""),  # For unvalidated variants, type in the variant:
        "variant_expression": record.get("variant_expression", ""),  # Please choose the type of the variant's validated 
        "change_hgvsexpress": record.get("change_hgvsexpress", ""),  # Indicate other changes
        "loinc_81290_9": record.get("loinc_81290_9", ""),  # Please indicate the genomic DNA sequence change as
        "loinc_48004_6": record.get("loinc_48004_6", ""),  # Please indicate the DNA change as a validated HGVS
        "loinc_48005_3": record.get("loinc_48005_3", ""),  # Please indicate protein change as a validated HGVS
        "variant_validation": record.get("variant_validation", ""),  # Please validate the variant in
        "geno_0000141": record.get("geno_0000141", ""),  # Pattern of inheritance
        "geno_0000141_other": record.get("geno_0000141_other", ""),  # The name of other type of inheritance [GENO]
        "loinc_48019_4": record.get("loinc_48019_4", ""),  # What is the variant type or consequence?
        "loinc_48019_4_other": record.get("loinc_48019_4_other", ""),  # What is the other mutation type? [GENO]
        "loinc_53034_5": record.get("loinc_53034_5", ""),  # Zygosity, eg. homozygous, heterozygous
        "loinc_53034_5_other": record.get("loinc_53034_5_other", ""),  # Please specify other zygosity [GENO]
        "protein_funct": record.get("protein_funct", ""),  # What is the effect of the variant on protein funct
        "pther_prot_expr": record.get("pther_prot_expr", ""),  # Please clarify other type
        "loinc_53037_8": record.get("loinc_53037_8", ""),  # Clinical Significance [ACMG] or Classification
        "clinician_verified": record.get("clinician_verified", ""),  # Has this form been verified by the clinician?
    }

ADDITIONAL_PROCESSING = {
    "snomedct_106221001_omim_p": lambda x: add_prefix_to_code(x, "OMIM"),
    "variant_validation": lambda x: {"yes": True, "no": False}.get(x.lower(), None),
    "loinc_53034_5_other": lambda x: add_prefix_to_code(x, "LOINC"),
    "loinc_48019_4_other": lambda x: add_prefix_to_code(x, "LOINC")
}

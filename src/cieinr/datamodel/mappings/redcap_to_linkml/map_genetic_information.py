# src/cieinr/datamodel/mappers/redcap_to_linkml/map_genetic_information.py
"""
Map REDCap genetic_information instrument fields to LinkML format.

This is a non-repeating (top-level) instrument in REDCap. All fields
sit at the top level of the flat REDCap record alongside demographics.
"""


def map_genetic_information(record):
    """
    Map REDCap record data to the GeneticInformation LinkML class format.

    Args:
        record (dict): The flat REDCap record data.

    Returns:
        dict: The mapped data in LinkML format, or None if the instrument
              has no data (all fields empty).
    """
    # Handle the variant_expression checkbox field.
    # REDCap exports checkboxes as variant_expression___chgvs = "1",
    # variant_expression___phgvs = "0", etc.
    variant_expression = _resolve_checkbox(record, "variant_expression", [
        "chgvs", "phgvs", "ghgvs", "1",
    ])

    mapped = {
        "completion_date_genetic": record.get("completion_date_genetic", ""),
        "geneticonfirmation": record.get("geneticonfirmation", ""),
        "geneticevaluationmonth": record.get("geneticevaluationmonth", ""),
        "geneticevaluationyear": record.get("geneticevaluationyear", ""),
        "genetic_diagnosis_g": record.get("genetic_diagnosis_g", ""),
        "g_iei_deficiency": record.get("g_iei_deficiency", ""),
        "other_non_g_iei": record.get("other_non_g_iei", ""),
        "gen_report": record.get("gen_report", ""),
        "g_other_iei_deficiency": record.get("g_other_iei_deficiency", ""),
        "g_other_iei_def_text": record.get("g_other_iei_def_text", ""),
        "interpretation_status": record.get("interpretation_status", ""),
        "loinc_81304_8": record.get("loinc_81304_8", ""),
        "loinc_81304_8_other": record.get("loinc_81304_8_other", ""),
        "loinc_48018_6": record.get("loinc_48018_6", ""),
        "loinc_lp7824_8": record.get("loinc_lp7824_8", ""),
        "variant_expression": variant_expression,
        "change_hgvsexpress": record.get("change_hgvsexpress", ""),
        "loinc_81290_9": record.get("loinc_81290_9", ""),
        "loinc_48004_6": record.get("loinc_48004_6", ""),
        "loinc_48005_3": record.get("loinc_48005_3", ""),
        "variant_validation": record.get("variant_validation", ""),
        "geno_0000141": record.get("geno_0000141", ""),
        "geno_0000141_other": record.get("geno_0000141_other", ""),
        "loinc_48019_4": record.get("loinc_48019_4", ""),
        "loinc_48019_4_other": record.get("loinc_48019_4_other", ""),
        "loinc_53034_5": record.get("loinc_53034_5", ""),
        "loinc_53034_5_other": record.get("loinc_53034_5_other", ""),
        "protein_funct": record.get("protein_funct", ""),
        "pther_prot_expr": record.get("pther_prot_expr", ""),
        "loinc_53037_8": record.get("loinc_53037_8", ""),
        "clinician_verified": record.get("clinician_verified", ""),
    }

    return mapped


def _resolve_checkbox(record, field_name, suffixes):
    """
    Resolve a REDCap checkbox field to a list of selected values.

    REDCap exports checkboxes as separate columns:
        field___suffix1 = "1"  (checked)
        field___suffix2 = "0"  (unchecked)

    Returns:
        str: Comma-separated selected suffixes, or "" if none selected.
    """
    selected = []
    for suffix in suffixes:
        key = f"{field_name}___{suffix}"
        if record.get(key) == "1":
            selected.append(suffix)
    return ",".join(selected) if selected else ""
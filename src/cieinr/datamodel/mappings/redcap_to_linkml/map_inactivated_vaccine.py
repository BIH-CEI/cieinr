# src/cieinr/datamodel/mappers/redcap_to_linkml/map_inactivated_vaccine.py

def map_inactivated_vaccine(record):
    """
    Map REDCap record data to the InactivatedVaccineHistory LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "completion_of_inact_vax": record.get("completion_of_inact_vax", ""),  # Date of completing this form?
        "inactiv_vax": record.get("inactiv_vax", ""),  # Please indicate what type of vaccine the participa
        "inactiv_vax_other": record.get("inactiv_vax_other", ""),  # Indicate 'other' inactive vaccination [VO]
        "inactiv_vax_dose": record.get("inactiv_vax_dose", ""),  # How many doses of the selected inactivated vaccine
        "inactiv_vax_ae": record.get("inactiv_vax_ae", ""),  # Was an adverse event observed after this vaccine?
        "inactiv_vax_ae_other": record.get("inactiv_vax_ae_other", ""),  # Please search in the HPO for the type of adverse e
        "inactiv_vax_ae_severity": record.get("inactiv_vax_ae_severity", ""),  # How severe were the observed adverse events for th
        "vo_0000424_before_pneu": record.get("vo_0000424_before_pneu", ""),  # What was the Pneumococcal response measured before
        "inactiv_vax_response": record.get("inactiv_vax_response", ""),  # Post- vaccination response evaluation
        "other_post_vaccine": record.get("other_post_vaccine", ""),  # please specify
        "reevalmonth": record.get("reevalmonth", ""),  # Month
        "reevalyear": record.get("reevalyear", ""),  # Year
        "file_pneumo_response": record.get("file_pneumo_response", ""),  # Please upload specific immune response to Pneumoco
    }

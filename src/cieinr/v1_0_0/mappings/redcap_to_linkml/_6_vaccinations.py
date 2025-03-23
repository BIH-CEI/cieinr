"""
Mapping function for inactivated_vaccine_history_and_specific_immune_re REDCap data to LinkML format for CIEINR.
"""

def map_inactivated_vaccine(record):
    """
    Map REDCap record data to the InactivatedVaccine LinkML class format.
    
    Args:
        record (dict): The REDCap record data.
        
    Returns:
        dict: The mapped data in LinkML format.
    """
    return {
        "completion_of_inact_vax": record.get("completion_of_inact_vax", ""),
        "inactiv_vax": record.get("inactiv_vax", ""),
        "inactiv_vax_other": record.get("inactiv_vax_other", ""),
        "inactiv_vax_dose": record.get("inactiv_vax_dose", ""),
        "inactiv_vax_ae": record.get("inactiv_vax_ae", ""),
        "inactiv_vax_ae_other": record.get("inactiv_vax_ae_other", ""),
        "inactiv_vax_ae_severity": record.get("inactiv_vax_ae_severity", ""),
        "vo_0000424_before_pneu": record.get("vo_0000424_before_pneu", ""),
        "inactiv_vax_response": record.get("inactiv_vax_response", ""),
        "inactiv_vax_response_date": record.get("inactiv_vax_response_date", ""),
        "other_specific_response": record.get("other_specific_response", ""),
        "file_pneumo_response": record.get("file_pneumo_response", "")
    }
    
    
"""
Mapping function for live_vaccine_and_specific_immune_response REDCap data to LinkML format for CIEINR.
"""

def map_live_vaccine(record):
    """
    Map REDCap record data to the LiveVaccine LinkML class format.
    
    Args:
        record (dict): The REDCap record data.
        
    Returns:
        dict: The mapped data in LinkML format.
    """
    return {
        "completion_live_vax": record.get("completion_live_vax", ""),
        "live_vax": record.get("live_vax", ""),
        "live_vax_other": record.get("live_vax_other", ""),
        "live_vax_dosages": record.get("live_vax_dosages", ""),
        "live_vax_ae": record.get("live_vax_ae", ""),
        "ae_live_vax": record.get("ae_live_vax", ""),
        "live_vax_ae_other": record.get("live_vax_ae_other", ""),
        "live_vax_ae_severity": record.get("live_vax_ae_severity", ""),
        "live_vax_response": record.get("live_vax_response", ""),
        "other_specific_live_response": record.get("other_specific_live_response", ""),
        "life_vax_response_date": record.get("life_vax_response_date", "")
    }

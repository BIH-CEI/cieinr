# src/cieinr/datamodel/mappers/redcap_to_linkml/map_vaccine_history.py

def map_vaccine_history(record):
    """
    Map REDCap record data to the VaccineHistory LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "completion_vax": record.get("completion_vax", ""),  # Date of completing this form.
        "vax_administered": record.get("vax_administered", ""),  # Which vaccine was administered?
        "vax_other": record.get("vax_other", ""),  # Please indicate 'other' vaccine? [VO]
        "vax_dosages": record.get("vax_dosages", ""),  # How many doses of the selected vaccine were receiv
        "vax_ae": record.get("vax_ae", ""),  # Did the patient develop a vaccine-associated infec
        "ae_vax": record.get("ae_vax", ""),  # Were any other adverse events observed?
        "vax_ae_other": record.get("vax_ae_other", ""),  # Please search for the type of adverse event
        "vax_ae_severity": record.get("vax_ae_severity", ""),  # How severe were the observed adverse events for th
        "vax_response": record.get("vax_response", ""),  # Antibody response to the selected vaccine
        "other_specific_response": record.get("other_specific_response", ""),  # Please specify the other antibody response:
        "imrespmonth": record.get("imrespmonth", ""),  # Month
        "imrespyear": record.get("imrespyear", ""),  # Year
        "measles_response": record.get("measles_response", ""),  # Measles antibody response
        "mumps_response": record.get("mumps_response", ""),  # Mumps antibody response
        "rubella_response": record.get("rubella_response", ""),  # Rubella antibody response
        "diphtheria_response": record.get("diphtheria_response", ""),  # Diphtheria antibody response
        "tetanus_response": record.get("tetanus_response", ""),  # Tetanus antibody response
        "pertussis_response": record.get("pertussis_response", ""),  # Pertussis antibody response
    }

# src/cieinr/datamodel/mappers/redcap_to_linkml/map_infections_initial.py

def map_infections_initial(record):
    """
    Map REDCap record data to the InfectionsInitial LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "date_infection_form": record.get("date_infection_form", ""),  # Date of completing this form.
        "type_of_infection": record.get("type_of_infection", ""),  # Please select the infection type that the particip
        "snomedct_61274003": record.get("snomedct_61274003", ""),  # Opportunistic Infection
        "snomedct_21483005": record.get("snomedct_21483005", ""),  # Central Nervous System (CNS) Infection
        "snomedct_81745001": record.get("snomedct_81745001", ""),  # Eye Infection
        "snomedct_385383008": record.get("snomedct_385383008", ""),  # Ear, Nose and Throat (ENT) Infection
        "snomedct_127856007": record.get("snomedct_127856007", ""),  # Skin and Soft Tissue Infection
        "snomedct_110522009": record.get("snomedct_110522009", ""),  # Bone and Joint Infection
        "snomedct_20139000": record.get("snomedct_20139000", ""),  # Respiratory Infection
        "snomedct_303699009": record.get("snomedct_303699009", ""),  # Gastrointestinal Infection
        "snomedct_21514008": record.get("snomedct_21514008", ""),  # Genitourinary Infections
        "snomedct_31099001": record.get("snomedct_31099001", ""),  # Systemic Infection
        "other_infection_hpo": record.get("other_infection_hpo", ""),  # Other Infection [HPO]
        "other_infection_mondo": record.get("other_infection_mondo", ""),  # Other Infection, if unable to find in HPO search  
        "other_infection": record.get("other_infection", ""),  # If other infection was not found using [MONDO] or 
        "infection_severity": record.get("infection_severity", ""),  # What was the maximum severity of the infection?
        "causing_agent": record.get("causing_agent", ""),  # What type of infection was detected in the patient
        "causing_agent_viral": record.get("causing_agent_viral", ""),  # If applicable, what was the virus causing the infe
        "causing_agent_bacterial": record.get("causing_agent_bacterial", ""),  # If applicable, what bacteria caused the infection?
        "causing_agent_mycotic": record.get("causing_agent_mycotic", ""),  # If applicable, what fungal/mycotic infectious agen
        "causing_organism_other": record.get("causing_organism_other", ""),  # What was the organism causing the infection?
        "infection_temp_pattern": record.get("infection_temp_pattern", ""),  # Was a temporal pattern observed in the infection?
        "infection_times_obseverd": record.get("infection_times_obseverd", ""),  # How many times did the patient have this infection
        "infection_date": record.get("infection_date", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_2": record.get("infection_date_2", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_3": record.get("infection_date_3", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_4": record.get("infection_date_4", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_5": record.get("infection_date_5", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_6": record.get("infection_date_6", ""),  # Year-month of Infection. If the date is unknown, u
        "more6inf": record.get("more6inf", ""),  # If the participant had infections more than 6 time
        "additional_comments": record.get("additional_comments", ""),  # Please provide any additional information or comme
    }

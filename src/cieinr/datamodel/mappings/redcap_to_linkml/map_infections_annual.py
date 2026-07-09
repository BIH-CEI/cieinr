# src/cieinr/datamodel/mappers/redcap_to_linkml/map_infections_annual.py

def map_infections_annual(record):
    """
    Map REDCap record data to the InfectionsAnnual LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "date_infection_form_v2": record.get("date_infection_form_v2", ""),  # Date of completing this form.
        "type_of_infection_v2": record.get("type_of_infection_v2", ""),  # Please select the types of infection that the part
        "snomedct_61274003_v2": record.get("snomedct_61274003_v2", ""),  # Opportunistic Infection
        "snomedct_21483005_v2": record.get("snomedct_21483005_v2", ""),  # Central Nervous System (CNS) Infection
        "snomedct_81745001_v2": record.get("snomedct_81745001_v2", ""),  # Eye Infection
        "snomedct_385383008_v2": record.get("snomedct_385383008_v2", ""),  # Ear, Nose and Throat (ENT) Infection
        "snomedct_127856007_v2": record.get("snomedct_127856007_v2", ""),  # Skin and Soft Tissue Infection
        "snomedct_110522009_v2": record.get("snomedct_110522009_v2", ""),  # Bone and Joint Infection
        "snomedct_20139000_v2": record.get("snomedct_20139000_v2", ""),  # Respiratory Infection
        "snomedct_303699009_v2": record.get("snomedct_303699009_v2", ""),  # Gastrointestinal Infection
        "snomedct_21514008_v2": record.get("snomedct_21514008_v2", ""),  # Genitourinary Infections
        "snomedct_31099001_v2": record.get("snomedct_31099001_v2", ""),  # Systemic Infection
        "other_infection_hpo_v2": record.get("other_infection_hpo_v2", ""),  # Other Infection [HPO]
        "other_infection_mondo_v2": record.get("other_infection_mondo_v2", ""),  # Other Infection [MONDO]
        "infection_severity_v2": record.get("infection_severity_v2", ""),  # What was severity for this infection for the last 
        "causing_agent_v2": record.get("causing_agent_v2", ""),  # What kind of  agent was causing the infection?
        "causing_agent_viral_v2": record.get("causing_agent_viral_v2", ""),  # If applicable, what was the causing viral infectio
        "causing_agent_bacterial_v2": record.get("causing_agent_bacterial_v2", ""),  # If applicable, what was the causing bacterial infe
        "causing_agent_mycotic_v2": record.get("causing_agent_mycotic_v2", ""),  # If applicable, what was the fungal/mycotic infecti
        "causing_organism_other_v2": record.get("causing_organism_other_v2", ""),  # What was the causing organism of the infection?
        "infection_temp_pattern_v2": record.get("infection_temp_pattern_v2", ""),  # Was a temporal pattern observed in this infection?
        "infection_times_obseverd_v2": record.get("infection_times_obseverd_v2", ""),  # How many times was this type of infection observed
        "infection_date_v2": record.get("infection_date_v2", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_2_v2": record.get("infection_date_2_v2", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_3_v2": record.get("infection_date_3_v2", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_4_v2": record.get("infection_date_4_v2", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_5_v2": record.get("infection_date_5_v2", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_6_v2": record.get("infection_date_6_v2", ""),  # Year-month of Infection. If the date is unknown, u
        "infection_date_7_v2": record.get("infection_date_7_v2", ""),  # Year-month of Infection. If the date is unknown, u
    }

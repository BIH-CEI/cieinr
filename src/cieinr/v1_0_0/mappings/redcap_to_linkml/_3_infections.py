"""
Mapping function for infections_initial_form REDCap data to LinkML format for CIEINR.
"""

def map_infections(record):
    """
    Map REDCap record data to the InfectionsInitial LinkML class format.
    
    Args:
        record (dict): The REDCap record data
        
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        # Main infection type
        "type_of_infection": record.get("type_of_infection", ""),
        
        # Specific infection types
        "snomedct_61274003": record.get("snomedct_61274003", ""),  # Opportunistic Infection
        "snomedct_21483005": record.get("snomedct_21483005", ""),  # CNS Infection
        "snomedct_81745001": record.get("snomedct_81745001", ""),  # Eye Infection
        "snomedct_385383008": record.get("snomedct_385383008", ""),  # ENT Infection
        "snomedct_127856007": record.get("snomedct_127856007", ""),  # Skin and Soft Tissue Infection
        "snomedct_110522009": record.get("snomedct_110522009", ""),  # Bone and Joint Infection
        "snomedct_20139000": record.get("snomedct_20139000", ""),  # Respiratory Infection
        "snomedct_303699009": record.get("snomedct_303699009", ""),  # Gastrointestinal Infection
        "snomedct_21514008": record.get("snomedct_21514008", ""),  # Genitourinary Infections
        "snomedct_31099001": record.get("snomedct_31099001", ""),  # Systemic Infection
        
        # Additional infection data
        "infection_severity": record.get("infection_severity", ""),
        "infection_temp_pattern": record.get("infection_temp_pattern", ""),
        "infection_times_obseverd": record.get("infection_times_obseverd", ""),
        "causing_agent": record.get("causing_agent", ""),
        "causing_agent_viral": record.get("causing_agent_viral", ""),
        "causing_agent_bacterial": record.get("causing_agent_bacterial", ""),
        "causing_agent_mycotic": record.get("causing_agent_mycotic", ""),
        "causing_organism_other": record.get("causing_organism_other", ""),
        
        # infection dates
        "infection_date": record.get("infection_date", ""),
        "infection_date_2": record.get("infection_date_2", ""),
        "infection_date_3": record.get("infection_date_3", ""),
        "infection_date_4": record.get("infection_date_4", ""),
        "infection_date_5": record.get("infection_date_5", ""),
        "infection_date_6": record.get("infection_date_6", ""),
        "infection_date_7": record.get("infection_date_7", ""),
        "infection_date_8": record.get("infection_date_8", ""),
        "infection_date_9": record.get("infection_date_9", ""),
        "infection_date_10": record.get("infection_date_10", ""),
        
        # Form completion status
        "infections_initial_form_complete": record.get("infections_initial_form_complete", "0")
    }
    
def map_infections_annual(record):
    """
    Map REDCap data for the Infections Annual form to LinkML format.
    """
    return {
        "date_infection_form_v2": record.get("date_infection_form_v2", ""),
        "type_of_infection_v2": record.get("type_of_infection_v2", ""),
        "none_inf_v2": record.get("none_inf_v2", ""),
        "snomedct_61274003_v2": record.get("snomedct_61274003_v2", ""),
        "snomedct_21483005_v2": record.get("snomedct_21483005_v2", ""),
        "snomedct_81745001_v2": record.get("snomedct_81745001_v2", ""),
        "snomedct_385383008_v2": record.get("snomedct_385383008_v2", ""),
        "snomedct_127856007_v2": record.get("snomedct_127856007_v2", ""),
        "snomedct_110522009_v2": record.get("snomedct_110522009_v2", ""),
        "snomedct_20139000_v2": record.get("snomedct_20139000_v2", ""),
        "snomedct_303699009_v2": record.get("snomedct_303699009_v2", ""),
        "snomedct_21514008_v2": record.get("snomedct_21514008_v2", ""),
        "snomedct_31099001_v2": record.get("snomedct_31099001_v2", ""),
        "other_infection_hpo_v2": record.get("other_infection_hpo_v2", ""),
        "other_infection_mondo_v2": record.get("other_infection_mondo_v2", ""),
        "infection_severity_v2": record.get("infection_severity_v2", ""),
        "causing_agent_v2": record.get("causing_agent_v2", ""),
        "causing_agent_viral_v2": record.get("causing_agent_viral_v2", ""),
        "causing_agent_bacterial_v2": record.get("causing_agent_bacterial_v2", ""),
        "causing_agent_mycotic_v2": record.get("causing_agent_mycotic_v2", ""),
        "causing_organism_other_v2": record.get("causing_organism_other_v2", ""),
        "infection_temp_pattern_v2": record.get("infection_temp_pattern_v2", ""),
        "infection_times_obseverd_v2": record.get("infection_times_obseverd_v2", ""),
        "infection_date_v2": record.get("infection_date_v2", ""),
        "infection_date_2_v2": record.get("infection_date_2_v2", ""),
        "infection_date_3_v2": record.get("infection_date_3_v2", ""),
        "infection_date_4_v2": record.get("infection_date_4_v2", ""),
        "infection_date_5_v2": record.get("infection_date_5_v2", ""),
        "infection_date_6_v2": record.get("infection_date_6_v2", ""),
        "infection_date_7_v2": record.get("infection_date_7_v2", ""),
        "infections_annual_form_complete": record.get("infections_annual_form_complete", "0")
    }
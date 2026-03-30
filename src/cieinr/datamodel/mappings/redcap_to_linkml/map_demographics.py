# src/cieinr/datamodel/mappers/redcap_to_linkml/map_demographics.py

def map_demographics(record):
    """
    Map REDCap record data to the PatientDemographicsInitial LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "assigned_centerid": record.get("assigned_centerid", ""),  # Enter the assigned Number of your Center in the Ca
        "visit_date_demographics": record.get("visit_date_demographics", ""),  # Enter the date for this visit
        "type_participant": record.get("type_participant", ""),  # Indicate the type of participant
        "record_id_no_dag": record.get("record_id_no_dag", ""),  # [Hidden] Removes DAG component of record ID, if ne
        "record_id_leading_zeroes": record.get("record_id_leading_zeroes", ""),  # [Hidden] Add leading zeroes to record ID number, i
        "national_iei_registry_id": record.get("national_iei_registry_id", ""),  # National IEI Registry ID
        "province_demographics": record.get("province_demographics", ""),  # Please indicate your province or territory:
        "birth_month": record.get("birth_month", ""),  # Month
        "birth_year": record.get("birth_year", ""),  # Year
        "usidnet_id": record.get("usidnet_id", ""),  # USIDNET ID#
        "esid_id": record.get("esid_id", ""),  # ESID ID#
        "pidtc_id": record.get("pidtc_id", ""),  # PIDTC ID#
        "cibmtr": record.get("cibmtr", ""),  # CIBMTR ID#
        "other_study_id": record.get("other_study_id", ""),  # Other Study ID#
        "enrolling_phys_demo": record.get("enrolling_phys_demo", ""),  # Name of Physician/NP/Provider Enrolling this Patie
        "form_completion_demo": record.get("form_completion_demo", ""),  # Name and role of person completing this data entry
        "genetic_diagnosis": record.get("genetic_diagnosis", ""),  # Is a diagnosis available?
        "iei_deficiency_basic": record.get("iei_deficiency_basic", ""),  # Please search for the IEI diagnosis:
        "other_iei_deficiency": record.get("other_iei_deficiency", ""),  # If not found in the list, please try searching in 
        "other_iei_def_text_v2_v2": record.get("other_iei_def_text_v2_v2", ""),  # ... or specify further, if not found
        "clinician_verification": record.get("clinician_verification", ""),  # Has the diagnostic information that you entered be
        "immunomonthstatus": record.get("immunomonthstatus", ""),  # Month
        "immunoyearstatus": record.get("immunoyearstatus", ""),  # Year
        "immunomonthonset": record.get("immunomonthonset", ""),  # Month
        "immunoyearonset": record.get("immunoyearonset", ""),  # Year
        "igrt_basic": record.get("igrt_basic", ""),  # Has the patient ever received Immunoglobulin repla
        "hct_basic_form": record.get("hct_basic_form", ""),  # Has the patient received hematopoietic stem cell t
        "syst_inf_basic": record.get("syst_inf_basic", ""),  # Has the patient experienced recurrent severe, chro
        "type_inf": record.get("type_inf", ""),  # If possible, briefly indicate type of infections
        "conditions_basic": record.get("conditions_basic", ""),  # Has the patient experienced any of the following c
        "important_basic": record.get("important_basic", ""),  # Please include additional important information ab
    }

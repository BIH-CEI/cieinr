"""
Mapping blocks for the CIEINR v1.0.0 data model.

These mappings define how fields in the CIEINR data model map to fields
required for phenopacket construction. Similar to the RareLink CDM mappings,
these are used by DataProcessor to access the correct fields in the data.
"""

# Individual block mapping
INDIVIDUAL_BLOCK = {
    "id_field": "record_id",
    "date_of_birth_field": "patient_demographics_initial_form.snomedct_184099003",
    "time_at_last_encounter_field": "patient_demographics_initial_form.last_encounter_date",
    "sex_field": "patient_demographics_initial_form.snomedct_281053000",
    "karyotypic_sex_field": "patient_demographics_initial_form.karyotypic_sex",
    "gender_field": "patient_demographics_initial_form.gender_identity",
}

# Vital status block mapping
VITAL_STATUS_BLOCK = {
    "status_field": "patient_demographics_initial_form.vital_status",
    "status_date_field": "patient_demographics_initial_form.date_of_death",
    "causes_of_death_field": "patient_demographics_initial_form.causes_of_death",
}

# Disease block mapping
DISEASE_BLOCK = {
    "term_field": "basic_form.iei_deficiency_basic",
    "onset_date_field": "patient_demographics_initial_form.snomedct_298059007",
    "diagnosis_date_field": "patient_demographics_initial_form.snomedct_432213005",
    "clinical_status_field": "patient_demographics_initial_form.disease_status",
}

# Phenotypic features block mapping
PHENOTYPIC_FEATURES_BLOCK = {
    "redcap_repeat_instrument": "infections_initial_form",
    "type_field": "infections_initial_form.type_of_infection",
    "specific_type_field": None,  # Dynamically determined based on type_field
    "severity_field": "infections_initial_form.infection_severity",
    "temp_pattern_field": "infections_initial_form.infection_temp_pattern",
    "temporal_pattern_field": "infections_initial_form.infection_times_obseverd",
}

# Code systems used in the data model
CIEINR_CODE_SYSTEMS = [
    {
        "id": "hp",
        "name": "Human Phenotype Ontology",
        "url": "http://purl.obolibrary.org/obo/hp.owl",
        "version": "2023-06-04",
        "namespace_prefix": "HP"
    },
    {
        "id": "mondo",
        "name": "Mondo Disease Ontology",
        "url": "http://purl.obolibrary.org/obo/mondo.owl",
        "version": "2023-05-31", 
        "namespace_prefix": "MONDO"
    },
    {
        "id": "ncit",
        "name": "NCI Thesaurus",
        "url": "http://purl.obolibrary.org/obo/ncit.owl",
        "version": "2023-03-27",
        "namespace_prefix": "NCIT"
    },
    {
        "id": "snomedct",
        "name": "SNOMED Clinical Terms",
        "url": "http://snomed.info/sct",
        "version": "2023-03",
        "namespace_prefix": "SNOMEDCT"
    }
]

# Mapping dictionaries for code conversions
MAPPING_DICTS = [
    {
        "name": "map_sex",
        "mapping": {
            "snomedct_248152002": "FEMALE",
            "snomedct_248153007": "MALE",
            "snomedct_32570691000036108": "OTHER_SEX",
            "": "UNKNOWN_SEX"
        },
    },
    {
        "name": "map_vital_status",
        "mapping": {
            "snomedct_438949009": "ALIVE",
            "snomedct_419099009": "DECEASED",
            "snomedct_185924006": "UNKNOWN_STATUS",
            "": "UNKNOWN_STATUS"
        },
    },
    {
        "name": "map_clinical_status",
        "mapping": {
            "active": "ACTIVE",
            "recurrence": "RECURRENCE",
            "remission": "REMISSION",
            "resolved": "RESOLVED",
            "": "UNKNOWN_STATUS"
        }
    }
]

def get_mapping_by_name(name: str, to_boolean: bool = False):
    """
    Get a mapping dictionary by name.
    
    Args:
        name: Name of the mapping to retrieve
        to_boolean: Whether to convert string values "true"/"false" to boolean
        
    Returns:
        Dictionary with the mapping
        
    Raises:
        KeyError: If no mapping with the given name exists
    """
    for mapping_dict in MAPPING_DICTS:
        if mapping_dict["name"] == name:
            mapping = mapping_dict["mapping"]
            if to_boolean:
                return {key: value.lower() == "true" for key, value in mapping.items()}
            return mapping
    raise KeyError(f"No mapping found for name: {name}")
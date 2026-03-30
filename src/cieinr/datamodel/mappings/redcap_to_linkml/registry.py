"""
Registry of mapping functions for the CIEINR project.
This file defines the mapping from REDCap instruments to their LinkML schema equivalents.
"""

from ._1_basic_form import map_basic_form
from ._2_patient_demographics import map_patient_demographics  
from ._3_infections import map_infections
from ._5_conditions import map_conditions
from ._6_vaccinations import map_inactivated_vaccine, map_live_vaccine
from ._7_labs_initial import map_cbc, map_lymphopheno_initial, map_lymphfunc_initial
from ._9_genetics import map_genetic_findings


# Registry of mapping functions with configuration
MAPPING_FUNCTIONS = {
    "basic_form": {
        "mapper": map_basic_form,
        "is_repeating": False
    },
    "patient_demographics_initial_form": {
        "mapper": map_patient_demographics,
        "is_repeating": False
    },
    "infections_initial_form": {
        "mapper": map_infections,
        "is_repeating": True
    },
    "genetic_information": {
        "mapper": map_genetic_findings,
        "is_repeating": True,
        "output_key": "genetic_findings" 
    },
    "patients_systemic_or_organ_specific_conditions":{
        "mapper": map_conditions,
        "is_repeating": True,
    },
    "inactivated_vaccine_history_and_specific_immune_re": {
        "mapper": map_inactivated_vaccine,
        "is_repeating": True
    },
    "live_vaccine_and_specific_immune_response": {
        "mapper": map_live_vaccine,
        "is_repeating": True
    },
    "cbc": {
        "mapper": map_cbc,
        "is_repeating": True
    },
    "lymphocytes_phenotype": {
        "mapper": map_lymphopheno_initial,
        "is_repeating": True
    },
    "lymphocyte_functionnk_cytotoxicity": {
        "mapper": map_lymphfunc_initial,
        "is_repeating": True
    }
}
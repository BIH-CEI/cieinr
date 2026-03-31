"""
Registry of mapping functions for the CIEINR project.
This file defines the mapping from REDCap instruments to their LinkML schema equivalents.
"""

from .map_demographics import map_demographics
from .map_cbc import map_cbc
from .map_conditions import map_conditions
from .map_infections_initial import map_infections_initial
from .map_infections_annual import map_infections_annual
from .map_lymphocyte_function import map_lymphocyte_function
from .map_lymphocytes_phenotype import map_lymphocytes_phenotype
from .map_vaccinations import map_inactivated_vaccine, map_live_vaccine
from .map_vaccine_history import map_vaccine_history
from .map_genetic_information import map_genetic_information

# Registry of mapping functions with configuration
MAPPING_FUNCTIONS = {
    "patient_demographics_initial_form": {
        "mapper": map_demographics,
        "is_repeating": False
    },
    "infections_initial_form": {
        "mapper": map_infections_initial,
        "is_repeating": True
    },
    "infections_annual_form": {
        "mapper": map_infections_annual,
        "is_repeating": True
    },
    "genetic_information": {
        "mapper": map_genetic_information,
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
        "mapper": map_lymphocytes_phenotype,
        "is_repeating": True
    },
    "lymphocyte_functionnk_cytotoxicity": {
        "mapper": map_lymphocyte_function,
        "is_repeating": True
    }
}
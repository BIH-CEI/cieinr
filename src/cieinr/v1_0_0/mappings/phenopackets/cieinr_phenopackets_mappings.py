"""
CIEINR Phenopackets Mappings

This module provides the mapping configurations for converting CIEINR data to Phenopackets,
ensuring compatibility with RareLink's phenopacket generation engine.
"""

from typing import Dict, Any
from dataclasses import dataclass
import logging
from pathlib import Path
import os
from dotenv import load_dotenv

# Try loading environment variables
try:
    # Load from .env file if it exists
    load_dotenv()
except Exception as e:
    print(f"Warning: Could not load .env file: {e}")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class CodeSystem:
    """Class for defining a code system."""
    name: str
    prefix: str
    version: str
    url: str
    iri_prefix: str

# Create a dictionary of code systems instead of using CodeSystemsContainer
# This avoids the import issues with the RareLink's CodeSystemsContainer class
CIEINR_CODE_SYSTEMS_DICT = {
    "hpo": CodeSystem(
        name="Human Phenotype Ontology",
        prefix="HPO",
        version="2024-08-13",
        url="http://purl.obolibrary.org/obo/hp.owl",
        iri_prefix="http://purl.obolibrary.org/obo/HP_"
    ),
    "loinc": CodeSystem(
        name="Logical Observation Identifiers Names and Codes",
        prefix="LOINC",
        version="2.78",
        url="https://loinc.org",
        iri_prefix="http://loinc.org"
    ),
    "icd10cm": CodeSystem(
        name="ICD-10 Clinical Modification",
        prefix="ICD10CM",
        version="2023",
        url="https://www.cdc.gov/nchs/icd/icd10cm.htm",
        iri_prefix="http://hl7.org/fhir/sid/icd-10-cm"
    ),
    "icd11": CodeSystem(
        name="International Classification of Diseases, Eleventh Revision",
        prefix="ICD11",
        version="2024-09-01",
        url="https://icd.who.int/en",
        iri_prefix="http://hl7.org/fhir/sid/icd-11"
    ),
    "mondo": CodeSystem(
        name="Monarch Disease Ontology",
        prefix="MONDO",
        version="2024-09-03",
        url="https://purl.obolibrary.org/obo/MONDO/",
        iri_prefix="http://purl.obolibrary.org/obo/MONDO_"
    ),
    "omim": CodeSystem(
        name="Online Mendelian Inheritance",
        prefix="OMIM",
        version="2024-09-12",
        url="https://omim.org/",
        iri_prefix="https://www.omim.org/entry/"
    ),
    "orpha": CodeSystem(
        name="Orphanet Rare Disease Ontology",
        prefix="ORPHA",
        version="2024-09-12",
        url="https://www.orpha.net/",
        iri_prefix="https://www.orpha.net/ORDO/Orphanet_"
    ),
    "ncit": CodeSystem(
        name="NCI Thesaurus OBO Edition",
        prefix="NCIT",
        version="24.04e",
        url="https://ncit.nci.nih.gov/",
        iri_prefix="http://purl.obolibrary.org/obo/NCIT_"
    ),
    "uo": CodeSystem(
        name="Units of Measurement Ontology",
        prefix="UO",
        version="2024-09-12",
        url="https://www.ontobee.org/ontology/UO",
        iri_prefix="http://purl.obolibrary.org/obo/UO_"
    ),
    "hgnc": CodeSystem(
        name="HUGO Gene Nomenclature Committee",
        prefix="HGNC",
        version="2024-08-23",
        url="https://www.genenames.org/",
        iri_prefix="https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/"
    ),
    "ncbitaxon": CodeSystem(
        name="NCBI Taxonomy Ontology",
        prefix="NCBITaxon",
        version="2024-07-03",
        url="https://www.ncbi.nlm.nih.gov/taxonomy",
        iri_prefix="http://purl.obolibrary.org/obo/NCBITaxon_"
    )
}

# Define mapping blocks for CIEINR data
INDIVIDUAL_BLOCK = {
    "id_field": "record_id",
    "date_of_birth_field": "patient_demographics_initial_form.snomedct_184099003",
    "time_at_last_encounter_field": "patient_demographics_initial_form.visit_date_demographics",
    "sex_field": None,  # Default to UNKNOWN_SEX
    "karyotypic_sex_field": None,  # Default to UNKNOWN_KARYOTYPE
    "gender_field": None,  # Default to None
}

VITAL_STATUS_BLOCK = {
    "instrument_name": "__dummy__",  # Special marker handled by our patches
    "status_field": "_default_",  # Will be handled to default to UNKNOWN_STATUS
    "time_of_death_field": None,
    "cause_of_death_field": None,
}

DISEASE_BLOCK = {
    "term_field_1": "basic_form.iei_deficiency_basic",
    "term_field_2": None,
    "term_field_3": None,
    "term_field_4": None,
    "term_field_5": None,
    "excluded_field": None,
    "onset_date_field": "patient_demographics_initial_form.snomedct_298059007",
    "onset_category_field": None,
    "primary_site_field": None,
}

PHENOTYPIC_FEATURES_BLOCK = {
    "redcap_repeat_instrument": "infections_initial_form",
    "type_field": "type_of_infection",
    "excluded_field": None,
    "onset_date_field": None,
    "resolution_field": None,
    "severity_field": "infection_severity",
    "modifier_temp_pattern_field": "infection_temp_pattern",
    "modifier_field_1": None,
    "modifier_field_2": None,
    "modifier_field_3": None,
    "modifier_field_4": None,
    "modifier_field_5": None,
    "evidence_field": None,
}

# Create label dictionaries from CIEINR's enum classes
def load_iuis_labels() -> Dict[str, str]:
    """
    Load labels for IUIS 2024 MONDO codes.
    
    Returns:
        Dictionary mapping MONDO codes to their human-readable descriptions
    """
    try:
        # Fallback: try to read from the source file
        labels = {}
        path = Path("src/cieinr/v1_0_0/linkml_schemas/iuis2024_redcap.txt")
        
        if path.exists():
            with open(path, "r") as f:
                for line in f:
                    entries = line.split(" | ")
                    for entry in entries:
                        if "," in entry:
                            code, label = entry.split(",", 1)
                            code = code.strip()
                            label = label.strip()
                            labels[code] = label
                            
            return labels
        else:
            logger.warning(f"File not found: {path}")
            
            # Provide a minimal set of known labels as fallback
            return {
                "mondo_0007843": "Kabuki Syndrome 1 due to KMT2D deficiency",
                "hp_0002383": "Encephalitis",
                "mondo_0043653": "Herpes Labialis (cold sores)",
                "hp_0002090": "Pneumonia"
            }
    except Exception as e:
        logger.error(f"Error loading IUIS labels: {e}")
        return {}

# Define the mapping dictionaries
MAPPING_DICTS = [
    {
        "name": "map_sex",
        "mapping": {
            "snomedct_248152002": "FEMALE",
            "snomedct_248153007": "MALE",
            "snomedct_184115007": "UNKNOWN_SEX",
            "snomedct_32570691000036108": "OTHER_SEX",
            "snomedct_1220561009": "UNKNOWN_SEX",
            "": "UNKNOWN_SEX"
        },
    },
    {
        "name": "map_vital_status",
        "mapping": {
            "snomedct_438949009": "ALIVE", 
            "snomedct_419099009": "DECEASED",
            "snomedct_399307001": "UNKNOWN_STATUS",
            "snomedct_185924006": "UNKNOWN_STATUS",
            "snomedct_261665006": "UNKNOWN_STATUS",
            "": "UNKNOWN_STATUS"
        },
    },
    {
        "name": "map_disease_verification_status",
        "mapping": {
            "hl7fhir_unconfirmed": "",
            "hl7fhir_provisional": "",
            "hl7fhir_differential": "",
            "hl7fhir_confirmed": "false",
            "hl7fhir_refuted": "true",
            "hl7fhir_entered-in-error": ""
        },
    },
    {
        "name": "map_infection_severity",
        "mapping": {
            "hp_0012825": "MILD", 
            "hp_0012826": "MODERATE",
            "hp_0012828": "SEVERE",
            "": "UNKNOWN"
        }
    },
    {
        "name": "map_infection_temporal_pattern",
        "mapping": {
            "hp_0011009": "ACUTE",
            "hp_0011011": "SUBACUTE",
            "hp_0011010": "CHRONIC",
            "hp_0031796": "RECURRENT",
            "": "UNKNOWN"
        }
    }
]

def get_mapping_by_name(name: str) -> Dict[str, str]:
    """
    Get a mapping dictionary by name.
    
    Args:
        name: Name of the mapping to retrieve
        
    Returns:
        Dictionary with the mapping
        
    Raises:
        KeyError: If no mapping with the given name exists
    """
    for mapping_dict in MAPPING_DICTS:
        if mapping_dict["name"] == name:
            return mapping_dict["mapping"]
    raise KeyError(f"No mapping found for name: {name}")

def create_cieinr_phenopacket_mappings() -> Dict[str, Any]:
    """
    Create a comprehensive mapping configuration for Phenopacket creation from CIEINR data.

    Returns:
        Dict[str, Any]: Combined mapping configurations
    """
    # Load IUIS labels for diseases
    iuis_labels = load_iuis_labels()
    
    # Get BioPortal API token from environment variables
    bioportal_api_token = os.getenv("BIOPORTAL_API_TOKEN", "")
    if bioportal_api_token:
        logger.info("BioPortal API token found in environment")
    else:
        logger.warning("BioPortal API token not found in environment")
    
    # Get creator info
    created_by = os.getenv("CREATED_BY", "CIEINR Data Team")
    
    # Create the mappings
    return {
        "individual": {
            "instrument_name": "patient_demographics_initial_form",
            "mapping_block": INDIVIDUAL_BLOCK,
            "label_dicts": {},
            "mapping_dicts": {
                "map_sex": get_mapping_by_name("map_sex"),
            }
        },
        "vitalStatus": {
            "instrument_name": "__dummy__",  # Special marker for our patched function
            "mapping_block": VITAL_STATUS_BLOCK,
            "label_dicts": {},
            "mapping_dicts": {
                "map_vital_status": get_mapping_by_name("map_vital_status"),
            }
        },
        "diseases": {
            "instrument_name": "basic_form",
            "mapping_block": DISEASE_BLOCK,
            "label_dicts": {
                "IUIS2024MONDO": iuis_labels
            },
            "mapping_dicts": {
                "map_disease_verification_status": get_mapping_by_name("map_disease_verification_status"),
            }
        },
        "phenotypicFeatures": {
            "instrument_name": "infections_initial_form",
            "mapping_block": PHENOTYPIC_FEATURES_BLOCK,
            "label_dicts": {},
            "mapping_dicts": {
                "phenotypic_feature_status": get_mapping_by_name("map_infection_severity"),
                "temporal_pattern": get_mapping_by_name("map_infection_temporal_pattern")
            }
        },
        "metadata": {
            "resources": CIEINR_CODE_SYSTEMS_DICT,
            "created_by": created_by,
            "bioportal_api_token": bioportal_api_token
        }
    }
from typing import Dict, Any
from cieinr.datamodel.mappings.phenopackets import (
    DISEASE_BLOCK,
    INDIVIDUAL_BLOCK,
    INFECTIONS_FEATURES_BLOCK,
    CONDITIONS_FEATURES_BLOCK,
    BASIC_PROCEDURE_BLOCK,
    INACTIVATED_VACCINE_BLOCK,
    VACCINE_HISTORY_BLOCK,
    CIEINR_CODE_SYSTEMS,
    CBC_MEASUREMENT_BLOCK,
    LYMPHOCYTES_PHENOTYPE_BLOCK,
    LYMPHOCYTE_FUNCTION_BLOCK,
    INTERPRETATION_BLOCK,
    VARIATION_DESCRIPTOR_BLOCK,
    mapping_dicts,
    label_dicts,
)



def create_phenopacket_mappings() -> Dict[str, Any]:
    """
    Create a comprehensive mapping configuration for CIEINR Phenopacket creation.
    Uses the RareLink ontology routing adapter for infections and conditions
    to resolve coded values from multiple ontology-backed dropdown fields.
    """
    mapping_dict_lookup = {
        mapping["name"]: mapping["mapping"] for mapping in mapping_dicts
    }
    return {
        "individual": {
            "instrument_name": "patient_demographics_initial_form",
            "mapping_block": INDIVIDUAL_BLOCK,
            "mapping_dicts": {},
            "enum_classes": {},
        },
        "diseases": {
            "instrument_name": {"patient_demographics_initial_form"},
            "mapping_block": DISEASE_BLOCK,
            "enum_classes": {
                "iei_deficiency_basic": "cieinr.datamodel.linkml_schemas.patient_demographics_initial_form.IeiDeficiencyBasicEnum",
            },
        },
        "ontology_routing": {
            "enabled": True,
            "instruments": [
                "infections_initial_form",
            ],
            "scan_fields": {
                "infections_initial_form": [
                    "snomedct_61274003",
                    "snomedct_21483005",
                    "snomedct_81745001",
                    "snomedct_385383008",
                    "snomedct_127856007",
                    "snomedct_110522009",
                    "snomedct_20139000",
                    "snomedct_303699009",
                    "snomedct_21514008",
                    "snomedct_31099001",
                    "other_infection_hpo",
                    "other_infection_mondo",
                ],
            },
            "onset_fields": {
                "infections_initial_form": [
                    "infection_date",
                    "infection_date_2",
                    "infection_date_3",
                    "infection_date_4",
                    "infection_date_5",
                    "infection_date_6",
                ],
            },
        },
        "phenotypicFeatures": [
            {
                "instrument_name": "infections_initial_form",
                "mapping_block": INFECTIONS_FEATURES_BLOCK,
                "data_model": "infections",
                "mapping_dicts": {
                    "phenotypic_feature_status": mapping_dict_lookup.get(
                        "phenotypic_feature_status", {}
                    ),
                },
                "multi_onset": True,
                "enable_field_scanning": False,
                "enum_classes": {
                    "type_of_infection": "cieinr.datamodel.linkml_schemas.infections_initial_form.InfectionTypeEnum",
                    "infection_severity": "cieinr.datamodel.linkml_schemas.infections_initial_form.InfectionSeverityEnum",
                },
            },
            {
                "instrument_name": "patients_systemic_or_organ_specific_conditions",
                "mapping_block": CONDITIONS_FEATURES_BLOCK,
                "data_model": "conditions",
                "mapping_dicts": {
                    "phenotypic_feature_status": mapping_dict_lookup.get(
                        "phenotypic_feature_status", {}
                    ),
                },
                "multi_onset": False,
                "enable_field_scanning": False,
                "ontology_routing": {
                    "type_of_condition": {
                        "snomedct_95320005": "cieinr.datamodel.linkml_schemas.conditions.Snomedct95320005Enum",
                        "snomedct_118938008": "cieinr.datamodel.linkml_schemas.conditions.Snomedct118938008Enum",
                        "snomedct_50043002": "cieinr.datamodel.linkml_schemas.conditions.Snomedct50043002Enum",
                        "snomedct_49601007": "cieinr.datamodel.linkml_schemas.conditions.Snomedct49601007Enum",
                        "mondo_0005570": "cieinr.datamodel.linkml_schemas.conditions.Mondo0005570Enum",
                        "snomedct_928000": "cieinr.datamodel.linkml_schemas.conditions.Snomedct928000Enum",
                        "snomedct_119292006": "cieinr.datamodel.linkml_schemas.conditions.Snomedct119292006Enum",
                        "snomedct_362969004": "cieinr.datamodel.linkml_schemas.conditions.Snomedct362969004Enum",
                        "snomedct_42030000": "cieinr.datamodel.linkml_schemas.conditions.Snomedct42030000Enum",
                        "snomedct_55342001": "cieinr.datamodel.linkml_schemas.conditions.Snomedct55342001Enum",
                        "snomedct_85828009": "cieinr.datamodel.linkml_schemas.conditions.Snomedct85828009Enum",
                        "hp_0025142": "cieinr.datamodel.linkml_schemas.conditions.Hp0025142Enum",
                        "snomedct_5294002": "cieinr.datamodel.linkml_schemas.conditions.Snomedct5294002Enum",
                    },
                },
                "enum_classes": {
                    "type_of_condition": "cieinr.datamodel.linkml_schemas.conditions.TypeOfConditionEnum",
                    "hp_0012539_modifier": "cieinr.datamodel.linkml_schemas.conditions.Hp0012539ModifierEnum",
                    "hp_0012189_modifier": "cieinr.datamodel.linkml_schemas.conditions.Hp0012189ModifierEnum",
                    "hp_0005523_modifier": "cieinr.datamodel.linkml_schemas.conditions.Hp0005523ModifierEnum",
                },
            },
        ],
        "procedures": {
            "instrument_name": "patient_demographics_initial_form",
            "mapping_block": BASIC_PROCEDURE_BLOCK,
            "mapping_dicts": {},
            "enum_classes": {
                "igrt_basic": "cieinr.datamodel.linkml_schemas.patient_demographics_initial_form.IgrtBasicEnum",
                "hct_basic_form": "cieinr.datamodel.linkml_schemas.patient_demographics_initial_form.HctBasicFormEnum",
            },
        },
        "measurements": [
            {
                "instrument_name": "cbc",
                "mapping_block": CBC_MEASUREMENT_BLOCK,
                "multi_measurement": True,
                "enum_classes": {
                    "cbc_type": "cieinr.datamodel.linkml_schemas.cbc.CbcTypeEnum",
                },
            },
            {
                "instrument_name": "lymphocytes_phenotype",
                "mapping_block": LYMPHOCYTES_PHENOTYPE_BLOCK,
                "multi_measurement": True,
                "enum_classes": {
                    "lympheno_test": "cieinr.datamodel.linkml_schemas.lymphocytes_phenotype.LymphenoTestEnum",
                },
            },
            {
                "instrument_name": "lymphocyte_functionnk_cytotoxicity",
                "mapping_block": LYMPHOCYTE_FUNCTION_BLOCK,
                "multi_measurement": True,
                "enum_classes": {
                    "lymphfunc_test": "cieinr.datamodel.linkml_schemas.lymphocyte_function.LymphfuncTestEnum",
                },
            },
        ],
        "treatments": [
            {
                "instrument_name": "inactivated_vaccine_history_and_specific_immune_re",
                "mapping_block": INACTIVATED_VACCINE_BLOCK,
                "enum_classes": {
                    "inactiv_vax": "cieinr.datamodel.linkml_schemas.inactivated_vaccine.InactivVaxEnum",
                },
            },
            {
                "instrument_name": "vaccine_history_and_specific_immune_response",
                "mapping_block": VACCINE_HISTORY_BLOCK,
                "enum_classes": {
                    "vax_administered": "cieinr.datamodel.linkml_schemas.vaccine_history.VaxAdministeredEnum",
                },
            },
        ],
        "variationDescriptor": {
            "instrument_name": "genetic_information",
            "mapping_block": VARIATION_DESCRIPTOR_BLOCK,
            "label_dicts": {
                "Zygosity": label_dicts.get("Zygosity", {}),
                "DNAChangeType": label_dicts.get("DNAChangeType", {}),
            },
        },
        "interpretations": {
            "instrument_name": "genetic_information",
            "mapping_block": INTERPRETATION_BLOCK,
            "mapping_dicts": {
                "map_interpretation_status": mapping_dict_lookup.get(
                    "map_interpretation_status", {}
                ),
                "map_acmg_classification": mapping_dict_lookup.get(
                    "map_acmg_classification", {}
                ),
            },
            "enum_classes": {
                "interpretation_status": "cieinr.datamodel.linkml_schemas.genetic_information.InterpretationStatusEnum",
                "loinc_53037_8": "cieinr.datamodel.linkml_schemas.genetic_information.Loinc530378Enum",
            },
        },
        "metadata": {
            "code_systems": CIEINR_CODE_SYSTEMS,
        },
    }


def get_mapping_for_block(
    block_name: str,
    mapping_type: str,
    key: str,
    mappings: Dict[str, Any] = None,
) -> Dict[str, str]:
    """
    Retrieve a specific mapping or label dictionary from the comprehensive mappings.
    """
    if mappings is None:
        mappings = create_phenopacket_mappings()

    block_mappings = mappings.get(block_name, {})

    if isinstance(block_mappings, list):
        combined = {}
        for config in block_mappings:
            if mapping_type in config:
                combined.update(config[mapping_type].get(key, {}))
        return combined

    if mapping_type not in block_mappings:
        return {}

    return block_mappings[mapping_type].get(key, {})

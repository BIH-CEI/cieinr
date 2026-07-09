mapping_dicts = [
    {
        "name": "map_interpretation_status",
        "mapping": {
            "unknown_status": "UNKNOWN_STATUS",
            "rejected": "REJECTED",
            "candidate": "CANDIDATE",
            "contributory": "CONTRIBUTORY",
            "causative": "CAUSATIVE",
        },
    },
    {
        "name": "map_acmg_classification",
        "mapping": {
            "loinc_la6668-3": "PATHOGENIC",
            "loinc_la26332-9": "LIKELY_PATHOGENIC",
            "loinc_la26333-7": "UNCERTAIN_SIGNIFICANCE",
            "loinc_la26334-5": "LIKELY_BENIGN",
            "loinc_la6675-8": "BENIGN",
            "loinc_la4489-6": "NOT_PROVIDED",
        },
    },
    {
        "name": "phenotypic_feature_status",
        "mapping": {
            "snomedct_410605003": "false",
            "snomedct_723511001": "true",
        },
    },
]


def get_mapping_by_name(name, to_boolean=False):
    """
    Fetches a mapping by its name and optionally applies a boolean conversion.
    """
    for mapping_dict in mapping_dicts:
        if mapping_dict["name"] == name:
            mapping = mapping_dict["mapping"]
            if to_boolean:
                return {key: value.lower() == "true" for key, value in mapping.items()}
            return mapping
    raise KeyError(f"No mapping found for name: {name}")

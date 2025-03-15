import json
from datetime import datetime
import uuid

def map_hpo_term(code):
    """Maps coded terms to HPO terms"""
    # This would be more comprehensive in a real implementation
    # with a proper ontology mapping service
    hpo_mappings = {
        # Severity mappings
        "hp_0012826": {
            "id": "HP:0012826",
            "label": "Moderate"
        },
        # Temperature pattern mappings
        "hp_0011009": {
            "id": "HP:0011009", 
            "label": "Intermittent fever"
        },
        "hp_0011011": {
            "id": "HP:0011011",
            "label": "Recurrent fever"
        },
        # Infection type mappings
        "hp_0002090": {
            "id": "HP:0002090",
            "label": "Pneumonia"
        },
        # Add more mappings as needed
    }
    
    if code in hpo_mappings:
        return hpo_mappings[code]
    
    # Default return if not found
    return {
        "id": code,
        "label": f"Unknown term for {code}"
    }

def map_mondo_term(code):
    """Maps coded terms to MONDO terms"""
    mondo_mappings = {
        "mondo_0007843": {
            "id": "MONDO:0007843",
            "label": "primary immunodeficiency disease"
        },
        "mondo_0043653": {
            "id": "MONDO:0043653",
            "label": "viral infection"
        },
        # Add more mappings as needed
    }
    
    if code in mondo_mappings:
        return mondo_mappings[code]
    
    # Default return if not found
    return {
        "id": code,
        "label": f"Unknown term for {code}"
    }

def map_ncit_term(code):
    """Maps coded terms to NCIT terms"""
    ncit_mappings = {
        "ncit_c156502": {
            "id": "NCIT:C156502",
            "label": "Recurrent"
        },
        "ncit_c65134": {
            "id": "NCIT:C65134",
            "label": "Chronic"
        },
        "ncit_c62710": {
            "id": "NCIT:C62710",
            "label": "Immunoglobulin Therapy"
        },
        # Add more mappings as needed
    }
    
    if code in ncit_mappings:
        return ncit_mappings[code]
    
    # Default return if not found
    return {
        "id": code,
        "label": f"Unknown term for {code}"
    }

def map_ncbitaxon_term(code):
    """Maps coded terms to NCBITaxon terms"""
    taxon_mappings = {
        "ncbitaxon_2": {
            "id": "NCBITaxon:2",
            "label": "Bacteria"
        },
        "ncbitaxon_10239": {
            "id": "NCBITaxon:10239",
            "label": "Viruses"
        },
        "ncbitaxon_81852": {
            "id": "NCBITaxon:81852",
            "label": "Staphylococcus aureus"
        },
        # Add more mappings as needed
    }
    
    if code in taxon_mappings:
        return taxon_mappings[code]
    
    # Default return if not found
    return {
        "id": code,
        "label": f"Unknown taxon for {code}"
    }

def map_viral_agent(code):
    """Maps viral agent codes to proper terms"""
    viral_mappings = {
        "3": {
            "id": "NCBITaxon:11623",
            "label": "Human respiratory syncytial virus"
        },
        "5": {
            "id": "NCBITaxon:11234",
            "label": "Influenza virus"
        },
        # Add more mappings as needed
    }
    
    if code in viral_mappings:
        return viral_mappings[code]
    
    # Default return if not found
    return {
        "id": f"VIRAL:{code}",
        "label": f"Unknown viral agent {code}"
    }

def map_snomed_term(code):
    """Maps SNOMED CT terms"""
    snomed_mappings = {
        "snomedct_127856007": {
            "id": "SNOMEDCT:127856007",
            "label": "Viral infection"
        },
        "snomedct_20139000": {
            "id": "SNOMEDCT:20139000",
            "label": "Pneumonia"
        },
        # Add more mappings as needed
    }
    
    if code in snomed_mappings:
        return snomed_mappings[code]
    
    # Default return if not found
    return {
        "id": code,
        "label": f"Unknown term for {code}"
    }

def generate_metadata():
    """Generates metadata for the phenopacket"""
    now = datetime.now().isoformat()
    
    return {
        "created": now,
        "created_by": "Adam G.",
        "resources": [
            {
                "id": "hp",
                "name": "Human Phenotype Ontology",
                "url": "http://purl.obolibrary.org/obo/hp.owl",
                "version": "2021-08-02",
                "namespace_prefix": "HP"
            },
            {
                "id": "mondo",
                "name": "Mondo Disease Ontology",
                "url": "http://purl.obolibrary.org/obo/mondo.owl",
                "version": "2021-09-30",
                "namespace_prefix": "MONDO"
            },
            {
                "id": "ncbitaxon",
                "name": "NCBI Taxonomy",
                "url": "http://purl.obolibrary.org/obo/ncbitaxon.owl",
                "version": "2021-06-10",
                "namespace_prefix": "NCBITaxon"
            },
            {
                "id": "snomedct",
                "name": "SNOMED Clinical Terms",
                "url": "http://snomed.info/sct",
                "version": "2021-09",
                "namespace_prefix": "SNOMEDCT"
            }
        ],
        "phenopacket_schema_version": "2.0.0"
    }

def extract_subject(data):
    """Extract subject information from the main record"""
    # Find the main record
    main_record = next(r for r in data if not r.get("redcap_repeat_instrument"))
    
    # Construct a unique identifier based on registry ID
    subject_id = main_record.get("national_iei_registry_id", f"PATIENT:{main_record.get('record_id')}")
    
    return {
        "id": subject_id,
        "time_at_last_encounter": {
            "timestamp": main_record.get("visit_date_demographics", datetime.now().strftime("%Y-%m-%d"))
        }
    }

def extract_phenotypic_features(data):
    """Extract phenotypic features from infection records"""
    features = []
    
    # Process the infection records
    infection_records = [r for r in data if r.get("redcap_repeat_instrument") == "infections_initial_form"]
    
    for record in infection_records:
        # Extract infection type
        infection_type = None
        if record.get("type_of_infection"):
            # If explicitly typed
            if record["type_of_infection"].startswith("snomedct_"):
                # Map SNOMED code
                term = map_snomed_term(record["type_of_infection"])
                infection_type = term
                
                # Check if there's a more specific mapping
                specific_field = record.get(record["type_of_infection"])
                if specific_field:
                    if specific_field.startswith("hp_"):
                        infection_type = map_hpo_term(specific_field)
                    elif specific_field.startswith("mondo_"):
                        infection_type = map_mondo_term(specific_field)
        
        if infection_type:
            # Create a feature for the infection type
            feature = {
                "type": infection_type,
                "onset": {
                    "timestamp": record.get("infection_date")
                }
            }
            
            # Add severity if available
            if record.get("infection_severity"):
                severity_term = map_hpo_term(record["infection_severity"])
                feature["severity"] = severity_term
            
            # Add to features list
            features.append(feature)
        
        # Extract fever pattern if available
        if record.get("infection_temp_pattern"):
            fever_pattern = map_hpo_term(record["infection_temp_pattern"])
            features.append({
                "type": fever_pattern,
                "onset": {
                    "timestamp": record.get("infection_date")
                }
            })
        
        # Add temporal pattern (recurrent, chronic, etc.)
        if record.get("infection_times_obseverd"):
            temporal_pattern = map_ncit_term(record["infection_times_obseverd"])
            features.append({
                "type": temporal_pattern,
                "onset": {
                    "timestamp": record.get("infection_date")
                }
            })
    
    return features

def extract_diseases(data):
    """Extract disease information from the main record"""
    diseases = []
    
    # Find the main record
    main_record = next(r for r in data if not r.get("redcap_repeat_instrument"))
    
    # Extract primary diagnosis if available
    if main_record.get("iei_deficiency_basic"):
        disease_term = map_mondo_term(main_record["iei_deficiency_basic"])
        disease = {
            "term": disease_term,
            "onset": {
                "timestamp": main_record.get("snomedct_184099003", "")  # Diagnostic date
            }
        }
        diseases.append(disease)
    
    return diseases

def extract_interpretations(data):
    """Extract genetic and diagnostic interpretations"""
    interpretations = []
    
    # Find the main record
    main_record = next(r for r in data if not r.get("redcap_repeat_instrument"))
    
    # Check if there's a genetic diagnosis
    if main_record.get("genetic_diagnosis") == "1":
        # Add a genomic interpretation
        interpretations.append({
            "id": f"interpretation:{uuid.uuid4()}",
            "progress_status": "COMPLETED",
            "diagnosis": {
                "disease": map_mondo_term(main_record.get("iei_deficiency_basic"))
            }
        })
    
    return interpretations

def extract_medical_actions(data):
    """Extract treatment/medication information"""
    actions = []
    
    # Find the main record
    main_record = next(r for r in data if not r.get("redcap_repeat_instrument"))
    
    # Check for IGRT (Immunoglobulin Replacement Therapy)
    if main_record.get("igrt_basic") == "ncit_c62710":
        actions.append({
            "procedure": map_ncit_term("ncit_c62710"),
            "treatment_target": map_mondo_term(main_record.get("iei_deficiency_basic"))
        })
    
    return actions

def transform_to_phenopacket(data):
    """Transform REDCap data to Phenopacket format"""
    phenopacket = {
        "id": f"phenopacket:{uuid.uuid4()}",
        "subject": extract_subject(data),
        "phenotypic_features": extract_phenotypic_features(data),
        "diseases": extract_diseases(data),
        "interpretations": extract_interpretations(data),
        "medical_actions": extract_medical_actions(data),
        "metadata": generate_metadata()
    }
    
    return phenopacket

# This function would be called with the patient data
def process_patient_data(json_data):
    data = json.loads(json_data) if isinstance(json_data, str) else json_data
    phenopacket = transform_to_phenopacket(data)
    return json.dumps(phenopacket, indent=2)

# Example usage:
# with open('RareLink_Berlin-records.json', 'r') as f:
#     data = json.load(f)
# phenopacket_json = process_patient_data(data)
# print(phenopacket_json)
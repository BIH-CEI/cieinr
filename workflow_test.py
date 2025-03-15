#!/usr/bin/env python3
"""
End-to-end workflow test for CIEINR.

This script demonstrates the entire workflow from:
1. REDCap API fetch to local records
2. REDCap records to LinkML format
3. LinkML format to Phenopackets
"""
import json
import os
import requests
import sys
import uuid
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List
from collections import defaultdict

# Import CIEINR functions directly to bypass CLI
from cieinr.config import Config
try:
    from cieinr.v1_0_0.redcap_to_linkml.registry import MAPPING_FUNCTIONS
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
    try:
        from cieinr.v1_0_0.redcap_to_linkml.registry import MAPPING_FUNCTIONS
    except ImportError:
        print("Error importing MAPPING_FUNCTIONS. Make sure the package is installed or modify sys.path.")
        sys.exit(1)

def fetch_redcap_records(api_url: str, token: str, project_id: str = None, use_test_data: bool = False) -> List[Dict[str, Any]]:
    """
    Fetch records from REDCap using the API or use test data.
    
    Args:
        api_url: The REDCap API URL
        token: The REDCap API token
        project_id: Optional project ID
        use_test_data: Whether to use test data instead of API
        
    Returns:
        List of records
    """
    if use_test_data:
        # Use the test patient data
        test_file = Path(__file__).parent / "res" / "test_patient.json"
        
        if not test_file.exists():
            raise FileNotFoundError(f"Test patient file not found at {test_file}")
        
        with open(test_file, "r") as infile:
            records = json.load(infile)
        
        print("Using test data instead of REDCap API.")
        return records
    
    # Prepare REDCap API request
    print(f"Fetching records from REDCap API: {api_url}")
    data = {
        'token': token,
        'content': 'record',
        'format': 'json',
        'type': 'flat',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'exportSurveyFields': 'false',
        'exportDataAccessGroups': 'false',
        'returnFormat': 'json'
    }
    
    if project_id:
        data['projectid'] = project_id
    
    # Make API request
    response = requests.post(api_url, data=data)
    
    # Check for errors
    if response.status_code != 200:
        raise ValueError(f"REDCap API request failed with status code {response.status_code}: {response.text}")
    
    # Parse response
    records = response.json()
    
    if not records:
        print("Warning: No records returned from REDCap API")
    
    print(f"Successfully fetched {len(records)} records from REDCap")
    return records

def redcap_to_linkml(records, output_file):
    """
    Transform REDCap records to LinkML format.
    
    Args:
        records: List of REDCap records (either from file or API)
        output_file: Path to save the transformed data
    """
    print(f"Transforming REDCap data to LinkML format...")
    
    # Process using the mapping functions
    transformed_data = []

    # Group data by record_id
    record_groups = defaultdict(list)
    for record in records:
        record_groups[record["record_id"]].append(record)

    # Process records
    for record_id, entries in record_groups.items():
        # Initialize the record structure with non-repeating sections first
        record = {
            "record_id": record_id,
        }

        # Add non-repeating data
        for entry in entries:
            if entry.get("redcap_repeat_instrument", "") == "":
                for schema_name, config in MAPPING_FUNCTIONS.items():
                    if not config["is_repeating"] and schema_name not in record:
                        try:
                            record[schema_name] = config["mapper"](entry)
                        except Exception as e:
                            print(f"Error mapping {schema_name}: {e}")
                            record[schema_name] = {}

        # Add repeating elements
        record["repeated_elements"] = []
        for entry in entries:
            if entry.get("redcap_repeat_instrument", "") != "":
                repeated_instrument = entry["redcap_repeat_instrument"]
                repeated_element = {
                    "redcap_repeat_instrument": repeated_instrument,
                    "redcap_repeat_instance": int(entry["redcap_repeat_instance"]),
                }

                # Find schema name and apply the mapper
                for schema_name, config in MAPPING_FUNCTIONS.items():
                    if config["is_repeating"] and repeated_instrument == schema_name:
                        try:
                            repeated_element[schema_name] = config["mapper"](entry)
                        except Exception as e:
                            print(f"Error mapping {schema_name}: {e}")
                            repeated_element[schema_name] = {}

                record["repeated_elements"].append(repeated_element)

        transformed_data.append(record)

    # Save the transformed data
    with open(output_file, "w") as outfile:
        json.dump(transformed_data, outfile, indent=2)

    print(f"Transformed data has been saved to {output_file}")
    return transformed_data

def map_hpo_term(code: str) -> dict:
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

def map_mondo_term(code: str) -> dict:
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

def map_ncit_term(code: str) -> dict:
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

def generate_metadata() -> dict:
    """Generates metadata for the phenopacket"""
    now = datetime.now().isoformat()
    config = Config()
    created_by = config.get("CREATED_BY") or "Unknown"
    
    return {
        "created": now,
        "created_by": created_by,
        "resources": [
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
                "id": "ncbitaxon",
                "name": "NCBI Taxonomy",
                "url": "http://purl.obolibrary.org/obo/ncbitaxon.owl",
                "version": "2023-04-01",
                "namespace_prefix": "NCBITaxon"
            },
            {
                "id": "snomedct",
                "name": "SNOMED Clinical Terms",
                "url": "http://snomed.info/sct",
                "version": "2023-03",
                "namespace_prefix": "SNOMEDCT"
            }
        ],
        "phenopacket_schema_version": "2.0.0"
    }

def extract_subject(record: dict) -> dict:
    """Extract subject information from the record"""
    # Construct a unique identifier based on registry ID
    subject_id = record.get("record_id", f"PATIENT:{uuid.uuid4()}")
    
    # Get date of birth from demographics
    demographics = record.get("patient_demographics_initial_form", {})
    birth_date = demographics.get("snomedct_184099003", "")
    
    return {
        "id": subject_id,
        "date_of_birth": birth_date,
        "time_at_last_encounter": {
            "timestamp": datetime.now().strftime("%Y-%m-%d")
        }
    }

def extract_phenotypic_features(record: dict) -> List[dict]:
    """Extract phenotypic features from infection records"""
    features = []
    
    # Process the infection records
    repeated_elements = record.get("repeated_elements", [])
    infection_records = [r for r in repeated_elements if r.get("redcap_repeat_instrument") == "infections_initial_form"]
    
    for record_element in infection_records:
        # Get the infection data
        infection = record_element.get("infections_initial_form", {})
        
        # Extract infection type
        infection_type = None
        if infection.get("type_of_infection"):
            # If explicitly typed
            infection_type_code = infection["type_of_infection"]
            
            # Check for specific infection code
            specific_field = infection.get(infection_type_code, "")
            
            if specific_field:
                if specific_field.startswith("hp_"):
                    infection_type = map_hpo_term(specific_field)
                elif specific_field.startswith("mondo_"):
                    infection_type = map_mondo_term(specific_field)
            else:
                # Use the general infection type
                infection_type = {
                    "id": infection_type_code,
                    "label": "Infection" 
                }
        
        if infection_type:
            # Create a feature for the infection type
            feature = {
                "type": infection_type,
            }
            
            # Add severity if available
            if infection.get("infection_severity"):
                severity_term = map_hpo_term(infection["infection_severity"])
                feature["severity"] = severity_term
            
            # Add to features list
            features.append(feature)
        
        # Extract fever pattern if available
        if infection.get("infection_temp_pattern"):
            fever_pattern = map_hpo_term(infection["infection_temp_pattern"])
            features.append({
                "type": fever_pattern
            })
        
        # Add temporal pattern (recurrent, chronic, etc.)
        if infection.get("infection_times_obseverd"):
            temporal_pattern = map_ncit_term(infection["infection_times_obseverd"])
            features.append({
                "type": temporal_pattern
            })
    
    return features

def extract_diseases(record: dict) -> List[dict]:
    """Extract disease information from the record"""
    diseases = []
    
    # Get the basic form data
    basic_form = record.get("basic_form", {})
    
    # Extract primary diagnosis if available
    if basic_form.get("iei_deficiency_basic"):
        disease_term = map_mondo_term(basic_form["iei_deficiency_basic"])
        
        # Get diagnosis date from demographics
        demographics = record.get("patient_demographics_initial_form", {})
        diagnosis_date = demographics.get("snomedct_432213005", "")
        onset_date = demographics.get("snomedct_298059007", "")
        
        disease = {
            "term": disease_term,
            "onset": {
                "timestamp": onset_date if onset_date else ""
            },
            "clinical_status": {
                "id": "active",
                "label": "Active" 
            },
            "diagnosis": {
                "timestamp": diagnosis_date if diagnosis_date else ""
            }
        }
        
        diseases.append(disease)
    
    return diseases

def transform_to_phenopacket(record: dict) -> dict:
    """Transform LinkML record to Phenopacket format"""
    phenopacket = {
        "id": f"phenopacket:{uuid.uuid4()}",
        "subject": extract_subject(record),
        "phenotypic_features": extract_phenotypic_features(record),
        "diseases": extract_diseases(record),
        "metadata": generate_metadata()
    }
    
    return phenopacket

def phenopackets_export(linkml_data, output_dir, output_file=None):
    """
    Transform LinkML data to Phenopackets.
    """
    print(f"Converting LinkML data to Phenopackets...")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    phenopackets = []
    
    # Transform each record to a phenopacket
    for record in linkml_data:
        try:
            phenopacket = transform_to_phenopacket(record)
            phenopackets.append(phenopacket)
            
            # Save individual phenopacket
            record_id = record.get("record_id", "unknown")
            record_output_path = os.path.join(output_dir, f"{record_id}.json")
            
            with open(record_output_path, "w") as outfile:
                json.dump(phenopacket, outfile, indent=2)
                
            print(f"Created phenopacket for record {record_id}")
            
            # Also save to res folder for convenience
            res_dir = Path(__file__).parent / "res" / "phenopackets"
            os.makedirs(res_dir, exist_ok=True)
            res_output_path = res_dir / f"{record_id}_phenopacket.json"
            with open(res_output_path, "w") as outfile:
                json.dump(phenopacket, outfile, indent=2)
            print(f"Also saved to {res_output_path}")
            
        except Exception as e:
            print(f"Error creating phenopacket for record {record.get('record_id', 'unknown')}: {e}")
            import traceback
            traceback.print_exc()
    
    # Save all phenopackets to a single file if requested
    if output_file:
        all_output_path = os.path.join(output_dir, output_file)
        with open(all_output_path, "w") as outfile:
            json.dump(phenopackets, outfile, indent=2)
        print(f"Saved all phenopackets to {all_output_path}")
    
    print(f"Exported {len(phenopackets)} phenopackets to {output_dir}")
    return phenopackets

def main():
    """
    Run the complete workflow.
    """
    # Parse arguments
    import argparse
    parser = argparse.ArgumentParser(description="CIEINR workflow test")
    parser.add_argument("--test", action="store_true", help="Use test data instead of REDCap API")
    parser.add_argument("--records-file", help="Use existing records file instead of fetching from REDCap")
    parser.add_argument("--output-dir", help="Output directory (defaults to ./output/timestamp)")
    args = parser.parse_args()
    
    # Setup file paths
    base_dir = Path(__file__).parent
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output_dir) if args.output_dir else base_dir / "output" / timestamp
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        if args.records_file:
            # Use existing records file
            records_file = Path(args.records_file)
            if not records_file.exists():
                raise FileNotFoundError(f"Records file not found: {records_file}")
            
            print(f"Using existing records file: {records_file}")
            with open(records_file, "r") as f:
                records = json.load(f)
        else:
            # Fetch from REDCap API or use test data
            config = Config()
            try:
                config.validate()
            except ValueError as e:
                print(f"Error validating configuration: {e}")
                print("Please make sure your .env file contains REDCAP_URL and REDCAP_API_TOKEN")
                return 1
            
            api_url = config.get("REDCAP_URL")
            token = config.get("REDCAP_API_TOKEN")
            project_id = config.get("REDCAP_PROJECT_ID")
            
            records_file = output_dir / "records.json"
            records = fetch_redcap_records(api_url, token, project_id, use_test_data=args.test)
            
            # Save the records for reference
            with open(records_file, "w") as outfile:
                json.dump(records, outfile, indent=2)
            print(f"Saved raw records to {records_file}")
        
        # Step 1: Convert REDCap records to LinkML format
        linkml_output = output_dir / "patient_linkml.json"
        linkml_data = redcap_to_linkml(records, linkml_output)
        
        # Step 2: Convert LinkML format to Phenopackets
        phenopackets_dir = output_dir / "phenopackets"
        phenopackets_output = "all_phenopackets.json"
        phenopackets = phenopackets_export(linkml_data, phenopackets_dir, phenopackets_output)
        
        # Also save to res directory for easy access
        res_linkml_path = base_dir / "res" / "patient_linkml.json"
        with open(res_linkml_path, "w") as outfile:
            json.dump(linkml_data, outfile, indent=2)
        
        print("\nWorkflow completed successfully!")
        print(f"Records: {records_file}")
        print(f"LinkML data: {linkml_output} (also at {res_linkml_path})")
        print(f"Phenopackets: {phenopackets_dir}")
        print(f"All phenopackets: {phenopackets_dir / phenopackets_output}")
        print(f"Individual phenopackets are also saved in {base_dir}/res/phenopackets/")
        
    except Exception as e:
        print(f"Error in workflow: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
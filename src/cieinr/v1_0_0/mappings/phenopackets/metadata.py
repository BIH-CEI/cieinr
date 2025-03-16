"""Module for generating Phenopacket metadata."""

from datetime import datetime
from typing import Dict, Any, Optional

def generate_metadata(created_by: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate metadata for a Phenopacket.
    
    Args:
        created_by: Optional name of the creator
        
    Returns:
        Dictionary containing metadata information
    """
    now = datetime.now().isoformat()
    creator = created_by or "CIEINR"
    
    return {
        "created": now,
        "created_by": creator,
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
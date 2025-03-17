"""
CIEINR Phenopackets Example Usage

This script demonstrates how to use the CIEINR phenopackets pipeline to generate
phenopackets from CIEINR data.
"""

import os
import json
import logging
from pathlib import Path

# Import the CIEINR phenopackets pipeline without applying patches
# The new approach doesn't require patching RareLink functions
from cieinr.utils.pipeline.cieinr_phenopackets import (
    run_cieinr_phenopackets_pipeline,
    load_cieinr_data
)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Run the CIEINR phenopackets example."""
    # Define paths
    input_file = "res/patient_linkml.json"  # Use the exact sample data provided
    output_dir = "output/phenopackets"  # Standard output directory in root
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    logger.info(f"Processing CIEINR data from {input_file}")
    logger.info(f"Writing phenopackets to {output_dir}")
    
    # Run the pipeline
    phenopackets, failed_records = run_cieinr_phenopackets_pipeline(
        input_file=input_file,
        output_dir=output_dir,
        created_by="CIEINR Example Script",
        validate=True
    )
    
    # Log results
    logger.info(f"Generated {len(phenopackets)} phenopackets")
    if failed_records:
        logger.warning(f"Failed to generate phenopackets for {len(failed_records)} records")
        for i, failed in enumerate(failed_records):
            logger.warning(f"Failed record {i+1}: {failed['error']}")
    
    # Write summary to output directory
    summary = {
        "total_records": len(phenopackets) + len(failed_records),
        "successful": len(phenopackets),
        "failed": len(failed_records),
        "failed_records": [
            {
                "record_id": record.get("record", {}).get("record_id", "unknown"),
                "error": record.get("error", "Unknown error")
            }
            for record in failed_records
        ]
    }
    
    with open(os.path.join(output_dir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2)
    
    logger.info(f"Summary written to {os.path.join(output_dir, 'summary.json')}")
    
    return phenopackets, failed_records

if __name__ == "__main__":
    # Always use the real patient_linkml.json data
    phenopackets, failed_records = main()
    
    # Print final message
    print(f"\nProcessed {len(phenopackets) + len(failed_records)} records")
    print(f"Successfully created {len(phenopackets)} phenopackets")
    print(f"Failed to create {len(failed_records)} phenopackets")
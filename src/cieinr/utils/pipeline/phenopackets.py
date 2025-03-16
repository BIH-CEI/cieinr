import json
import logging
import os
from pathlib import Path
from datetime import datetime

from rarelink.utils.processor import DataProcessor
from rarelink.phenopackets import (
    create_phenopacket,
    write_phenopackets,
    phenopacket_pipeline,
    validate_phenopackets
)

# Import CIEINR specific mappings
from cieinr.v1_0_0.mappings.phenopackets.mapping_blocks import (
    INDIVIDUAL_BLOCK,
    DISEASE_BLOCK,
    PHENOTYPIC_FEATURES_BLOCK,
    CIEINR_CODE_SYSTEMS
)
from cieinr.v1_0_0.mappings.phenopackets.metadata import generate_metadata

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def process_cieinr_phenopackets(
    input_data_path: Path, 
    output_dir: Path = None, 
    created_by: str = "CIEINR Data Team"
):
    """
    Process LinkML data into Phenopackets using RareLink's pipeline.

    Args:
        input_data_path (Path): Path to the LinkML JSON file
        output_dir (Path, optional): Directory to save generated Phenopacket JSON files
        created_by (str, optional): Creator name for metadata
    """
    # If no output directory specified, create a timestamped directory
    if output_dir is None:
        base_dir = Path.cwd()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = base_dir / "output" / timestamp / "phenopackets"
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Read the LinkML input data
        with open(input_data_path, 'r') as f:
            linkml_data = json.load(f)
        
        # Validate input data
        if not isinstance(linkml_data, list):
            raise ValueError("Input data must be a list of patient records")
        
        # Optional: Add logging for number of records
        logger.info(f"Processing {len(linkml_data)} patient records")

        # Run the phenopacket pipeline
        phenopackets = []
        for record in linkml_data:
            try:
                # Create individual Phenopacket
                phenopacket = create_phenopacket(
                    data=record, 
                    created_by=created_by
                )
                phenopackets.append(phenopacket)
                logger.info(f"Created Phenopacket for record ID: {phenopacket.id}")
            except Exception as e:
                logger.error(f"Failed to create Phenopacket for record: {e}")
                # Optionally continue processing other records
        
        # Write Phenopackets to files
        write_phenopackets(phenopackets, str(output_dir))
        logger.info(f"Wrote {len(phenopackets)} Phenopackets to {output_dir}")

        # Validate the generated Phenopackets
        try:
            validation_results = validate_phenopackets(output_dir)
            
            # Log validation results
            if isinstance(validation_results, list):
                successful_validations = sum(1 for success, _ in validation_results if success)
                logger.info(f"Validation complete: {successful_validations}/{len(validation_results)} Phenopackets validated successfully")
            else:
                success, details = validation_results
                if success:
                    logger.info("Phenopacket validation successful")
                else:
                    logger.error("Phenopacket validation failed")
            
        except Exception as val_error:
            logger.error(f"Validation process encountered an error: {val_error}")

        return phenopackets

    except Exception as e:
        logger.error(f"Error processing CIEINR Phenopackets: {e}")
        raise



def main():
    """
    Example usage of the Phenopacket processing function.
    """
    # Example paths - adjust as needed
    base_dir = Path.cwd()
    input_data_path = base_dir / "res" / "patient_linkml.json"
    output_dir = base_dir / "output" / datetime.now().strftime("%Y%m%d_%H%M%S") / "phenopackets"
    
    # Process Phenopackets
    phenopackets = process_cieinr_phenopackets(
        input_data_path=input_data_path, 
        output_dir=output_dir,
        created_by="CIEINR Data Curator"
    )

if __name__ == "__main__":
    main()
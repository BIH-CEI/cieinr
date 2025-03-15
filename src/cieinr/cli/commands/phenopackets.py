import typer
import json
import os
import sys
from pathlib import Path
from typing import Optional, List
from datetime import datetime

# For proper RareLink integration, add the submodules path to system path
sys.path.append(str(Path(__file__).parent.parent.parent.parent.parent / "submodules"))

# Import RareLink utilities when available as submodule
try:
    from rarelink.phenopackets import phenopacket_pipeline as rarelink_phenopacket_pipeline
except ImportError:
    # Fallback to local implementation
    pass

from cieinr.cli.utils.env import load_env, validate_required_keys, get_env_variable
from cieinr.cli.utils.output import (
    format_header, 
    format_section, 
    success_message, 
    error_message, 
    warning_message, 
    info_message,
    format_command
)

# Import CIEINR phenopacket generation
from cieinr.phenopackets.create import create_phenopacket
from cieinr.phenopackets.write import write_phenopackets

app = typer.Typer(help="Phenopacket commands for CIEINR")

@app.command("create")
def create_phenopackets_command(
    input_file: Optional[Path] = typer.Option(
        None,
        "--input", "-i",
        help="Path to the LinkML records JSON file",
    ),
    output_dir: Path = typer.Option(
        Path.home() / "Downloads" / "cieinr_phenopackets",
        help="Directory to save generated phenopackets",
    ),
    created_by: Optional[str] = typer.Option(
        None,
        "--created-by",
        help="Name of the creator (overrides value from .env file)",
    ),
):
    """
    Create phenopackets from LinkML records.
    
    This command will:
    1. Read the LinkML records from the specified input file (or auto-detect)
    2. Generate phenopackets for each record
    3. Save the phenopackets to the output directory
    """
    format_header("Create Phenopackets from LinkML Records")
    
    # Validate required environment variables if created_by is not provided
    if created_by is None:
        if not validate_required_keys(["CREATED_BY"]):
            error_message(f"Please run {format_command('cieinr setup keys')} to configure your API keys or provide --created-by.")
            raise typer.Exit(1)
        created_by = get_env_variable("CREATED_BY", "CIEINR Engine").strip('"\'')
    
    # Load environment variables
    env_vars = load_env()
    redcap_project_name = env_vars.get("REDCAP_PROJECT_NAME", "").strip('"\'')
    sanitized_project_name = redcap_project_name.replace(" ", "_")
    
    # Auto-detect input file if not specified
    if input_file is None:
        input_file = Path.home() / "Downloads" / "cieinr_records" / f"{sanitized_project_name}-linkml-records.json"
    
    # Check if input file exists
    if not input_file.exists():
        error_message(f"Input file {input_file} does not exist. Please run {format_command('cieinr transform linkml')} first.")
        raise typer.Exit(1)
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    info_message(f"Creating phenopackets from {input_file}...")
    
    try:
        # Read LinkML records from file
        with open(input_file, 'r') as f:
            linkml_records = json.load(f)
        
        # Determine whether to use RareLink implementation or our own
        try:
            # Use RareLink implementation if available
            info_message("Using RareLink phenopacket pipeline...")
            rarelink_phenopacket_pipeline(
                input_data=linkml_records,
                output_dir=str(output_dir),
                created_by=created_by
            )
        except (ImportError, NameError):
            # Use our own implementation
            info_message("Using CIEINR phenopacket pipeline...")
            
            # Generate phenopackets for each record
            phenopackets = []
            with typer.progressbar(linkml_records, label="Generating phenopackets") as progress:
                for record in progress:
                    try:
                        phenopacket = create_phenopacket(record, created_by)
                        phenopackets.append(phenopacket)
                    except Exception as e:
                        error_message(f"Failed to create phenopacket for record ID {record.get('record_id', 'unknown')}: {e}")
            
            # Save phenopackets to files
            write_phenopackets(phenopackets, output_dir)
        
        success_message(f"Created phenopackets and saved them to {output_dir}")
        
    except Exception as e:
        error_message(f"Failed to create phenopackets: {e}")
        raise typer.Exit(1)

@app.command("validate")
def validate_phenopackets_command(
    input_path: Path = typer.Argument(
        ...,
        help="Path to a phenopacket file or directory containing phenopackets",
    ),
):
    """
    Validate phenopackets against the GA4GH Phenopacket schema.
    
    This command will:
    1. Validate the specified phenopacket file or all phenopackets in the directory
    2. Report validation results
    """
    format_header("Validate Phenopackets")
    
    # Check if input path exists
    if not input_path.exists():
        error_message(f"Input path {input_path} does not exist.")
        raise typer.Exit(1)
    
    try:
        # Import validation function
        from cieinr.phenopackets.validate import validate_phenopackets
        
        # Validate phenopackets
        info_message(f"Validating phenopackets at {input_path}...")
        results = validate_phenopackets(input_path)
        
        # Report results
        if isinstance(results, list):
            # Multiple results (directory)
            valid_count = sum(1 for r in results if r[0])
            invalid_count = len(results) - valid_count
            
            format_section("Validation Summary")
            typer.echo(f"Total phenopackets: {len(results)}")
            typer.echo(f"Valid phenopackets: {valid_count}")
            typer.echo(f"Invalid phenopackets: {invalid_count}")
            
            if invalid_count > 0:
                format_section("Invalid Phenopackets")
                for i, (valid, details) in enumerate(results):
                    if not valid:
                        error_message(f"Phenopacket {i+1}: {details}")
        else:
            # Single result (file)
            valid, details = results
            
            if valid:
                success_message(f"Phenopacket {input_path} is valid.")
            else:
                error_message(f"Phenopacket {input_path} is invalid: {details}")
        
    except Exception as e:
        error_message(f"Failed to validate phenopackets: {e}")
        raise typer.Exit(1)
"""
Main CLI application module for CIEINR.
"""
import typer
import sys
import os
from typing import Optional
from pathlib import Path
from cieinr import __version__

# Add the submodules to sys.path to allow importing
submodules_path = Path(__file__).parent.parent.parent.parent / "submodules"
if submodules_path.exists():
    sys.path.append(str(submodules_path))
    
try:
    # Try importing from the RareLink submodule
    from rarelink.cli.utils import (
        format_header,
        format_section,
        success_message,
        error_message,
        warning_message
    )
except ImportError:
    # If that fails, try the other potential location
    sys.path.append(str(Path(__file__).parent.parent.parent.parent / "submodules" / "src"))
    try:
        from rarelink.cli.utils import (
            format_header,
            format_section,
            success_message,
            error_message,
            warning_message
        )
    except ImportError:
        # If both fail, print a warning but continue
        print("Warning: Could not import RareLink CLI utilities")

from cieinr.cli.commands.setup import app as setup_app
from cieinr.cli.commands.transform import app as transform_app
from cieinr.cli.commands.phenopackets import app as phenopackets_app
from cieinr.cli.commands.download import app as download_app

# Create the main app
app = typer.Typer(
    help="CIEINR: Canadian Inborn Errors of Immunity National Registry",
    no_args_is_help=True
)

# Add subcommands
app.add_typer(setup_app, name="setup", help="Setup commands for environment and configuration")
app.add_typer(transform_app, name="transform", help="Data transformation commands")
app.add_typer(phenopackets_app, name="phenopackets", help="Generate phenopackets from patient data")
app.add_typer(download_app, name="download", help="Download data from REDCap")

@app.callback()
def callback():
    """
    CIEINR: Canadian Inborn Errors of Immunity National Registry

    Command-line interface for managing and processing CIEINR data.
    """
    pass

@app.command()
def version():
    """Display the current version of the CIEINR package."""
    typer.echo(f"CIEINR version: {__version__}")

def main():
    """Main entry point for the CLI."""
    app()

if __name__ == "__main__":
    main()
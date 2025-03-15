"""
Main CLI application module for CIEINR.
"""
import typer
from typing import Optional
from cieinr import __version__

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
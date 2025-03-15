"""
Main CLI application module for CIEINR.
"""
import typer
import sys
from pathlib import Path
from typing import Optional
from cieinr._version import __version__
from cieinr.utils.version_utils import format_version_message

# Add the submodules to sys.path to allow importing
submodules_path = Path(__file__).parent.parent.parent.parent / "submodules" 
if submodules_path.exists():
    sys.path.append(str(submodules_path))
    rarelink_src_path = submodules_path / "rarelink" / "src"
    if rarelink_src_path.exists():
        sys.path.append(str(rarelink_src_path))

# from cieinr.cli.commands.setup import app as setup_app
# from cieinr.cli.commands.transform import app as transform_app
# from cieinr.cli.commands.phenopackets import app as phenopackets_app
# from cieinr.cli.commands.download import app as download_app
# Create the main app
app = typer.Typer(
    help="CIEINR: Canadian Inborn Errors of Immunity National Registry",
    no_args_is_help=True
)

# Add subcommands
# app.add_typer(setup_app, name="setup", help="Setup commands for environment and configuration")
# app.add_typer(transform_app, name="transform", help="Data transformation commands")
# app.add_typer(phenopackets_app, name="phenopackets", help="Generate phenopackets from patient data")
# app.add_typer(download_app, name="download", help="Download data from REDCap")

@app.callback()
def callback():
    """
    CIEINR: Canadian Inborn Errors of Immunity National Registry

    Command-line interface for managing and processing CIEINR data.
    """
    pass

@app.command()
def version(
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed version information")
):
    """Display the current version of the CIEINR package."""
    if verbose:
        from cieinr.utils.version_utils import get_full_version_info
        info = get_full_version_info()
        typer.echo(f"CIEINR version: {info['version']}")
        typer.echo(f"Development version: {'Yes' if info['is_dev_version'] else 'No'}")
        
        if info['git_revision']:
            typer.echo(f"Git revision: {info['git_revision']}")
        if info['git_branch']:
            typer.echo(f"Git branch: {info['git_branch']}")
            
        typer.echo(f"Build date: {info['build_date']}")
    else:
        typer.echo(format_version_message())

def main():
    """Main entry point for the CLI."""
    app()

if __name__ == "__main__":
    main()
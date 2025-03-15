"""
Download commands for fetching data from REDCap.
"""
import typer
import json
from pathlib import Path
from typing import Optional
from cieinr.config import Config

app = typer.Typer(help="Download commands for CIEINR")

@app.command("records")
def download_records(
    output_file: Optional[str] = typer.Option("records.json", help="Output file path")
):
    """
    Download records from REDCap and save them to a JSON file.
    This is currently a mock implementation that works with the test_patient.json file.
    """
    # TODO: Implement actual REDCap API integration
    # For now, we'll just copy the test_patient.json to the output_file location
    
    # Load Config to ensure API keys are set
    config = Config()
    try:
        config.validate()
    except ValueError as e:
        typer.echo(f"Error validating configuration: {e}")
        typer.echo("Please run 'cieinr setup keys' to configure your API keys.")
        raise typer.Exit(1)
    
    # Use the test patient data for now
    try:
        test_file = Path(__file__).parents[3] / ".." / ".." / "res" / "test_patient.json"
        
        if not test_file.exists():
            typer.echo(f"Test patient file not found at {test_file}")
            raise typer.Exit(1)
        
        with open(test_file, "r") as infile:
            records = json.load(infile)
        
        # Save to output file
        with open(output_file, "w") as outfile:
            json.dump(records, outfile, indent=2)
        
        typer.echo(f"Downloaded {len(records)} records to {output_file}")
        typer.echo("Note: This is using test data. Actual REDCap integration will be implemented in a future version.")
        
    except Exception as e:
        typer.echo(f"Error downloading records: {e}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
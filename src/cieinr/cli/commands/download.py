"""
Download commands for fetching data from REDCap.
"""
import typer
import json
import requests
from pathlib import Path
from typing import Optional, Dict, Any, List
from cieinr.config import Config

app = typer.Typer(help="Download commands for CIEINR")

def fetch_redcap_records(api_url: str, token: str, project_id: str = None) -> List[Dict[str, Any]]:
    """
    Fetch records from REDCap using the API.
    
    Args:
        api_url: The REDCap API URL
        token: The REDCap API token
        project_id: Optional project ID (may be included in the API URL or token)
        
    Returns:
        List of records
    """
    # Prepare REDCap API request
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
        typer.echo("Warning: No records returned from REDCap API")
    
    return records

@app.command("records")
def download_records(
    output_file: Optional[str] = typer.Option("records.json", help="Output file path"),
    use_test_data: bool = typer.Option(False, "--test", help="Use test data instead of REDCap API")
):
    """
    Download records from REDCap and save them to a JSON file.
    """
    # Load Config to ensure API keys are set
    config = Config()
    try:
        config.validate()
    except ValueError as e:
        typer.echo(f"Error validating configuration: {e}")
        typer.echo("Please run 'cieinr setup keys' to configure your API keys.")
        raise typer.Exit(1)
    
    try:
        if use_test_data:
            # Use the test patient data
            test_file = Path(__file__).parents[3] / ".." / ".." / "res" / "test_patient.json"
            
            if not test_file.exists():
                typer.echo(f"Test patient file not found at {test_file}")
                raise typer.Exit(1)
            
            with open(test_file, "r") as infile:
                records = json.load(infile)
            
            typer.echo("Using test data instead of REDCap API.")
        else:
            # Fetch from REDCap API
            typer.echo("Fetching records from REDCap API...")
            
            api_url = config.get("REDCAP_URL")
            token = config.get("REDCAP_API_TOKEN")
            project_id = config.get("REDCAP_PROJECT_ID")
            
            if not api_url or not token:
                typer.echo("Missing REDCap API URL or token. Please run 'cieinr setup keys'.")
                raise typer.Exit(1)
            
            records = fetch_redcap_records(api_url, token, project_id)
        
        # Save to output file
        with open(output_file, "w") as outfile:
            json.dump(records, outfile, indent=2)
        
        typer.echo(f"Downloaded {len(records)} records to {output_file}")
        
    except Exception as e:
        typer.echo(f"Error downloading records: {e}")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
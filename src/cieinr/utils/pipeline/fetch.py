"""Module for fetching REDCap data."""

import json
import requests
from pathlib import Path
from typing import Dict, Any, List

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
        test_file = Path(__file__).parent.parent.parent.parent.parent / "res" / "test_patient.json"
        
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
    print(f"Successfully fetched {len(records)} records from REDCap")
    return records
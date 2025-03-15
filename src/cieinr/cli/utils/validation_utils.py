"""
Validation utilities for configuration and environment variables.
"""
import os
import json
import re
import requests
from pathlib import Path
from typing import List, Dict, Any, Optional
from dotenv import dotenv_values

def validate_env(required_keys: List[str], env_path: Optional[Path] = None) -> bool:
    """
    Validate that required environment variables are present and non-empty.
    
    Args:
        required_keys: List of required environment variable names
        env_path: Path to the .env file (optional)
        
    Returns:
        bool: True if all required keys are present
        
    Raises:
        ValueError: If any required key is missing or empty
    """
    # Load environment variables
    if env_path and env_path.exists():
        env_vars = dotenv_values(env_path)
    else:
        env_vars = {k: v for k, v in os.environ.items()}
    
    # Check for missing keys
    missing = []
    for key in required_keys:
        if key not in env_vars or not env_vars[key]:
            missing.append(key)
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
    
    return True

def validate_config(config: Dict[str, Any], required_keys: List[str]) -> bool:
    """
    Validate that a configuration dictionary contains required keys.
    
    Args:
        config: Configuration dictionary to validate
        required_keys: List of required keys
        
    Returns:
        bool: True if all required keys are present
        
    Raises:
        ValueError: If any required key is missing
    """
    missing = []
    for key in required_keys:
        if key not in config or not config[key]:
            missing.append(key)
    
    if missing:
        raise ValueError(f"Missing required configuration values: {', '.join(missing)}")
    
    return True

def validate_url(url: str) -> bool:
    """
    Validate that a URL is properly formatted and reachable.
    
    Args:
        url: URL to validate
        
    Returns:
        bool: True if URL is valid
        
    Raises:
        ValueError: If URL is malformed
        ConnectionError: If URL is unreachable
    """
    # Check URL format
    url_pattern = re.compile(
        r'^(?:http|https)://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )
    
    if not url_pattern.match(url):
        raise ValueError(f"Invalid URL format: {url}")
    
    try:
        # Send a HEAD request (faster than GET for validation)
        response = requests.head(url, timeout=5)
        # Allow up to 400 for validation (some APIs return non-200 for HEAD)
        if response.status_code >= 400:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
    except requests.RequestException as e:
        raise ConnectionError(f"Unable to connect to URL: {url} - {str(e)}")
    
    return True

def validate_redcap_projects_json(file_path: Path) -> bool:
    """
    Validate a REDCap projects JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        bool: True if file is valid
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file format is invalid
    """
    if not file_path.exists():
        raise FileNotFoundError(f"REDCap projects file not found: {file_path}")
    
    try:
        with open(file_path, 'r') as f:
            projects = json.load(f)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    
    # Check if it's a list of projects
    if not isinstance(projects, list):
        raise ValueError("REDCap projects file must contain a list of projects")
    
    # Validate each project
    for project in projects:
        if not isinstance(project, dict):
            raise ValueError("Each project must be a dictionary")
        
        required_fields = ['id', 'name', 'token', 'url']
        for field in required_fields:
            if field not in project:
                raise ValueError(f"Missing required field '{field}' in project: {project.get('name', 'Unknown')}")
    
    return True
"""
Environment variable utilities for managing configuration in the CLI.
"""
import os
from pathlib import Path
from typing import Dict, Optional, List, Union
from dotenv import load_dotenv, set_key, find_dotenv

def get_env_file_path() -> Path:
    """
    Find the .env file in the current directory or above.
    
    Returns:
        Path: Path to the .env file.
    """
    env_path = find_dotenv(usecwd=True)
    if not env_path:
        env_path = '.env'
        Path(env_path).touch(exist_ok=True)
    return Path(env_path)

def load_env() -> Dict[str, str]:
    """
    Load environment variables from .env file.
    
    Returns:
        Dict: Dictionary of environment variables.
    """
    env_path = get_env_file_path()
    load_dotenv(env_path)
    
    # Load from .env file
    env_vars = {}
    if env_path.exists():
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    env_vars[key] = value.strip().strip('"')
    
    # Add any variables from os.environ that aren't in the file
    for key, value in os.environ.items():
        if key not in env_vars:
            env_vars[key] = value
    
    return env_vars

def set_env_variable(key: str, value: str) -> bool:
    """
    Set an environment variable in .env file and os.environ.
    
    Args:
        key: The environment variable name
        value: The value to set
        
    Returns:
        bool: True if successful
    """
    env_path = get_env_file_path()
    
    # Add quotes if the value contains spaces
    if ' ' in value and not (value.startswith('"') and value.endswith('"')):
        value = f'"{value}"'
    
    # Update .env file
    set_key(env_path, key, value)
    
    # Update os.environ
    os.environ[key] = value.strip('"')
    
    return True

def get_env_variable(key: str, default: Optional[str] = None) -> Optional[str]:
    """
    Get an environment variable, first trying os.environ then .env file.
    
    Args:
        key: The environment variable name
        default: Default value if not found
        
    Returns:
        str: The environment variable value or default
    """
    # First check os.environ
    value = os.environ.get(key)
    if value:
        return value
    
    # If not found, check .env file
    env_vars = load_env()
    return env_vars.get(key, default)

def validate_required_keys(required_keys: List[str]) -> bool:
    """
    Validate that required environment variables are set.
    
    Args:
        required_keys: List of required keys
        
    Returns:
        bool: True if all required keys are present and non-empty
        
    Raises:
        ValueError: If any required key is missing or empty
    """
    env_vars = load_env()
    
    missing = []
    for key in required_keys:
        if key not in env_vars or not env_vars[key]:
            missing.append(key)
    
    if missing:
        raise ValueError(f"Missing required environment variables: {', '.join(missing)}")
    
    return True
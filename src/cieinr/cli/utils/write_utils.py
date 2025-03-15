"""
Utilities for writing files and environment variables.
"""
from pathlib import Path
from typing import Union, Dict, Any, List
import re
import os

def write_env_file(env_path: Union[str, Path], key: str, value: str) -> None:
    """
    Write a key-value pair to the .env file, creating the file if it doesn't exist.
    If the key already exists, its value will be updated.
    
    Args:
        env_path: Path to the .env file
        key: The environment variable name
        value: The environment variable value
    """
    env_path = Path(env_path)
    
    # Ensure the file exists
    if not env_path.exists():
        env_path.touch()
    
    # Read the current file content
    lines = []
    if env_path.exists():
        with open(env_path, 'r') as f:
            lines = f.readlines()
    
    # Find and replace the line with the key
    key_pattern = re.compile(f'^{re.escape(key)}=.*')
    found = False
    new_lines = []
    
    for line in lines:
        if key_pattern.match(line.strip()):
            new_lines.append(f"{key}={value}\n")
            found = True
        else:
            new_lines.append(line)
    
    # If the key wasn't found, add it
    if not found:
        new_lines.append(f"{key}={value}\n")
    
    # Write the updated content back
    with open(env_path, 'w') as f:
        f.writelines(new_lines)
    
    # Update the environment variable in the current process
    os.environ[key] = value.strip('"')  # Remove quotes if present
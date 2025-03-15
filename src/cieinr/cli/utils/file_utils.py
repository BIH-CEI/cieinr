"""
File operation utilities for CIEINR.
"""
import os
import json
import requests
from pathlib import Path
from typing import Any, Dict, Union
import typer
from tqdm import tqdm

def ensure_directory_exists(directory_path: Union[str, Path]) -> Path:
    """
    Ensure that a directory exists, creating it if necessary.
    
    Args:
        directory_path: Path to the directory
        
    Returns:
        Path: Path object of the directory
    """
    path = Path(directory_path)
    path.mkdir(parents=True, exist_ok=True)
    return path

def download_file(url: str, destination: Union[str, Path], show_progress: bool = True) -> Path:
    """
    Download a file from a URL to a local destination with progress bar.
    
    Args:
        url: URL to download from
        destination: Local file path to save to
        show_progress: Whether to show a progress bar
        
    Returns:
        Path: Path to the downloaded file
    """
    dest_path = Path(destination)
    
    # Ensure the parent directory exists
    ensure_directory_exists(dest_path.parent)
    
    # Stream download with progress bar
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    block_size = 8192  # 8KB
    
    with open(dest_path, 'wb') as f:
        if show_progress and total_size > 0:
            with tqdm(total=total_size, unit='B', unit_scale=True, desc=f"Downloading {dest_path.name}") as pbar:
                for chunk in response.iter_content(block_size):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))
        else:
            for chunk in response.iter_content(block_size):
                if chunk:
                    f.write(chunk)
    
    return dest_path

def read_json(file_path: Union[str, Path]) -> Dict[str, Any]:
    """
    Read a JSON file into a dictionary.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        dict: Contents of the JSON file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file is not valid JSON
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {path}")
    
    with open(path, 'r') as f:
        return json.load(f)

def write_json(data: Dict[str, Any], file_path: Union[str, Path], indent: int = 2) -> Path:
    """
    Write a dictionary to a JSON file.
    
    Args:
        data: Dictionary to write
        file_path: Path to write to
        indent: Indentation level for JSON formatting
        
    Returns:
        Path: Path to the written file
    """
    path = Path(file_path)
    
    # Ensure the parent directory exists
    ensure_directory_exists(path.parent)
    
    with open(path, 'w') as f:
        json.dump(data, f, indent=indent)
    
    return path
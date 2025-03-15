"""
Version utility functions for CIEINR.
"""
import re
import importlib.metadata
from typing import Optional

def get_current_version() -> str:
    """
    Get the current version of the CIEINR package.
    
    Returns:
        str: The version string
    """
    try:
        return importlib.metadata.version("cieinr")
    except importlib.metadata.PackageNotFoundError:
        # If package is not installed, get from __init__.py
        try:
            from cieinr import __version__
            return __version__
        except (ImportError, AttributeError):
            return "unknown"
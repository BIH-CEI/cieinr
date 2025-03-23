"""
Utilities for working with version information.
"""

import datetime
import subprocess
from packaging.version import Version
from cieinr._version import __version__

def get_version():
    """
    Get the current version of the package.
    
    Returns:
        str: Current package version
    """
    return __version__

def get_full_version_info():
    """
    Get full version details including git information if available.
    
    Returns:
        dict: Version information with keys:
            - version: Package version string
            - is_dev_version: Whether it's a development version
            - git_revision: Git revision hash if available
            - git_branch: Git branch if available
            - build_date: Date and time when this was called
    """
    info = {
        "version": __version__,
        "is_dev_version": "dev" in __version__ or "a" in __version__,
        "git_revision": None,
        "git_branch": None,
        "build_date": datetime.datetime.now().isoformat()
    }
    
    # Try to get git revision info
    try:
        git_rev = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        info["git_revision"] = git_rev
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    
    # Try to get git branch info
    try:
        git_branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        info["git_branch"] = git_branch
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    
    return info

def version_greater_than(version_to_check):
    """
    Check if the current version is greater than the specified version.
    
    Args:
        version_to_check (str): Version to compare against
        
    Returns:
        bool: True if current version is greater, False otherwise
    """
    current = Version(__version__)
    check = Version(version_to_check)
    return current > check

def format_version_message():
    """
    Format a user-friendly version message.
    
    Returns:
        str: Formatted version message with additional details if available
    """
    info = get_full_version_info()
    message = f"CIEINR version {info['version']}"
    
    if info["git_revision"]:
        short_rev = info["git_revision"][:8]
        message += f" (git:{short_rev}"
        
        if info["git_branch"] and info["git_branch"] != "HEAD":
            message += f", {info['git_branch']}"
            
        message += ")"
    
    return message
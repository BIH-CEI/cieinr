"""Functions for handling dates and timestamps."""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from typing import Optional, Dict

def process_date(date_input: Optional[str]) -> Optional[datetime]:
    """
    Converts a date string into a datetime object.
    
    Args:
        date_input: Date string in ISO format (YYYY-MM-DD)
        
    Returns:
        Datetime object or None if conversion fails
    """
    if not date_input:
        return None
        
    try:
        return datetime.fromisoformat(date_input)
    except Exception as e:
        print(f"Error converting date to datetime: {e}")
        return None

def convert_date_to_iso_age(event_date_str: str, dob_str: str) -> Optional[str]:
    """
    Convert an event date and a date of birth into an ISO8601 duration.
    
    Args:
        event_date_str: Event date in ISO format
        dob_str: Date of birth in ISO format
        
    Returns:
        ISO8601 duration string (e.g., "P10Y2M") or None if conversion fails
    """
    if not event_date_str or not dob_str:
        return None
        
    try:
        # Convert dates to datetime objects
        dob = datetime.fromisoformat(dob_str)
        event_date = datetime.fromisoformat(event_date_str)
        
        # Calculate difference
        delta = relativedelta(event_date, dob)
        
        # Format as ISO8601 duration
        return f"P{delta.years}Y{delta.months}M"
    except Exception as e:
        print(f"Error calculating ISO age: {e}")
        return None

def create_timestamp_dict(date_str: Optional[str]) -> Optional[Dict[str, str]]:
    """
    Creates a timestamp dictionary for Phenopackets.
    
    Args:
        date_str: Date string in ISO format
        
    Returns:
        Dictionary with a timestamp field or None if date is invalid
    """
    if not date_str:
        return None
        
    return {"timestamp": date_str}
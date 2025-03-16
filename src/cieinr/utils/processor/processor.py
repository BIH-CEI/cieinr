"""DataProcessor class for handling field mapping and transformations."""

from datetime import datetime
from dateutil.relativedelta import relativedelta
import logging
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

class DataProcessor:
    """
    DataProcessor handles field access, mapping, and transformation for data processing.
    
    This class provides utilities to:
    1. Access data fields using mapping configuration
    2. Process codes, dates and other types of data
    3. Fetch labels and mappings from enums and dictionaries
    4. Process repeated elements
    """
    
    def __init__(self, mapping_config: Dict[str, Any]):
        """
        Initialize the DataProcessor with mapping configuration.
        
        Args:
            mapping_config: Dictionary of field mappings
        """
        self.mapping_config = mapping_config
    
    def get_field(self, 
                 data: Dict[str, Any], 
                 field_name: str,
                 highest_instance: bool = False) -> Any:
        """
        Fetches a field value from data based on the mapping configuration.
        
        Args:
            data: Input data dictionary
            field_name: The name of the field to fetch
            highest_instance: Whether to fetch the value from the highest instance
            
        Returns:
            The value of the requested field or None if not found
        """
        field_path = self.mapping_config.get(field_name)
        if field_path is None:
            logger.warning(f"Field '{field_name}' not found in mapping_config.")
            return None
            
        try:
            if highest_instance:
                # For handling repeated elements, get the highest instance
                # This would need a more complex implementation based on your data structure
                pass
            else:
                # Simple field access
                return data.get(field_path)
        except Exception as e:
            logger.error(f"Failed to fetch field '{field_name}' with path '{field_path}': {e}")
            return None
    
    def prefer_non_empty_field(self, data: Dict[str, Any], fields: List[str]) -> Any:
        """
        Returns the first non-empty field value from a list of fields.
        
        Args:
            data: Input data dictionary
            fields: List of field names to check
            
        Returns:
            The first non-empty field value or None if all are empty
        """
        for field in fields:
            value = self.get_field(data, field)
            if value:
                return value
        
        return None
    
    @staticmethod
    def process_date(date_input: str) -> Optional[datetime]:
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
            logger.error(f"Error converting date to datetime: {e}")
            return None
    
    @staticmethod
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
            logger.error(f"Error calculating ISO age: {e}")
            return None
    
    @staticmethod
    def process_code(code: str) -> Optional[str]:
        """
        Process a code to ensure proper format.
        
        Args:
            code: Code to process (e.g., "hp_0012826")
            
        Returns:
            Processed code (e.g., "HP:0012826") or None if invalid
        """
        if not code:
            return None
            
        # Determine delimiter
        delimiter = "_" if "_" in code else ":" if ":" in code else None
        if not delimiter:
            return code
            
        # Split prefix and code
        prefix, rest = code.split(delimiter, 1)
        prefix_upper = prefix.upper()
        
        # Handle transformation based on prefix
        if delimiter == "_":
            # Replace the first "_" with ":"
            return f"{prefix_upper}:{rest}"
        elif delimiter == ":":
            # Ensure prefix is uppercase
            return f"{prefix_upper}:{rest}"
            
        return code
    
    def fetch_label(self, code: str, enum_class=None) -> Optional[str]:
        """
        Fetch label for a code from an enum or mapping.
        
        Args:
            code: Code to look up
            enum_class: Optional enum class to use
            
        Returns:
            Label for the code or None if not found
        """
        if enum_class:
            try:
                # Try to get label from enum
                enum_value = getattr(enum_class, code, None)
                if enum_value and hasattr(enum_value, 'description'):
                    return enum_value.description
            except (AttributeError, ValueError) as e:
                logger.warning(f"Error getting label from enum: {e}")
                
        # Handle fallback for when enum is not provided or lookup fails
        return None
        
    @staticmethod
    def generate_unique_id(length: int = 30, used_ids: Optional[set] = None) -> str:
        """
        Generate a unique ID.
        
        Args:
            length: Length of the ID to generate
            used_ids: Set of already used IDs
            
        Returns:
            Unique ID string
        """
        import uuid
        
        if used_ids is None:
            used_ids = set()
            
        while True:
            unique_id = uuid.uuid4().hex[:length]
            if unique_id not in used_ids:
                used_ids.add(unique_id)
                return unique_id
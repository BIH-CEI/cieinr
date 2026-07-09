# individual_block.py
from typing import Dict, Any, Optional

def get_combined_dob(data: Dict[str, Any]) -> Optional[str]:
    # Navigate the nested structure in your JSON
    demographics = data.get("patient_demographics_initial_form", {})
    
    year = demographics.get("birth_year")
    month = demographics.get("birth_month")

    if year and month:
        return f"{year}-{str(month).zfill(2)}-01"
    return None

# We keep this for reference, but the mapper needs the field in the record
INDIVIDUAL_BLOCK = {
    "id_field": "record_id",
    "date_of_birth_field": "computed_dob",
    "sex_field": "UNKNOWN",
    "time_at_last_encounter_field": "patient_demographics_initial_form.visit_date_demographics",
}
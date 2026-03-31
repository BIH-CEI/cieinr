import json
from src.cieinr.datamodel.mappings.phenopackets.individual_block import get_combined_dob

with open("res/patient_linkml.json", "r") as f:
    records = json.load(f)

for record in records:
    record["computed_dob"] = get_combined_dob(record)

with open("res/patient_linkml_ready.json", "w") as f:
    json.dump(records, f, indent=2)
# src/cieinr/datamodel/mappers/redcap_to_linkml/map_lymphocyte_function.py

def map_lymphocyte_function(record):
    """
    Map REDCap record data to the LymphocyteFunction LinkML class format.
    
    Args:
        record (dict): The REDCap record data
    
    Returns:
        dict: The mapped data in LinkML format
    """
    return {
        "completetion_date_lymphfunc": record.get("completetion_date_lymphfunc", ""),  # Date of completing this form.
        "lymphfunc_test": record.get("lymphfunc_test", ""),  # Please provide the following information at EACH d
        "lymphfunc_ncit_c88791": record.get("lymphfunc_ncit_c88791", ""),  # Phytohemagglutinin (PHA)
        "phamonth": record.get("phamonth", ""),  # Month
        "phayear": record.get("phayear", ""),  # Year
        "lymphfunc_ncit_c88791_val": record.get("lymphfunc_ncit_c88791_val", ""),  # PHA Result
        "lymphfunc_ncit_c74017": record.get("lymphfunc_ncit_c74017", ""),  # Anti-CD3/CD28 Antibody
        "anticd3_cd28month": record.get("anticd3_cd28month", ""),  # Month
        "anticd3_cd28_year": record.get("anticd3_cd28_year", ""),  # Year
        "lymphfunc_ncit_c74017_val": record.get("lymphfunc_ncit_c74017_val", ""),  # Anti-CD3/CD28 Antibody Result
        "lymphfunc_ncit_c88774": record.get("lymphfunc_ncit_c88774", ""),  # Concanavalin A (ConA)
        "conamonth": record.get("conamonth", ""),  # Month
        "conayear": record.get("conayear", ""),  # Year
        "lymphfunc_ncit_c88774_val": record.get("lymphfunc_ncit_c88774_val", ""),  # ConA Result
        "lymphfunc_ncit_c88789": record.get("lymphfunc_ncit_c88789", ""),  # Pokeweed mitogen (PWM)
        "pwmmonth": record.get("pwmmonth", ""),  # Month
        "pwmyear": record.get("pwmyear", ""),  # Year
        "lymphfunc_ncit_c88789_val": record.get("lymphfunc_ncit_c88789_val", ""),  # PWM Result
        "lymphfunc_ncit_c17166": record.get("lymphfunc_ncit_c17166", ""),  # Staph Aureus Protein A (SpA)
        "spamonth": record.get("spamonth", ""),  # Month
        "spayear": record.get("spayear", ""),  # Year
        "lymphfunc_ncit_c17166_val": record.get("lymphfunc_ncit_c17166_val", ""),  # SpA Result
        "lymphfunc_ncit_c85185": record.get("lymphfunc_ncit_c85185", ""),  # Tetanus
        "tetanusmonth": record.get("tetanusmonth", ""),  # Month
        "tetanusyear": record.get("tetanusyear", ""),  # Year
        "lymphfunc_ncit_c85185_val": record.get("lymphfunc_ncit_c85185_val", ""),  # Tetanus Result
        "lymphfunc_ncit_c34541": record.get("lymphfunc_ncit_c34541", ""),  # Diphtheria
        "diphtheriamonth": record.get("diphtheriamonth", ""),  # Month
        "diphtheriayear": record.get("diphtheriayear", ""),  # Year
        "lymphfunc_ncit_c34541_val": record.get("lymphfunc_ncit_c34541_val", ""),  # Diphtheria Result
        "lymphfunc_ncit_c77163": record.get("lymphfunc_ncit_c77163", ""),  # Candida
        "candidamonth": record.get("candidamonth", ""),  # Month
        "candidayear": record.get("candidayear", ""),  # Year
        "lymphfunc_ncit_c77163_val": record.get("lymphfunc_ncit_c77163_val", ""),  # Candida Result
        "lymphfunc_ncit_c116203": record.get("lymphfunc_ncit_c116203", ""),  # Natural Killer (NK) Cell Cytotoxicity
        "nkcellcytomonth": record.get("nkcellcytomonth", ""),  # Month
        "nkcellcytoyear": record.get("nkcellcytoyear", ""),  # Year
        "lymphfunc_ncit_c116203_val": record.get("lymphfunc_ncit_c116203_val", ""),  # NK cell Cytotoxicity Result
        "lymph_fn": record.get("lymph_fn", ""),  # Please upload test report(s). Please, REMOVE PATIE
    }

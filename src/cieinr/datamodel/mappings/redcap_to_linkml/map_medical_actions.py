def map_allergic_reactions(record):
    """
    Map REDCap data for the Allergic Reactions form.
    """
    return {
        "completion_date_allergy": record.get("completion_date_allergy", ""),
        "allergic_yes": record.get("allergic_yes", ""),
        "procedure_7": record.get("procedure_7", ""),
        "allergic_test_date": record.get("allergic_test_date", "")
    }

def map_antimicrobial_medications(record):
    """
    Map REDCap data for the Antimicrobial Medications form.
    """
    return {
        "date_antimicrobial_form": record.get("date_antimicrobial_form", ""),
        "procedure_9": record.get("procedure_9", ""),
        "procedure_8": record.get("procedure_8", "")
    }

def map_antimicrobial_medications_annual(record):
    """
    Map REDCap data for the Antimicrobial Medications Annual form.
    """
    return {
        "date_antimicrobial_form_v2": record.get("date_antimicrobial_form_v2", ""),
        "procedure_8_v2": record.get("procedure_8_v2", "")
    }

def map_immunoglobulin_infusions(record):
    """
    Map REDCap data for the Immunoglobulin Infusions form.
    """
    return {
        "date_ig_form": record.get("date_ig_form", ""),
        "procedure_10": record.get("procedure_10", ""),
        "currently_ig_therapy": record.get("currently_ig_therapy", ""),
        "date_ig_initiation": record.get("date_ig_initiation", ""),
        "ig_termination": record.get("ig_termination", "")
    }

def map_immunoglobulin_infusions_annual(record):
    """
    Map REDCap data for the Immunoglobulin Infusions Annual form.
    """
    return {
        "date_ig_form_v2": record.get("date_ig_form_v2", ""),
        "currently_ig_therapy_v2": record.get("currently_ig_therapy_v2", ""),
        "date_ig_initiation_v2": record.get("date_ig_initiation_v2", ""),
        "ig_termination_v2": record.get("ig_termination_v2", "")
    }

def map_transfusion_treatments(record):
    """
    Map REDCap data for the Transfusion Treatments form.
    """
    return {
        "date_transfusion_form": record.get("date_transfusion_form", ""),
        "procedure_11": record.get("procedure_11", ""),
        "procedure_11_type": record.get("procedure_11_type", ""),
        "ad_ev_transf": record.get("ad_ev_transf", "")
    }

def map_immunomodulator_medication(record):
    """
    Map REDCap data for the Immunomodulator Medication form.
    """
    return {
        "procedure_12": record.get("procedure_12", ""),
        "imm_modulat": record.get("imm_modulat", ""),
        "completion_date_immunomod": record.get("completion_date_immunomod", "")
    }

def map_surgeries_and_procedures(record):
    """
    Map REDCap data for the Surgeries and Procedures form.
    """
    return {
        "completion_date_surgery": record.get("completion_date_surgery", ""),
        "procedure_13": record.get("procedure_13", ""),
        "procedure_13_date": record.get("procedure_13_date", ""),
        "surg_proced": record.get("surg_proced", "")
    }

def map_respiratory_support(record):
    """
    Map REDCap data for the Respiratory Support form.
    """
    return {
        "date_respiratory_support": record.get("date_respiratory_support", ""),
        "procedure_16": record.get("procedure_16", ""),
        "procedure_16_type": record.get("procedure_16_type", ""),
        "resp_other": record.get("resp_other", ""),
        "procedure_16_start": record.get("procedure_16_start", "")
    }

def map_hematopoietic_stem_cells_transplantation(record):
    """
    Map REDCap data for the Hematopoietic Stem Cells Transplantation form.
    """
    return {
        "procedure_17": record.get("procedure_17", ""),
        "what_transplant_number": record.get("what_transplant_number", ""),
        "transplant_number": record.get("transplant_number", ""),
        "gvhd": record.get("gvhd", ""),
        "type_gvhd": record.get("type_gvhd", ""),
        "other_gvhd": record.get("other_gvhd", "")
    }

def map_endoscopy_abdominal_ultrasound(record):
    """
    Map REDCap data for the Endoscopy/Abdominal Ultrasound form.
    """
    return {
        "endoscopy_us": record.get("endoscopy_us", ""),
        "date_endoscopy_pre_dx": record.get("date_endoscopy_pre_dx", ""),
        "time_endoscopy": record.get("time_endoscopy", ""),
        "endoscopy_result_pre_dx": record.get("endoscopy_result_pre_dx", ""),
        "ultrsouns_result": record.get("ultrsouns_result", ""),
        "resul_us": record.get("resul_us", ""),
        "pdf_endo_result_pre_dx": record.get("pdf_endo_result_pre_dx", ""),
        "pdf_abdominal_us_pre_dx": record.get("pdf_abdominal_us_pre_dx", ""),
        "procedure_6": record.get("procedure_6", ""),
        "other_instrumental_results": record.get("other_instrumental_results", ""),
        "other_endoscopy": record.get("other_endoscopy", "")
    }
    
def map_gene_therapy(record):
    """
    Map REDCap data for the Gene Therapy form to LinkML format.
    """
    return {
        "completion_date_gene": record.get("completion_date_gene", ""),
        "procedure_19": record.get("procedure_19", ""),
        "date_pft_annual": record.get("date_pft_annual", ""),
        "date_chest_xray": record.get("date_chest_xray", ""),
        "fev1_annual": record.get("fev1_annual", ""),
        "xray_results_annual": record.get("xray_results_annual", ""),
        "pdf_chest_xray_annual": record.get("pdf_chest_xray_annual", ""),
        "hrct_result_annual": record.get("hrct_result_annual", ""),
        "pdf_chest_ct_annual": record.get("pdf_chest_ct_annual", ""),
        "other_investigations_1": record.get("other_investigations_1", "")
    }

def map_solid_organ_transplantation_therapy(record):
    """
    Map REDCap data for the Solid Organ Transplantation Therapy form to LinkML format.
    """
    return {
        "procedure_18": record.get("procedure_18", ""),
        "procedure_18_date": record.get("procedure_18_date", ""),
    }

def map_death_form(record):
    """
    Map REDCap data for the Death Form to LinkML format.
    """
    return {
        "snomedct_398299004": record.get("snomedct_398299004", ""),
        "snomedct_184305005": record.get("snomedct_184305005", ""),
        "snomedct_184305005_other": record.get("snomedct_184305005_other", ""),
        "unknown_death": record.get("unknown_death", ""),
    }
    
def map_xray_ct_ini(record):
    """
    Map REDCap data for the Xray and CT Initial form to LinkML format.
    """
    return {
        "completion_date_pft": record.get("completion_date_pft", ""),
        "procedure_1": record.get("procedure_1", ""),
        "date_pft_annual": record.get("date_pft_annual", ""),
        "date_chest_xray": record.get("date_chest_xray", ""),
        "fev1_annual": record.get("fev1_annual", ""),
        "xray_results_annual": record.get("xray_results_annual", ""),
        "pdf_chest_xray_annual": record.get("pdf_chest_xray_annual", ""),
        "hrct_result_annual": record.get("hrct_result_annual", ""),
        "pdf_chest_ct_annual": record.get("pdf_chest_ct_annual", ""),
        "other_investigations_1": record.get("other_investigations_1", ""),
    }

def map_xray_ct_annual(record):
    """
    Map REDCap data for the Xray and CT Annual form to LinkML format.
    """
    return {
        "completion_date_pft_v2": record.get("completion_date_pft_v2", ""),
        "procedure_1_v2": record.get("procedure_1_v2", ""),
        "date_pft_annual_v2": record.get("date_pft_annual_v2", ""),
        "fev1_annual_v2": record.get("fev1_annual_v2", ""),
        "xray_results_annual_v2": record.get("xray_results_annual_v2", ""),
        "pdf_chest_xray_annual_v2": record.get("pdf_chest_xray_annual_v2", ""),
        "hrct_result_annual_v2": record.get("hrct_result_annual_v2", ""),
        "pdf_chest_ct_annual_v2": record.get("pdf_chest_ct_annual_v2", ""),
        "other_investigations_1_v2": record.get("other_investigations_1_v2", ""),
    }

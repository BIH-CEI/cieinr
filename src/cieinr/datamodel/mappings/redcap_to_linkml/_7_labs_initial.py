def map_cbc(record):
    """
    Map REDCap data for the CBC form to the LinkML CBC class format.
    """
    return {
        "cbc_type": record.get("cbc_type", ""),
        "cbc_date": record.get("cbc_date", ""),
        "cbc_haemoglobin": record.get("cbc_haemoglobin", ""),
        "cbc_haemoglobin_unit": record.get("cbc_haemoglobin_unit", ""),
        "cbc_haemoglobin_range": record.get("cbc_haemoglobin_range", ""),
        "cbc_haemoglobin_val": record.get("cbc_haemoglobin_val", ""),
        "cbc_platelets": record.get("cbc_platelets", ""),
        "cbc_platelets_unit": record.get("cbc_platelets_unit", ""),
        "cbc_platelets_range": record.get("cbc_platelets_range", ""),
        "cbc_platelets_val": record.get("cbc_platelets_val", ""),
        "cbc_leukocytes": record.get("cbc_leukocytes", ""),
        "cbc_leukocytes_unit": record.get("cbc_leukocytes_unit", ""),
        "cbc_leukocytes_range": record.get("cbc_leukocytes_range", ""),
        "cbc_leukocytes_val": record.get("cbc_leukocytes_val", ""),
        "cbc_neutrophils": record.get("cbc_neutrophils", ""),
        "cbc_neutrophils_unit": record.get("cbc_neutrophils_unit", ""),
        "cbc_neutrophils_range": record.get("cbc_neutrophils_range", ""),
        "cbc_neutrophils_val": record.get("cbc_neutrophils_val", ""),
        "cbc_eosinophils": record.get("cbc_eosinophils", ""),
        "cbc_eosinophils_unit": record.get("cbc_eosinophils_unit", ""),
        "cbc_eosinophils_range": record.get("cbc_eosinophils_range", ""),
        "cbc_eosinophils_val": record.get("cbc_eosinophils_val", ""),
        "cbc_lymphocytes": record.get("cbc_lymphocytes", ""),
        "cbc_lymphocytes_unit": record.get("cbc_lymphocytes_unit", ""),
        "cbc_lymphocytes_range": record.get("cbc_lymphocytes_range", ""),
        "cbc_lymphocytes_val": record.get("cbc_lymphocytes_val", ""),
        "cbc_monocytes": record.get("cbc_monocytes", ""),
        "cbc_monocytes_unit": record.get("cbc_monocytes_unit", ""),
        "cbc_monocytes_range": record.get("cbc_monocytes_range", ""),
        "cbc_monocytes_val": record.get("cbc_monocytes_val", "")
    }
    
def map_lymphopheno_initial(record):
    """
    Map REDCap data for the initial Lymphocyte Phenotype form to LinkML format.
    
    Args:
        record (dict): The REDCap record data.
        
    Returns:
        dict: The mapped data in LinkML format.
    """
    return {
        "lympheno_test": record.get("lympheno_test", ""),
        "lympheno_test_date": record.get("lympheno_test_date", ""),
        "lympheno_loinc_8122_4": record.get("lympheno_loinc_8122_4", ""),
        "lympheno_loinc_8122_4_unit": record.get("lympheno_loinc_8122_4_unit", ""),
        "lympheno_loinc_8122_4_unito": record.get("lympheno_loinc_8122_4_unito", ""),
        "lympheno_loinc_8122_4_val": record.get("lympheno_loinc_8122_4_val", ""),
        "lympheno_loinc_8122_4_int": record.get("lympheno_loinc_8122_4_int", ""),
        "lympheno_loinc_24467_3": record.get("lympheno_loinc_24467_3", ""),
        "lympheno_loinc_24467_3_unit": record.get("lympheno_loinc_24467_3_unit", ""),
        "lympheno_loinc_24467_3_unito": record.get("lympheno_loinc_24467_3_unito", ""),
        "lympheno_loinc_24467_3_val": record.get("lympheno_loinc_24467_3_val", ""),
        "lympheno_loinc_24467_3_int": record.get("lympheno_loinc_24467_3_int", ""),
        "lympheno_loinc_14135_8": record.get("lympheno_loinc_14135_8", ""),
        "lympheno_loinc_14135_8_unit": record.get("lympheno_loinc_14135_8_unit", ""),
        "lympheno_loinc_14135_8_unito": record.get("lympheno_loinc_14135_8_unito", ""),
        "lympheno_loinc_14135_8_val": record.get("lympheno_loinc_14135_8_val", ""),
        "lympheno_loinc_14135_8_int": record.get("lympheno_loinc_14135_8_int", ""),
        "lympheno_loinc_8116_6": record.get("lympheno_loinc_8116_6", ""),
        "lympheno_loinc_8116_6_unit": record.get("lympheno_loinc_8116_6_unit", ""),
        "lympheno_loinc_8116_6_unito": record.get("lympheno_loinc_8116_6_unito", ""),
        "lympheno_loinc_8116_6_val": record.get("lympheno_loinc_8116_6_val", ""),
        "lympheno_loinc_8116_6_int": record.get("lympheno_loinc_8116_6_int", ""),
        "lympheno_loinc_9558_8": record.get("lympheno_loinc_9558_8", ""),
        "lympheno_loinc_9558_8_unit": record.get("lympheno_loinc_9558_8_unit", ""),
        "lympheno_loinc_9558_8_unito": record.get("lympheno_loinc_9558_8_unito", ""),
        "lympheno_loinc_9558_8_val": record.get("lympheno_loinc_9558_8_val", ""),
        "lympheno_loinc_9558_8_int": record.get("lympheno_loinc_9558_8_int", ""),
        "lympheno_loinc_9728_7": record.get("lympheno_loinc_9728_7", ""),
        "lympheno_loinc_9728_7_unit": record.get("lympheno_loinc_9728_7_unit", ""),
        "lympheno_loinc_9728_7_unito": record.get("lympheno_loinc_9728_7_unito", ""),
        "lympheno_loinc_9728_7_val": record.get("lympheno_loinc_9728_7_val", ""),
        "lympheno_loinc_9728_7_int": record.get("lympheno_loinc_9728_7_int", ""),
        "lymphopheno_other": record.get("lymphopheno_other", ""),
        "lymphopheno_test": record.get("lymphopheno_test", "")
    }

    """
    Map REDCap data for the initial Lymphocyte Phenotype form.
    """
    return {
        "lympheno_test": record.get("lympheno_test", ""),
        "lympheno_test_date": record.get("lympheno_test_date", ""),
        "lympheno_loinc_8122_4_int": record.get("lympheno_loinc_8122_4_int", ""),
        "lympheno_loinc_8122_4_unito": record.get("lympheno_loinc_8122_4_unito", ""),
        "lympheno_loinc_24467_3_int": record.get("lympheno_loinc_24467_3_int", ""),
        "lympheno_loinc_24467_3_val": record.get("lympheno_loinc_24467_3_val", ""),
        "lympheno_loinc_14135_8_int": record.get("lympheno_loinc_14135_8_int", ""),
        "lympheno_loinc_14135_8_val": record.get("lympheno_loinc_14135_8_val", ""),
        "lympheno_loinc_8116_6_int": record.get("lympheno_loinc_8116_6_int", ""),
        "lympheno_loinc_8116_6_val": record.get("lympheno_loinc_8116_6_val", ""),
        "lympheno_loinc_9558_8_int": record.get("lympheno_loinc_9558_8_int", ""),
        "lympheno_loinc_9558_8_val": record.get("lympheno_loinc_9558_8_val", ""),
        "lympheno_loinc_9728_7_int": record.get("lympheno_loinc_9728_7_int", ""),
        "lympheno_loinc_9728_7_val": record.get("lympheno_loinc_9728_7_val", ""),
        "lymphopheno_other": record.get("lymphopheno_other", ""),
        "lymphopheno_test": record.get("lymphopheno_test", "")
    }



def map_lymphfunc_initial(record):
    """
    Map REDCap data for the initial Lymphocyte Function/NK Cytotoxicity form.
    """
    return {
        "lymphfunc_test": record.get("lymphfunc_test", ""),
        "lymphfunc_date": record.get("lymphfunc_date", ""),
        "lymphfunc_ncit_c88791": record.get("lymphfunc_ncit_c88791", ""),
        "lymphfunc_ncit_c88791_val": record.get("lymphfunc_ncit_c88791_val", ""),
        "lymphfunc_ncit_c74017": record.get("lymphfunc_ncit_c74017", ""),
        "lymphfunc_ncit_c74017_val": record.get("lymphfunc_ncit_c74017_val", ""),
        "lymphfunc_ncit_c88774": record.get("lymphfunc_ncit_c88774", ""),
        "lymphfunc_ncit_c88774_val": record.get("lymphfunc_ncit_c88774_val", ""),
        "lymphfunc_ncit_c88789": record.get("lymphfunc_ncit_c88789", ""),
        "lymphfunc_ncit_c88789_val": record.get("lymphfunc_ncit_c88789_val", ""),
        "lymphfunc_ncit_c17166": record.get("lymphfunc_ncit_c17166", ""),
        "lymphfunc_ncit_c17166_val": record.get("lymphfunc_ncit_c17166_val", ""),
        "lymphfunc_ncit_c85185": record.get("lymphfunc_ncit_c85185", ""),
        "lymphfunc_ncit_c85185_val": record.get("lymphfunc_ncit_c85185_val", ""),
        "lymphfunc_ncit_c34541": record.get("lymphfunc_ncit_c34541", ""),
        "lymphfunc_ncit_c34541_val": record.get("lymphfunc_ncit_c34541_val", ""),
        "lymphfunc_ncit_c77163": record.get("lymphfunc_ncit_c77163", ""),
        "lymphfunc_ncit_c77163_val": record.get("lymphfunc_ncit_c77163_val", ""),
        "lymphfunc_ncit_c116203": record.get("lymphfunc_ncit_c116203", ""),
        "lymphfunc_ncit_c116203_val": record.get("lymphfunc_ncit_c116203_val", ""),
        "lymph_fn": record.get("lymph_fn", "")
    }


def map_tcr_initial(record):
    """
    Map REDCap data for the TCR Initial form to LinkML format.
    """
    return {
        "tcr_test": record.get("tcr_test", ""),
        "type_tcr_test": record.get("type_tcr_test", ""),
        "date_tcr_test": record.get("date_tcr_test", ""),
        "tcr_v_beta_response": record.get("tcr_v_beta_response", ""),
        "tcr_v_pdf_test": record.get("tcr_v_pdf_test", "")
    }


def map_trec_krec(record):
    """
    Map REDCap data for the TREC/KREC form.
    """
    return {
        "trec_test": record.get("trec_test", ""),
        "type_trec_test": record.get("type_trec_test", ""),
        "date_trec_test": record.get("date_trec_test", ""),
        "trectest_result": record.get("trectest_result", ""),
        "trec_level": record.get("trec_level", ""),
        "krec_test": record.get("krec_test", ""),
        "type_krec_test": record.get("type_krec_test", ""),
        "date_krec": record.get("date_krec", ""),
        "krec_test_result": record.get("krec_test_result", ""),
        "krec_level_custom": record.get("krec_level_custom", ""),
        "trec_pdf": record.get("trec_pdf", "")
    }

def map_phagocyte_function(record):
    """
    Map REDCap data for the initial Phagocyte Function form.
    """
    return {
        "phagocyte_function_test": record.get("phagocyte_function_test", ""),
        "phagocyte_test_date": record.get("phagocyte_test_date", ""),
        "neutrophil_test": record.get("neutrophil_test", ""),
        "other_test": record.get("other_test", ""),
        "nph_test_result": record.get("nph_test_result", ""),
        "nph_test_results": record.get("nph_test_results", ""),
        "flow_adhesion_val": record.get("flow_adhesion_val", ""),
        "please_upload_flow_cytomet": record.get("please_upload_flow_cytomet", "")
    }


def map_autoantibodies_initial(record):
    """
    Map REDCap data for the Autoantibodies Initial form to LinkML format.
    """
    return {
        "autoantibodies_test": record.get("autoantibodies_test", ""),
        "autoantibodies_test_date": record.get("autoantibodies_test_date", ""),
        "autoanti_ana_val": record.get("autoanti_ana_val", ""),
        "autoanti_anca_val": record.get("autoanti_anca_val", ""),
        "autoanti_ena_val": record.get("autoanti_ena_val", ""),
        "autoanti_anti_tpo_val": record.get("autoanti_anti_tpo_val", ""),
        "autoanti_anti_neu_val": record.get("autoanti_anti_neu_val", ""),
        "autoanti_anti_plat_val": record.get("autoanti_anti_plat_val", ""),
        "autoanti_iga_ttg_val": record.get("autoanti_iga_ttg_val", ""),
        "autoanti_dat_val": record.get("autoanti_dat_val", ""),
        "other_autoanti_test": record.get("other_autoanti_test", ""),
        "other_autoanti_test_3": record.get("other_autoanti_test_3", ""),
        "other_autoanti_test_4": record.get("other_autoanti_test_4", ""),
        "other_autoanti_test_2": record.get("other_autoanti_test_2", ""),
        "other_autoanti_val": record.get("other_autoanti_val", ""),
        "other_autoanti_val_3": record.get("other_autoanti_val_3", ""),
        "other_autoanti_val_4": record.get("other_autoanti_val_4", ""),
        "other_autoanti_val_2": record.get("other_autoanti_val_2", "")
    }
    
def map_immunoglobulin_initial(record):
    """
    Map REDCap data for the Immunoglobulin Initial form to LinkML format.
    """
    return {
        "type_immunologbulins_test": record.get("type_immunologbulins_test", ""),
        "immmunglobulin_test_date": record.get("immmunglobulin_test_date", ""),
        "igrt_result": record.get("igrt_result", ""),
        "immmunglobulin_igg": record.get("immmunglobulin_igg", ""),
        "immmunglobulin_igg_val": record.get("immmunglobulin_igg_val", ""),
        "immmunglobulin_igg_int": record.get("immmunglobulin_igg_int", ""),
        "immmunglobulin_iga": record.get("immmunglobulin_iga", ""),
        "immmunglobulin_iga_val": record.get("immmunglobulin_iga_val", ""),
        "immmunglobulin_iga_int": record.get("immmunglobulin_iga_int", ""),
        "immmunglobulin_igm": record.get("immmunglobulin_igm", ""),
        "immmunglobulin_igm_val": record.get("immmunglobulin_igm_val", ""),
        "immmunglobulin_igm_int": record.get("immmunglobulin_igm_int", ""),
        "immmunglobulin_ige": record.get("immmunglobulin_ige", ""),
        "immmunglobulin_ige_val": record.get("immmunglobulin_ige_val", ""),
        "immmunglobulin_ige_int": record.get("immmunglobulin_ige_int", "")
    }
    
def map_isohemagglutinins_initial(record):
    """
    Map REDCap data for the Isohemagglutinins Initial form to LinkML format.
    """
    return {
        "ig1_eval": record.get("ig1_eval", ""),
        "date_subsets": record.get("date_subsets", ""),
        "igg1_val": record.get("igg1_val", ""),
        "igg1_int": record.get("igg1_int", ""),
        "igg2_val": record.get("igg2_val", ""),
        "igg2_int": record.get("igg2_int", ""),
        "igg3_val": record.get("igg3_val", ""),
        "igg3_int": record.get("igg3_int", ""),
        "igg4_val": record.get("igg4_val", ""),
        "igg4_int": record.get("igg4_int", ""),
        "isohaem_eval": record.get("isohaem_eval", ""),
        "isohaem_date": record.get("isohaem_date", ""),
        "patient_blood_group": record.get("patient_blood_group", ""),
        "a_ab": record.get("a_ab", ""),
        "a_ab_val": record.get("a_ab_val", ""),
        "b_ab": record.get("b_ab", ""),
        "b_ab_val": record.get("b_ab_val", ""),
        "m_protein_yes": record.get("m_protein_yes", ""),
        "m_protein_date": record.get("m_protein_date", ""),
        "m_protein_val": record.get("m_protein_val", ""),
        "m_protein_pdf": record.get("m_protein_pdf", "")
    }
    
def map_complement_initial(record):
    """
    Map REDCap data for the Complement Initial form to LinkML format.
    """
    return {
        "complement_evaluation": record.get("complement_evaluation", ""),
        "complement_time": record.get("complement_time", ""),
        "complement_date": record.get("complement_date", ""),
        "ch50": record.get("ch50", ""),
        "ch50_int": record.get("ch50_int", ""),
        "ch50_val": record.get("ch50_val", ""),
        "ch50_unit": record.get("ch50_unit", ""),
        "ch100": record.get("ch100", ""),
        "ch100_int": record.get("ch100_int", ""),
        "ch100_val": record.get("ch100_val", ""),
        "ch100_unit": record.get("ch100_unit", ""),
        "complement_c1q": record.get("complement_c1q", ""),
        "complement_c1q_int": record.get("complement_c1q_int", ""),
        "complement_c1q_val": record.get("complement_c1q_val", ""),
        "complement_c1q_unit": record.get("complement_c1q_unit", ""),
        "complement_c2": record.get("complement_c2", ""),
        "complement_c2_int": record.get("complement_c2_int", ""),
        "complement_c2_val": record.get("complement_c2_val", ""),
        "complement_c2_unit": record.get("complement_c2_unit", ""),
        "complement_c3": record.get("complement_c3", ""),
        "complement_c3_int": record.get("complement_c3_int", ""),
        "complement_c3_val": record.get("complement_c3_val", ""),
        "complement_c3_unit": record.get("complement_c3_unit", ""),
        "complement_c4": record.get("complement_c4", ""),
        "complement_c4_int": record.get("complement_c4_int", ""),
        "complement_c4_val": record.get("complement_c4_val", ""),
        "complement_c4_unit": record.get("complement_c4_unit", ""),
        "mannose_bind_lectin": record.get("mannose_bind_lectin", ""),
        "mannose_bind_lectin_int": record.get("mannose_bind_lectin_int", ""),
        "mannose_bind_lectin_val": record.get("mannose_bind_lectin_val", ""),
        "mannose_bind_lectin_unit": record.get("mannose_bind_lectin_unit", ""),
        "ficolin_3": record.get("ficolin_3", ""),
        "ficolin_3_int": record.get("ficolin_3_int", ""),
        "ficolin_3_val": record.get("ficolin_3_val", ""),
        "ficolin_3_unit": record.get("ficolin_3_unit", ""),
        "masps": record.get("masps", ""),
        "masps_descr": record.get("masps_descr", ""),
        "masps_int": record.get("masps_int", ""),
        "masps_val": record.get("masps_val", ""),
        "masps_unit": record.get("masps_unit", ""),
        "mann_bind_lectin_sp2": record.get("mann_bind_lectin_sp2", ""),
        "mann_bind_lectin_sp2_int": record.get("mann_bind_lectin_sp2_int", "")
    }
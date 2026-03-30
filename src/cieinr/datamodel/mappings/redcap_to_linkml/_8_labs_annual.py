def map_cbc_annual(record):
    """
    Map REDCap data for the CBC Annual form to LinkML format.
    """
    return {
        "cbc_type_v2": record.get("cbc_type_v2", ""),
        "cbc_date_v2": record.get("cbc_date_v2", ""),
        "cbc_haemoglobin_v2": record.get("cbc_haemoglobin_v2", ""),
        "cbc_haemoglobin_unit_v2": record.get("cbc_haemoglobin_unit_v2", ""),
        "cbc_haemoglobin_range_v2": record.get("cbc_haemoglobin_range_v2", ""),
        "cbc_haemoglobin_val_v2": record.get("cbc_haemoglobin_val_v2", ""),
        "cbc_platelets_v2": record.get("cbc_platelets_v2", ""),
        "cbc_platelets_unit_v2": record.get("cbc_platelets_unit_v2", ""),
        "cbc_platelets_range_v2": record.get("cbc_platelets_range_v2", ""),
        "cbc_platelets_val_v2": record.get("cbc_platelets_val_v2", ""),
        "cbc_leukocytes_v2": record.get("cbc_leukocytes_v2", ""),
        "cbc_leukocytes_unit_v2": record.get("cbc_leukocytes_unit_v2", ""),
        "cbc_leukocytes_range_v2": record.get("cbc_leukocytes_range_v2", ""),
        "cbc_leukocytes_val_v2": record.get("cbc_leukocytes_val_v2", ""),
        "cbc_neutrophils_v2": record.get("cbc_neutrophils_v2", ""),
        "cbc_neutrophils_unit_v2": record.get("cbc_neutrophils_unit_v2", ""),
        "cbc_neutrophils_range_v2": record.get("cbc_neutrophils_range_v2", ""),
        "cbc_neutrophils_val_v2": record.get("cbc_neutrophils_val_v2", ""),
        "cbc_eosinophils_v2": record.get("cbc_eosinophils_v2", ""),
        "cbc_eosinophils_unit_v2": record.get("cbc_eosinophils_unit_v2", ""),
        "cbc_eosinophils_range_v2": record.get("cbc_eosinophils_range_v2", ""),
        "cbc_eosinophils_val_v2": record.get("cbc_eosinophils_val_v2", ""),
        "cbc_lymphocytes_v2": record.get("cbc_lymphocytes_v2", ""),
        "cbc_lymphocytes_unit_v2": record.get("cbc_lymphocytes_unit_v2", ""),
        "cbc_lymphocytes_range_v2": record.get("cbc_lymphocytes_range_v2", ""),
        "cbc_lymphocytes_val_v2": record.get("cbc_lymphocytes_val_v2", ""),
        "cbc_monocytes_v2": record.get("cbc_monocytes_v2", ""),
        "cbc_monocytes_unit_v2": record.get("cbc_monocytes_unit_v2", ""),
        "cbc_monocytes_range_v2": record.get("cbc_monocytes_range_v2", ""),
        "cbc_monocytes_val_v2": record.get("cbc_monocytes_val_v2", "")
    }
    
def map_lymphopheno_annual(record):
    """
    Map REDCap data for the annual Lymphocyte Phenotype form.
    """
    return {
        "lympheno_test_date_v2": record.get("lympheno_test_date_v2", ""),
        "lympheno_loinc_8122_4_int_v2": record.get("lympheno_loinc_8122_4_int_v2", ""),
        "lympheno_loinc_8122_4_unito_v2": record.get("lympheno_loinc_8122_4_unito_v2", ""),
        "lympheno_loinc_24467_3_int_v2": record.get("lympheno_loinc_24467_3_int_v2", ""),
        "lympheno_loinc_24467_3_val_v2": record.get("lympheno_loinc_24467_3_val_v2", ""),
        "lympheno_loinc_14135_8_int_v2": record.get("lympheno_loinc_14135_8_int_v2", ""),
        "lympheno_loinc_14135_8_val_v2": record.get("lympheno_loinc_14135_8_val_v2", ""),
        "lympheno_loinc_8116_6_int_v2": record.get("lympheno_loinc_8116_6_int_v2", ""),
        "lympheno_loinc_8116_6_val_v2": record.get("lympheno_loinc_8116_6_val_v2", ""),
        "lympheno_loinc_9558_8_int_v2": record.get("lympheno_loinc_9558_8_int_v2", ""),
        "lympheno_loinc_9558_8_val_v2": record.get("lympheno_loinc_9558_8_val_v2", ""),
        "lympheno_loinc_9728_7_int_v2": record.get("lympheno_loinc_9728_7_int_v2", ""),
        "lympheno_loinc_9728_7_val_v2": record.get("lympheno_loinc_9728_7_val_v2", ""),
        "lymphopheno_other_v2": record.get("lymphopheno_other_v2", ""),
        "lymphopheno_test_v2": record.get("lymphopheno_test_v2", "")
    }
    
    
def map_lymphocytes_phenotype_annual(record):
    """
    Map REDCap data for the annual Lymphocyte Phenotype form to the LinkML format.
    
    Field names and branching logic have been updated with the _v2 suffix.
    
    Args:
        record (dict): The REDCap record data.
        
    Returns:
        dict: The mapped data in LinkML format.
    """
    return {
        "lympheno_test_v2": record.get("lympheno_test_v2", ""),
        "lympheno_test_date_v2": record.get("lympheno_test_date_v2", ""),
        "lympheno_loinc_8122_4_v2": record.get("lympheno_loinc_8122_4_v2", ""),
        "lympheno_loinc_8122_4_unit_v2": record.get("lympheno_loinc_8122_4_unit_v2", ""),
        "lympheno_loinc_8122_4_unito_v2": record.get("lympheno_loinc_8122_4_unito_v2", ""),
        "lympheno_loinc_8122_4_val_v2": record.get("lympheno_loinc_8122_4_val_v2", ""),
        "lympheno_loinc_8122_4_int_v2": record.get("lympheno_loinc_8122_4_int_v2", ""),
        "lympheno_loinc_24467_3_v2": record.get("lympheno_loinc_24467_3_v2", ""),
        "lympheno_loinc_24467_3_unit_v2": record.get("lympheno_loinc_24467_3_unit_v2", ""),
        "lympheno_loinc_24467_3_unito_v2": record.get("lympheno_loinc_24467_3_unito_v2", ""),
        "lympheno_loinc_24467_3_val_v2": record.get("lympheno_loinc_24467_3_val_v2", ""),
        "lympheno_loinc_24467_3_int_v2": record.get("lympheno_loinc_24467_3_int_v2", ""),
        "lympheno_loinc_14135_8_v2": record.get("lympheno_loinc_14135_8_v2", ""),
        "lympheno_loinc_14135_8_unit_v2": record.get("lympheno_loinc_14135_8_unit_v2", ""),
        "lympheno_loinc_14135_8_unito_v2": record.get("lympheno_loinc_14135_8_unito_v2", ""),
        "lympheno_loinc_14135_8_val_v2": record.get("lympheno_loinc_14135_8_val_v2", ""),
        "lympheno_loinc_14135_8_int_v2": record.get("lympheno_loinc_14135_8_int_v2", ""),
        "lympheno_loinc_8116_6_v2": record.get("lympheno_loinc_8116_6_v2", ""),
        "lympheno_loinc_8116_6_unit_v2": record.get("lympheno_loinc_8116_6_unit_v2", ""),
        "lympheno_loinc_8116_6_unito_v2": record.get("lympheno_loinc_8116_6_unito_v2", ""),
        "lympheno_loinc_8116_6_val_v2": record.get("lympheno_loinc_8116_6_val_v2", ""),
        "lympheno_loinc_8116_6_int_v2": record.get("lympheno_loinc_8116_6_int_v2", ""),
        "lympheno_loinc_9558_8_v2": record.get("lympheno_loinc_9558_8_v2", ""),
        "lympheno_loinc_9558_8_unit_v2": record.get("lympheno_loinc_9558_8_unit_v2", ""),
        "lympheno_loinc_9558_8_unito_v2": record.get("lympheno_loinc_9558_8_unito_v2", ""),
        "lympheno_loinc_9558_8_val_v2": record.get("lympheno_loinc_9558_8_val_v2", ""),
        "lympheno_loinc_9558_8_int_v2": record.get("lympheno_loinc_9558_8_int_v2", ""),
        "lympheno_loinc_9728_7_v2": record.get("lympheno_loinc_9728_7_v2", ""),
        "lympheno_loinc_9728_7_unit_v2": record.get("lympheno_loinc_9728_7_unit_v2", ""),
        "lympheno_loinc_9728_7_unito_v2": record.get("lympheno_loinc_9728_7_unito_v2", ""),
        "lympheno_loinc_9728_7_val_v2": record.get("lympheno_loinc_9728_7_val_v2", ""),
        "lympheno_loinc_9728_7_int_v2": record.get("lympheno_loinc_9728_7_int_v2", ""),
        "lymphopheno_other_v2": record.get("lymphopheno_other_v2", ""),
        "lymphopheno_test_v2": record.get("lymphopheno_test_v2", "")
    }
    
def map_phagocyte_function_annual(record):
    """
    Map REDCap data for the annual Phagocyte Function form.
    """
    return {
        "phagocyte_test_date_v2": record.get("phagocyte_test_date_v2", ""),
        "neutrophil_test_v2": record.get("neutrophil_test_v2", ""),
        "other_test_v2": record.get("other_test_v2", ""),
        "nph_test_result_v2": record.get("nph_test_result_v2", ""),
        "nph_test_results_v2": record.get("nph_test_results_v2", ""),
        "flow_adhesion_val_v2": record.get("flow_adhesion_val_v2", ""),
        "please_upload_flow_cytomet_v2": record.get("please_upload_flow_cytomet_v2", "")
    }
    
def map_autoantibodies_annual(record):
    """
    Map REDCap data for the Autoantibodies Annual form to LinkML format.
    """
    return {
        "autoantibodies_test_date_v2": record.get("autoantibodies_test_date_v2", ""),
        "autoanti_ana_val_v2": record.get("autoanti_ana_val_v2", ""),
        "autoanti_anca_val_v2": record.get("autoanti_anca_val_v2", ""),
        "autoanti_ena_val_v2": record.get("autoanti_ena_val_v2", ""),
        "autoanti_anti_tpo_val_v2": record.get("autoanti_anti_tpo_val_v2", ""),
        "autoanti_anti_neu_val_v2": record.get("autoanti_anti_neu_val_v2", ""),
        "autoanti_anti_plat_val_v2": record.get("autoanti_anti_plat_val_v2", ""),
        "autoanti_iga_ttg_val_v2": record.get("autoanti_iga_ttg_val_v2", ""),
        "autoanti_dat_val_v2": record.get("autoanti_dat_val_v2", ""),
        "other_autoanti_test_v2": record.get("other_autoanti_test_v2", ""),
        "other_autoanti_val_v2": record.get("other_autoanti_val_v2", "")
    }
    
def map_immunoglobulin_annual(record):
    """
    Map REDCap data for the Immunoglobulin Annual form to LinkML format.
    """
    return {
        "immmunglobulin_test_date_v2": record.get("immmunglobulin_test_date_v2", ""),
        "igrt_2": record.get("igrt_2", ""),
        "immmunglobulin_igg_int_v2": record.get("immmunglobulin_igg_int_v2", ""),
        "immmunglobulin_igg_val_v2": record.get("immmunglobulin_igg_val_v2", ""),
        "immmunglobulin_iga_int_v2": record.get("immmunglobulin_iga_int_v2", ""),
        "immmunglobulin_iga_val_v2": record.get("immmunglobulin_iga_val_v2", ""),
        "immmunglobulin_igm_int_v2": record.get("immmunglobulin_igm_int_v2", ""),
        "immmunglobulin_igm_val_v2": record.get("immmunglobulin_igm_val_v2", ""),
        "immmunglobulin_ige_int_v2": record.get("immmunglobulin_ige_int_v2", ""),
        "immmunglobulin_ige_val_v2": record.get("immmunglobulin_ige_val_v2", ""),
        "immmunglobulin_iga_v2": record.get("immmunglobulin_iga_v2", ""),
        "immmunglobulin_igm_v2": record.get("immmunglobulin_igm_v2", ""),
        "immmunglobulin_igg_v2": record.get("immmunglobulin_igg_v2", ""),
        "immmunglobulin_ige_v2": record.get("immmunglobulin_ige_v2", "")
    }
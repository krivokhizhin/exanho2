from . import agency_relation as agency_relation_ms_mod
from . import reference as reference_ds_mod

def match_builder(filename:str):
    if filename.lower().startswith('nsiOkato_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkato_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkdp_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkdp_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkei_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkei_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkfs_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkfs_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkogu_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkogu_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkopf_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkopf_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkpd2_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkpd2_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOktmo_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOktmo_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkv_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkv_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkved_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkved_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkved2_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOkved2_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOrganization_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiOrganization_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiPurchaseMethod_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiPurchaseMethod_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiClauseType_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiClauseType_inc_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiProtocol_all_'.lower()):
        return reference_ds_mod.parseString
    
    if filename.lower().startswith('nsiProtocol_inc_'.lower()):
        return reference_ds_mod.parseString

    
    if filename.lower().startswith('agencyRelations_all_'.lower()):
        return agency_relation_ms_mod.parseString
    
    if filename.lower().startswith('agencyRelations_inc_'.lower()):
        return agency_relation_ms_mod.parseString   
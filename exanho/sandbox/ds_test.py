def run():

    import exanho.orm.domain as domain
    d = domain.Domain('postgresql+psycopg2://kks:Nata1311@localhost/eis44_test')

    # ds_mod = importlib.import_module('exanho.eis223.ds.reference')
    import exanho.eis44.ds.export_types as ds_mod
    f = open('/home/kks/projects/eis44DS/contracts/contract_Adygeja_Resp_2020110100_2020120100_002.xml/contract_1010200198019000007_61198985.xml', 'br')
    f_str = f.read()
    rootObj = ds_mod.parseString(f_str)
    
    from exanho.eis44.parsing.integration_types.zfcs_contract2015 import parse as ds_parse

    for child in rootObj.get_children():
        with d.session_scope() as session:
            ds_parse(session, child, False)
            print(child.get_xml_tag())
            pass

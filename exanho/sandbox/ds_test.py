def run():

    import exanho.orm.domain as domain
    d = domain.Domain('postgresql+psycopg2://kks:Nata1311@localhost/eis44_test')

    import exanho.eis44.ds.contracts.fcsExport as ds_mod
    f = open('/home/kks/projects/eis44DS/data/contracts/contract_Adygeja_Resp_2019080100_2019090100_001.xml/contract_1010504482319000005_51306396.xml', 'br')
    f_str = f.read()
    rootObj = ds_mod.parseString(f_str)
    
    from exanho.eis44.parsing.integration_types.zfcs_contract2015 import parse as ds_parse

    for child in rootObj.get_children():
        with d.session_scope() as session:
            ds_parse(session, child, True)
            print(child.get_xml_tag())
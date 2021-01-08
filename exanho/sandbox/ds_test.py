def run():
    import xmlschema
    # schema_file = open('/home/kks/projects/eis44DS/xsd/11.0.4/fcsExport_contract.xsd')
    schema = xmlschema.XMLSchema('/home/kks/projects/eis44DS/xsd/11.0.4/fcsExport_contract.xsd')
    schema.export('/home/kks/projects/eis44DS/gen', only_relative=False)

    for xsd_component in schema.iter_components():
        xsd_component

    for key, import_schema in schema.imports.items():

        for xsd_component in import_schema.iter_components():
            xsd_component

        for inner_key, import_inner_schema in import_schema.imports.items():

            for xsd_component in import_inner_schema.iter_components():
                xsd_component




    # import exanho.orm.domain as domain
    # d = domain.Domain('postgresql+psycopg2://kks:Nata1311@localhost/eis44_test')

    # # ds_mod = importlib.import_module('exanho.eis223.ds.reference')
    # import exanho.eis44.ds.export_types as ds_mod
    # f = open('/home/kks/projects/eis44DS/contracts/contract_Adygeja_Resp_2020110100_2020120100_002.xml/contract_1010100225119000004_61063483.xml', 'br')
    # f_str = f.read()
    # rootObj = ds_mod.parseString(f_str)
    
    # from exanho.eis44.parsing.integration_types.zfcs_contract2015 import parse as ds_parse

    # for child in rootObj.get_children():
    #     with d.session_scope() as session:
    #         ds_parse(session, child, False)
    #         print(child.get_xml_tag())
    #         pass

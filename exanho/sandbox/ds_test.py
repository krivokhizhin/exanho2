def run():

    import exanho.orm.domain as domain
    d = domain.Domain('postgresql+psycopg2://kks:Nata1311@localhost/eis223_test')

    # ds_mod = importlib.import_module('exanho.eis223.ds.reference')
    import exanho.eis223.ds.reference as ds_mod
    f = open('/home/kks/projects/eis223DS/nsiClauseType/nsiClauseType_all_20201129_020917_001.xml', 'br')
    # f = open('/home/kks/projects/eis223DS/nsiPurchaseMethod/nsiPurchaseMethod_all_20201129_012618_001.xml/nsiPurchaseMethod_all_20201129_012618_001.xml', 'br')
    # f = open('/home/kks/projects/eis223DS/nsiProtocol/nsiProtocol_all_20201129_020243_001.xml/nsiProtocol_all_20201129_020243_001.xml', 'br')
    f_str = f.read()
    rootObj = ds_mod.parseString(f_str)

    from exanho.eis223.parsing.reference.nsi_order_clause import parse as ds_parse
    # from exanho.eis223.parsing.reference.nsi_purchase_method import parse as ds_parse
    # from exanho.eis223.parsing.reference.nsi_protocol import parse as ds_parse
    with d.session_scope() as session:
        ds_parse(session, rootObj, False)
import importlib
from lxml import etree

def run():

    import exanho.orm.domain as domain
    d = domain.Domain('postgresql+psycopg2://kks:Nata1311@localhost/eis223_test')

    # ds_mod = importlib.import_module('exanho.eis223.ds.reference')
    import exanho.eis223.ds.reference as ds_mod
    f = open('/home/kks/projects/eis223DS/nsiOkv_all_20201108_021309_001.xml', 'br')
    f_str = f.read()
    rootObj = ds_mod.parseString(f_str)

    from exanho.eis223.parsing.reference.nsi_okv import parse as ds_parse
    with d.session_scope() as session:
        ds_parse(session, rootObj, False)

    # print(rootObj.gds_elementtree_node_)
    # if type(rootObj.gds_elementtree_node_) == etree._Element:
    #     tag = rootObj.gds_elementtree_node_.tag
    #     print(tag)

    # print(rootObj.get_xml_tag())
    # print(rootObj)

    # for item in rootObj.body.item:
    #     print(item.nsiOkvData.guid)
    #     print(item.nsiOkvData.changeDateTime)
    #     print(item.nsiOkvData.startDateActive)
    #     print(item.nsiOkvData.endDateActive)
    #     print(item.nsiOkvData.businessStatus)
    #     print(item.nsiOkvData.code)
    #     print(item.nsiOkvData.digitalCode)
    #     print(item.nsiOkvData.name)
    #     print(item.nsiOkvData.shortName)
    #     print()

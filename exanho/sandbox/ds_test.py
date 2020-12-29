
# def get_children(self):
#     for child_name in self.__class__.member_data_items_.keys():
#         if not hasattr(self, child_name):
#             continue

#         child_attr = getattr(self, child_name)
#         if child_attr is None or not child_attr:
#             continue

#         try:
#             for child in iter(child_attr):
#                 yield child
#         except TypeError:
#             yield child_attr

# def get_xml_tag(self):
#     return self.gds_elementtree_node_.tag

def run():

    import exanho.orm.domain as domain
    d = domain.Domain('postgresql+psycopg2://kks:Nata1311@localhost/eis223_test')

    # ds_mod = importlib.import_module('exanho.eis223.ds.reference')
    import exanho.eis44.ds.contract as ds_mod
    f = open('/home/kks/projects/eis44DS/contract_0176100000714000001_13354543.xml', 'br')
    f_str = f.read()
    rootObj = ds_mod.parseString(f_str)

    for child in rootObj.get_children():
        print(child.get_xml_tag())

    # from exanho.eis223.parsing.customer_registry.nsi_customer import parse as ds_parse
    # with d.session_scope() as session:
    #     ds_parse(session, rootObj, False)
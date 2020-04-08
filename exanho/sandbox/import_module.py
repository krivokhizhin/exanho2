import importlib

# from abc import ABCMeta
# from exanho.core.actors import ServiceBase


module_path = 'exanho.services.nsi.organization_type' # 'exanho.workers.loading' # 'exanho.orm.sqlalchemy'
url = 'postgresql+psycopg2://kks:Nata1311@localhost/eis44'


def run():
    mod = importlib.import_module(module_path)

    # hosting_service = None   
    # for service_name, service_class in vars(mod).items():
    #     if ((type(service_class) == type or type(service_class) == ABCMeta)
    #     and issubclass(service_class, ServiceBase)
    #     and service_name != ServiceBase.__name__):
    #         hosting_service = service_class

    # print(hosting_service)

    # service = hosting_service()
    # print(service.put('Dd', 'ddddd'))

    mod.domain.configure(url)
    # print(mod.domain.validate(url))
    mod.domain.recreate(url)
    print('complete')
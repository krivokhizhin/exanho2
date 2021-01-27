import importlib

from exanho.orm.domain import Domain, Sessional
from exanho.core.manager_context import Context as ExanhoContext


module_path = 'exanho.eis44.workers.log_parser' # 'exanho.services.nsi.organization_type' # 'exanho.orm.domain'
url = 'postgresql+psycopg2://kks:Nata1311@localhost/eis44_test'


def run():
    Sessional.domain = Domain(url)
    appsettings = {'log_parser': 'exanho.eis44.log_parsers.participant'}
    mod = importlib.import_module(module_path)
    print(mod.__name__)

    context = mod.initialize(appsettings, ExanhoContext(object()))
    context = mod.work(context)
    mod.finalize(context)

    # hosting_service = None   
    # for service_name, service_class in vars(mod).items():
    #     if ((type(service_class) == type or type(service_class) == ABCMeta)
    #     and issubclass(service_class, ServiceBase)
    #     and service_name != ServiceBase.__name__):
    #         hosting_service = service_class

    # print(hosting_service)

    # service = hosting_service()
    # print(service.put('Dd', 'ddddd'))

    # mod.domain.configure(url)
    # print(mod.domain.validate(url))
    # mod.domain.recreate(url)
    print('complete')
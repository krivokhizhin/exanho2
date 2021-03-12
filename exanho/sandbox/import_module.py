import importlib

from exanho.orm.domain import Domain, Sessional
from exanho.core.manager_context import Context as ExanhoContext


module_path = 'exanho.eis44.upgrade.add_ensuring' # 'exanho.services.nsi.organization_type' # 'exanho.orm.domain'
url = 'postgresql+psycopg2://kks:Nata1311@localhost/eis44_test'


def run():
    Sessional.domain = Domain(url)
    appsettings = {
        'min_doc_id': 0, 'max_doc_id': 212430,
        'docs': [32055, 34804, 35448, 39183, 39188, 39187, 42741, 43546, 43642, 46713, 43097, 46964, 42744, 219631, 221646, 228854, 229086, 230016, 230384, 230890, 214738, 215075, 217545, 220519, 221047, 221664, 222143, 225208, 219151, 222221, 222525, 225206, 219152, 222219, 225207, 225374, 218948, 222163, 224845, 225014, 225204, 227118, 225057, 226323, 221960, 43362, 33208, 94989, 32997, 31542, 40644, 29412, 29575, 216550, 218679]
    }
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
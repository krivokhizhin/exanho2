import importlib
from multiprocessing import Process, Queue

from ..domain import Domain

def validate_db(worker_cfg, res_queue):
    for module_name in worker_cfg.modules:
        importlib.import_module(module_name)

    domain = Domain()
    domain.initialize(worker_cfg.db_url)
    res_queue.put(domain.validate())

def check_db_schema(worker_cfg):

    res_queue = Queue()
    validate_process = Process(target=validate_db, args=(worker_cfg, res_queue))
    validate_process.daemon = True
    validate_process.start()

    result = res_queue.get()
    validate_process.join()
    return result
from . import *

def create(config, log_queue):
    if config.kind == 'RpcServer':
        return RpcServer(config, log_queue)

    raise Exception(f'No action found for the specified type ({config.kind}).') 

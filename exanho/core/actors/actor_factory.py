from . import XmlRpcServer, SleepWorker, QueueWorker

def create(config, context):

    if config.kind == 'XmlRpcServer':
        return XmlRpcServer(config, context)

    if config.kind == 'SleepWorker':
        return SleepWorker(config, context)

    if config.kind == 'QueueWorker':
        return QueueWorker(config, context)

    raise Exception(f'No action found for the specified type ({config.kind}).') 

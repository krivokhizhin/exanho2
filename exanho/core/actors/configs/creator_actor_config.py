from . import RpcServerActorConfig, XmlRpcServerActorConfig, SleepWorkerActorConfig, QueueWorkerActorConfig

def create_actor_config(config: dict):
    if config['kind'].lower() == 'RpcServer'.lower():
        return RpcServerActorConfig.create_instance(config)

    if config['kind'].lower() == 'XmlRpcServer'.lower():
        return XmlRpcServerActorConfig.create_instance(config)

    if config['kind'].lower() == 'SleepWorker'.lower():
        return SleepWorkerActorConfig.create_instance(config)

    if config['kind'].lower() == 'QueueWorker'.lower():
        return QueueWorkerActorConfig.create_instance(config)
    
    raise Exception('Unknown type of actor configuration: {}.'.format(config.kind))
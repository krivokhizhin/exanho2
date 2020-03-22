from . import RpcServerActorConfig

def create_actor_config(config):
    if config.kind.lower() == 'RpcServer'.lower():
        return RpcServerActorConfig.create_instance(config)
    
    raise Exception('Unknown type of unit configuration: {}.'.format(config.kind)) 
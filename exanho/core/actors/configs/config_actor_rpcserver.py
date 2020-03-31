from . import ActorConfig, ListConfigBaseDerived, RpcService

class RpcServerActorConfig(ActorConfig):
    services = ListConfigBaseDerived(RpcService)
from . import ActorConfig, ListConfigBaseDerived, Service

class RpcServerActorConfig(ActorConfig):
    services = ListConfigBaseDerived(Service)
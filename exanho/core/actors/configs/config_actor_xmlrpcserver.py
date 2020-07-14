from . import ActorConfig, ListConfigBaseDerived, XmlRpcService

class XmlRpcServerActorConfig(ActorConfig):
    services = ListConfigBaseDerived(XmlRpcService)
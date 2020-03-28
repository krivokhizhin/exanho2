from ...common.descriptors import String
from . import ActorConfig, ReadOnlyConfigBaseDerived, TCPaddress, Concurrency

class RpcServerActorConfig(ActorConfig):
    address = ReadOnlyConfigBaseDerived(TCPaddress)
    concurrency = ReadOnlyConfigBaseDerived(Concurrency)
    handler_module = String()
from .common.descriptors import Boolean, Integer, String, List
from .actors.configs import ConfigBase, ActorConfig, ConfigBaseDerived, ListConfigBaseDerived

class ConnectingConfig(ConfigBase):
    name = String('default')
    url = String()
    models = List()

class QueueConfig(ConfigBase):
    name = String()
    maxsize = Integer(-1)

class EndpointConfig(ConfigBase):
    interface = String()
    host = String()
    port = Integer()

class ContextConfig(ConfigBase):
    db_connectings = ListConfigBaseDerived(ConnectingConfig)
    joinable_queues = ListConfigBaseDerived(QueueConfig)
    service_endpoints = ListConfigBaseDerived(EndpointConfig)

class ExanhoConfig(ConfigBase):
    context = ConfigBaseDerived(ContextConfig)
    actors = ListConfigBaseDerived(ActorConfig)
from .common.descriptors import Boolean, Integer, String
from .actors.configs import ConfigBase, ActorConfig, ConfigBaseDerived, ListConfigBaseDerived

class ConnectingConfig(ConfigBase):
    name = String('default')
    url = String()

class QueueConfig(ConfigBase):
    name = String()
    maxsize = Integer(-1)

class ContextConfig(ConfigBase):
    db_connectings = ListConfigBaseDerived(ConnectingConfig)
    joinable_queues = ListConfigBaseDerived(QueueConfig)

class ExanhoConfig(ConfigBase):
    context = ConfigBaseDerived(ContextConfig)
    actors = ListConfigBaseDerived(ActorConfig)
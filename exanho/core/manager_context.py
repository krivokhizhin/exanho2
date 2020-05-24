from .common.descriptors import Boolean, Integer, String
from .actors.configs import ConfigBase,ListConfigBaseDerived

class QueueConfig(ConfigBase):
    name = String()
    maxsize = Integer(-1)

class ContextConfig(ConfigBase):
    joinable_queues = ListConfigBaseDerived(QueueConfig)
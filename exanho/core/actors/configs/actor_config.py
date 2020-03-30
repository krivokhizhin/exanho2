from ...common.descriptors import Boolean, Integer, String
from . import ConfigBase

class ActorConfig(ConfigBase):
    name = String()
    kind = String()
    daemon = Boolean()
from ...common.descriptors import Integer, String
from . import ConfigBase

class ActorConfig(ConfigBase):
    name = String()
    kind = String()
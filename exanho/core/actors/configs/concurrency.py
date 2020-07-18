from ...common.descriptors import Boolean, Integer, String
from . import ConfigBase

class Concurrency(ConfigBase):
    degree = Integer(0)
    kind = String('thread')
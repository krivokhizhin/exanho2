from ...common.descriptors import Boolean, Integer, String
from . import ConfigBase

class Concurrency(ConfigBase):
    degree = Integer(1)
    kind = String('thread')
    daemon = Boolean(True)
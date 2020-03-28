from ...common.descriptors import Integer, String
from . import ConfigBase

class Concurrency(ConfigBase):
    degree = Integer()
    kind = String()
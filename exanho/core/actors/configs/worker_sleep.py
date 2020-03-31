from ...common.descriptors import Integer, String
from . import ConfigBase

class SleepWorker(ConfigBase):
    module = String()
    sleep = Integer()
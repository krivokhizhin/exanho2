from ...common.descriptors import Integer, Float, String
from . import ConfigBase, ConfigBaseDerived, List, Concurrency

class SleepWorker(ConfigBase):
    module = String()
    sleep = Float()
    factor_thread = Integer(1)
    appsettings = ConfigBaseDerived(List)
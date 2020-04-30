from ...common.descriptors import Float, String
from . import ConfigBase, ConfigBaseDerived, List, Concurrency

class SleepWorker(ConfigBase):
    module = String()
    sleep = Float()
    concurrency = ConfigBaseDerived(Concurrency)
    appsettings = ConfigBaseDerived(List)
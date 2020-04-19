from ...common.descriptors import Float, String
from . import ConfigBase, ConfigBaseDerived, List

class SleepWorker(ConfigBase):
    module = String()
    sleep = Float()
    appsettings = ConfigBaseDerived(List)
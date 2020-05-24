from ...common.descriptors import Integer, String
from . import ConfigBase, ConfigBaseDerived, List

class WorkerConfig(ConfigBase):
    module = String()
    factor_thread = Integer(1)
    appsettings = ConfigBaseDerived(List)
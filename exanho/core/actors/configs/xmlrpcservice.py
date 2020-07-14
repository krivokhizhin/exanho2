from ...common.descriptors import String
from . import ConfigBase, ConfigBaseDerived, Concurrency

class XmlRpcService(ConfigBase):
    handler_module = String()
    interface = String()
    concurrency = ConfigBaseDerived(Concurrency)
    db_key = String()
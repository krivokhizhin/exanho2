from ...common.descriptors import Integer, String
from . import ConfigBase, ConfigBaseDerived, TCPaddress, Concurrency

class Service(ConfigBase):
    handler_module = String()
    address = ConfigBaseDerived(TCPaddress)
    concurrency = ConfigBaseDerived(Concurrency)
from ...common.descriptors import Integer, String
from . import ConfigBase, ConfigBaseDerived, TCPaddress, Concurrency

class RpcService(ConfigBase):
    handler_module = String()
    address = ConfigBaseDerived(TCPaddress)
    secret_key = String()
    concurrency = ConfigBaseDerived(Concurrency)
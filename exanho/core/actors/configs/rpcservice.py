from ...common.descriptors import Integer, String
from . import ConfigBase, ConfigBaseDerived, TCPaddress, Concurrency, DbDomain

class RpcService(ConfigBase):
    handler_module = String()
    address = ConfigBaseDerived(TCPaddress)
    secret_key = String()
    concurrency = ConfigBaseDerived(Concurrency)
    db_domain = ConfigBaseDerived(DbDomain)
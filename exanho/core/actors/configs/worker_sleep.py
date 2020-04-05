from ...common.descriptors import Float, String
from . import ConfigBase, ConfigBaseDerived, DbDomain

class SleepWorker(ConfigBase):
    module = String()
    sleep = Float()
    db_domain = ConfigBaseDerived(DbDomain)
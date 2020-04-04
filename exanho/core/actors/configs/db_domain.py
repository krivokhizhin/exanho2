from ...common.descriptors import Boolean, String
from . import ConfigBase

class DbDomain(ConfigBase):
    module = String()
    url = String()
    validate = Boolean(False)
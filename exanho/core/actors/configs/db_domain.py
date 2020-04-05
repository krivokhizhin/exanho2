from ...common.descriptors import Boolean, String
from . import ConfigBase

class DbDomain(ConfigBase):
    url = String()
    validate = Boolean(False)
from ...common.descriptors import Integer, String
from . import ConfigBase

class TCPaddress(ConfigBase):
    host = String()
    port = Integer()
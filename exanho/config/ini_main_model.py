from ..common import Sctructure

class AppCfg(Sctructure):
    _fields = ['host', 'port', 'units_config', 'logging_pub_bind', 'logging_maxsize', 'logging_config']
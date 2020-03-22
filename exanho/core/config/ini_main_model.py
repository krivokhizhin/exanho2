from ..common import Sctructure

class AppCfg(Sctructure):
    _fields = ['host', 'port', 'actors_config_path', 'logging_pub_bind', 'logging_maxsize', 'logging_config']
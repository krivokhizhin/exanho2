from ..common import Structure

class AppCfg(Structure):
    _fields = ['host', 'port', 'actors_config_path', 'secret_key', 'logging_pub_bind', 'logging_maxsize', 'logging_config']
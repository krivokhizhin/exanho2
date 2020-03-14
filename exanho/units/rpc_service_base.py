from ..common import ExitException
from .rpc_handler import RPCHandler

class ServiceBase(RPCHandler):
    
    def call_exit(self):
        raise ExitException()
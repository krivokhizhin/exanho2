from ..common import ExitException
from .rpc_handler import RPCHandler

class ServiceBase(RPCHandler):

    def validate(self):
        return True
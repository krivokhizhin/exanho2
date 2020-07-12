from .rpc_handler import RpcHandler

class ServiceBase(RpcHandler):
    secret_key = None
    context = None

    def validate(self):
        return True
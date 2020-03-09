from socketserver import BaseRequestHandler

from ..contract import rpc_utilities as util

class RPCHandler(BaseRequestHandler):
    
    def handle(self):
        func_name, args, kwargs = util.receive_rpc_data(self.request)
        try:
            result = getattr(self, func_name)(*args,**kwargs)
            util.send_rpc_data(self.request, result)
        except Exception as e:
            util.send_rpc_data(self.request, str(e))
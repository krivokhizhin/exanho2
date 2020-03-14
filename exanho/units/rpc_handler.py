import logging

from socketserver import BaseRequestHandler

from ..common import ExitException
from ..contract import rpc_utilities as util

class RPCHandler(BaseRequestHandler):
    
    def handle(self):
        try:
            func_name, args, kwargs = util.receive_rpc_data(self.request)
            result = getattr(self, func_name)(*args,**kwargs)            
            util.send_rpc_data(self.request, result)
        except ExitException:
            util.send_rpc_data(self.request, 'OK')
            self.server.shutdown()
        except Exception as ex:
            util.send_rpc_data(self.request, ex.args)
            raise        
import logging
from socketserver import BaseRequestHandler

from ..common import rpc_utilities as util
from ..common.authenticate import server_authenticate


class RpcHandler(BaseRequestHandler):
    
    def handle(self):
        try:
            if self.secret_key and not server_authenticate(self.request, self.secret_key):
                self.request.close()
                logging.getLogger(self.__class__.__name__).warning(f'{self.client_address}: identification error')
                return
            args, kwargs = util.receive_rpc_data(self.request)
            func_name, *args = args
            result = getattr(self, func_name)(*args,**kwargs)            
            util.send_rpc_data(self.request, result)
        except Exception as ex:
            util.send_rpc_data(self.request, ex.args)
            raise        

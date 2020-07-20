import logging
import time
from xmlrpc.client import ServerProxy

from exanho.core.common import try_logged, Timer
from exanho.core.actors import ServiceBase
from exanho.interfaces import ISampleService

class SampleService(ISampleService, ServiceBase):

    logger = logging.getLogger(__name__)

    @try_logged
    def echo(self, *args, **kwargs):
        return 'echo', args, kwargs

    @try_logged
    def load(self, load = 10000000):
        timer = Timer()
        with timer:
            n = int(load)
            i = j = k = 0
            while i < n:
                while j < n:
                    while k < n:
                        k += 1
                    j += 1
                i += 1
        return 'load', timer.elapsed

    @try_logged
    def raise_ex(self, message = 'raise Exception'):
        raise Exception(message)
    
    # @try_logged
    # def execute(self, task):
    #     self.logger.debug(f'{task} START')
    #     host, port = SampleService.context.get_service_endpoint(ISampleService2)
    #     rpc_paths = '/'

    #     if host and port:
    #         client = ServerProxy(f'http://{host}:{port}{rpc_paths}', allow_none=True, use_builtin_types=True)
    #         client.echo(task)
    #     self.logger.debug(f'{task} FINISH')

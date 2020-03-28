import importlib
import logging

from abc import ABCMeta
from socketserver import TCPServer

from . import Actor, ServiceBase
from .configs import RpcServerActorConfig

JOIN_TIMEOUT = 1

class RpcServer(Actor):

    def run(self, config: RpcServerActorConfig):
        log = logging.getLogger(__name__)

        mod = importlib.import_module(config.handler_module)
        for service_name, service_class in vars(mod).items():
            if ((type(service_class) == type or type(service_class) == ABCMeta)
            and issubclass(service_class, ServiceBase)
            and service_name != ServiceBase.__name__):
                self.service_class = service_class
                    
        if not self.service_class:
            raise Exception('{}: No services'.format(config.name))

        TCPServer.allow_reuse_address = True
        self.serv = TCPServer((config.address.host, config.address.port), self.service_class)
        self.serv.handle_error = self._handle_error

        self.handlers = []

        log.info(f'The actor "{config.name}" has been initialized.')

        if config.concurrency.degree > 0:
            if config.concurrency.kind == 'process':
                from multiprocessing import Process
                for n in range(config.concurrency.degree):
                    p = Process(target=self.serv.serve_forever, name=f'Process#{n}')
                    p.daemon = True
                    p.start()
                    self.handlers.append(p)
            elif config.concurrency.kind == 'thread':
                from threading import Thread
                for n in range(config.concurrency.degree):
                    t = Thread(target=self.serv.serve_forever, name=f'Thread#{n}')
                    t.daemon = True
                    t.start()
                    self.handlers.append(t)
            else:
                raise Exception(f'The concurrency_type is "{config.concurrency.kind}". There must be either "Thread" or "Process".')

        log.info(f'The actor "{config.name}" has been started.')

    def finalize(self):
        log = logging.getLogger(RpcServer.__module__)
        self.serv.shutdown()
        self.serv.server_close()
        for handler in self.handlers:
            handler.join(JOIN_TIMEOUT)
            if handler.is_alive():
                log.warning(f'The {handler.name} was not completed in the allotted time interval ({JOIN_TIMEOUT} sec.).')            

    def handle(msg):
        pass

    def _handle_error(self, request, client_address):
        log = logging.getLogger(RpcServer.__module__)
        log.error(f'An exception occurred while processing the request from the address: {client_address}')
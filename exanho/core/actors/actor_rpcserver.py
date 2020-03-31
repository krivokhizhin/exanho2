import importlib
import logging

from abc import ABCMeta
from collections import defaultdict
from socketserver import TCPServer

from . import Actor, ServiceBase

JOIN_TIMEOUT = 1

class RpcServer(Actor):

    def run(self):
        log = logging.getLogger(__name__)

        self.handlers = defaultdict(list)

        for service_config in self.config.services:

            hosting_service = None
            mod = importlib.import_module(service_config.handler_module)            
            for service_name, service_class in vars(mod).items():
                if ((type(service_class) == type or type(service_class) == ABCMeta)
                and issubclass(service_class, ServiceBase)
                and service_name != ServiceBase.__name__):
                    hosting_service = service_class
                        
            if not hosting_service:
                raise Exception('{}: No services'.format(self.config.name))

            if service_config.secret_key:
                hosting_service.secret_key = service_config.secret_key.encode('utf-8')

            TCPServer.allow_reuse_address = True
            self.serv = TCPServer((service_config.address.host, service_config.address.port), hosting_service)
            self.serv.handle_error = self._handle_error

            log.info(f'The actor "{self.config.name}": service "{hosting_service.__name__}" has been initialized.')

            if service_config.concurrency.degree > 0:
                if service_config.concurrency.kind == 'process':
                    from multiprocessing import Process
                    for n in range(service_config.concurrency.degree):
                        p = Process(target=self.serv.serve_forever, name=f'Process#{n}')
                        p.daemon = True
                        p.start()
                        self.handlers[hosting_service.__name__].append(p)
                elif service_config.concurrency.kind == 'thread':
                    from threading import Thread
                    for n in range(service_config.concurrency.degree):
                        t = Thread(target=self.serv.serve_forever, name=f'Thread#{n}')
                        t.daemon = True
                        t.start()
                        self.handlers[hosting_service.__name__].append(t)
                else:
                    raise Exception(f'The concurrency_type is "{service_config.concurrency.kind}". There must be either "Thread" or "Process".')

            log.info(f'The actor "{self.config.name}": "{hosting_service.__name__}" has been started.')

        log.info(f'The actor "{self.config.name}" has been installed.')

    def finalize(self):
        log = logging.getLogger(RpcServer.__module__)
        # self.serv.shutdown()
        self.serv.server_close()

        # for service_name, handlers in self.handlers.items():
        #     for handler in handlers:
        #         handler.join(JOIN_TIMEOUT)
        #         if handler.is_alive():
        #             log.warning(f'The {handler.name} was not completed in the allotted time interval ({JOIN_TIMEOUT} sec.).')  
        #         log.info(f'The service "{service_name}" has been stopped.')          

    def handle(msg):
        pass

    def _handle_error(self, request, client_address):
        log = logging.getLogger(RpcServer.__module__)
        log.error(f'An exception occurred while processing the request from the address: {client_address}')
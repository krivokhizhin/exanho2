import importlib
import logging
import time

from socketserver import TCPServer
from abc import ABCMeta

from . import ExanhoUnitBase, ServiceBase

class TCPServerUnit(ExanhoUnitBase):

    logger = logging.getLogger(__name__)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.serv = None
        self.service_class = None


    def initialize(self, *args, **kwargs):
        super().initialize()
            
        mod = importlib.import_module(self.config.handler)
        for service_name, service_class in vars(mod).items():
            self.log.debug(f'check initialize: service_name={service_name}, service_class={service_class}, type()=f{type(service_class)}')
            if ((type(service_class) == type or type(service_class) == ABCMeta)
            and issubclass(service_class, ServiceBase)
            and service_name != ServiceBase.__name__):
                self.service_class = service_class
                    
        if not self.service_class:
            raise Exception('{}: No services'.format(self.config.name))

        TCPServer.allow_reuse_address = True
        self.serv = TCPServer((self.config.host, self.config.port), self.service_class)
        self.serv.handle_error = self._handle_error

        self.log.info(f'The unit "{self.config.name}" has been initialized.')

    def run(self, *args, **kwargs):

        if self.config.concurrency_degree > 0:
            if self.config.concurrency_type == 'process':
                from multiprocessing import Process
                for n in range(self.config.concurrency_degree):
                    p = Process(target=self.serv.serve_forever)
                    p.daemon = True
                    p.start()
            elif self.config.concurrency_type == 'thread':
                from threading import Thread
                for n in range(self.config.concurrency_degree):
                    t = Thread(target=self.serv.serve_forever)
                    t.daemon = True
                    t.start()
            else:
                raise Exception(f'The concurrency_type is "{self.config.concurrency_type}". There must be either "Thread" or "Process".')

        self.log.info(f'The unit "{self.config.name}" has been started.')

        self.serv.serve_forever()

    def shutdown(self, *args, **kwargs):
        pass

    def _handle_error(self, request, client_address):
        log = logging.getLogger(TCPServerUnit.__module__)
        log.error(f'An exception occurred while processing the request from the address: {client_address}')
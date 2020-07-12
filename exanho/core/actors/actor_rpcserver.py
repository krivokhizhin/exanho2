import importlib
import logging

from abc import ABCMeta
from collections import defaultdict
from socketserver import TCPServer

from . import Actor, ServiceBase

JOIN_TIMEOUT = 1

class RpcServer(Actor):

    def run(self, config, context):
        log = logging.getLogger(__name__)

        self.servers = list()

        for service_config in config.services:

            mod = importlib.import_module(service_config.handler_module)  

            hosting_service = None   
            for service_name, service_class in vars(mod).items():
                if ((type(service_class) == type or type(service_class) == ABCMeta)
                and issubclass(service_class, ServiceBase)
                and service_name != ServiceBase.__name__):
                    hosting_service = service_class
                        
            if not hosting_service:
                raise Exception('{}: No services'.format(config.name))

            hosting_service.context = context

            if service_config.secret_key:
                hosting_service.secret_key = service_config.secret_key.encode('utf-8')          

            if service_config.db_domain:                
                mod.domain.configure(service_config.db_domain.url)
                log.info(f'The actor "{config.name}", service "{hosting_service.__name__}: domain has been configured')

                if service_config.db_domain.validate:
                    #TODO: move to a separate process
                    valid, errors, warnings = mod.domain.validate(service_config.db_domain.url)
                    if not valid:
                        log.error(errors)
                        if warnings:
                            log.warning(warnings)
                        raise RuntimeError(f'The database schema does not match the ORM model')
                    log.info(f'The actor "{config.name}", service "{hosting_service.__name__}: domain is valid')   

            TCPServer.allow_reuse_address = True
            serv = TCPServer((service_config.address.host, service_config.address.port), hosting_service)
            serv.handle_error = self._handle_error
            self.servers.append(serv)

            log.info(f'The actor "{config.name}": service "{hosting_service.__name__}" has been initialized')

            if service_config.concurrency.degree > 0:
                if service_config.concurrency.kind == 'process':
                    from multiprocessing import Process
                    for n in range(service_config.concurrency.degree):
                        p = Process(target=serv.serve_forever, name=f'Process#{n}')
                        p.daemon = True
                        p.start()
                elif service_config.concurrency.kind == 'thread':
                    from threading import Thread
                    for n in range(service_config.concurrency.degree):
                        t = Thread(target=serv.serve_forever, name=f'Thread#{n}')
                        t.daemon = True
                        t.start()
                else:
                    raise Exception(f'The concurrency_type is "{service_config.concurrency.kind}". There must be either "Thread" or "Process"')

            log.info(f'The actor "{config.name}": "{hosting_service.__name__}" has been started')

        log.info(f'The actor "{config.name}" has been installed')

    def finalize(self):
        for serv in self.servers:
            serv.server_close()       

    def handle(self, msg):
        pass

    def _handle_error(self, request, client_address):
        log = logging.getLogger(RpcServer.__module__)
        log.error(f'An exception occurred while processing the request from the address: {client_address}')
import importlib
import logging

from abc import ABCMeta
from xmlrpc.server import SimpleXMLRPCServer

from . import Actor, ServiceBase

JOIN_TIMEOUT = 1

class XmlRpcServer(Actor):

    def run(self, config, context):
        log = logging.getLogger(__name__)

        self.servers = list()

        for service_config in config.services:

            mod = importlib.import_module(service_config.handler_module)  
            interface_key = service_config.interface

            hosting_service = None   
            for service_name, service_class in vars(mod).items():
                if ((type(service_class) == type or type(service_class) == ABCMeta)
                and issubclass(service_class, ServiceBase)
                and service_name != ServiceBase.__name__
                and service_name.lower() != interface_key.lower()):
                    hosting_service = service_class
                        
            if not hosting_service:
                raise Exception('{}: No services'.format(config.name))

            hosting_service.context = context         

            if service_config.db_key:
                db_url = context.connectings[service_config.db_key]         
                mod.domain.configure(db_url)
                log.info(f'The actor "{config.name}", service "{hosting_service.__name__}: domain has been configured')

            SimpleXMLRPCServer.allow_reuse_address = True
            serv = SimpleXMLRPCServer(context.get_service_endpoint(interface_key), logRequests=False, allow_none=True, use_builtin_types=True)
            serv.register_instance(hosting_service())

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
import importlib
import logging

from abc import ABCMeta
from multiprocessing import Process
from xmlrpc.server import SimpleXMLRPCServer

from . import Actor, ServiceBase, ServeByProcess, serve_forever

JOIN_TIMEOUT = 1

class XmlRpcServer(Actor):

    def run(self, config, context):
        log = logging.getLogger(__name__)

        self._processes = list()

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

            SimpleXMLRPCServer.allow_reuse_address = True
            serv = SimpleXMLRPCServer(context.get_service_endpoint(interface_key), logRequests=False, allow_none=True, use_builtin_types=True)
            serv.register_instance(hosting_service())

            log.debug(f'The actor "{config.name}": service "{hosting_service.__name__}" has been initialized')

            if service_config.concurrency.kind.lower() == 'process':
                for n in range(service_config.concurrency.degree):
                    p = Process(target=serve_forever, name=f'{interface_key}-{n+1}', args=(serv.serve_forever, context, service_config.db_key), daemon=True)
                    p.start()
                    self._processes.append(ServeByProcess(p, serv))
                    log.debug(f'Service "{hosting_service.__name__}" has been located in "{p.name}" process')
            elif service_config.concurrency.kind.lower() == 'thread':
                p = Process(target=serve_forever, name=interface_key, args=(serv.serve_forever, context, service_config.db_key, service_config.concurrency.degree), daemon=True)
                p.start()
                self._processes.append(ServeByProcess(p, serv))
                log.debug(f'Service "{hosting_service.__name__}" has been located in "{p.name}" process')
            else:
                raise Exception(f'The concurrency_type is "{service_config.concurrency.kind}". There must be either "Thread" or "Process"')

            log.info(f'The actor "{config.name}": "{hosting_service.__name__}" has been started')

        log.info(f'The actor "{config.name}" has been installed')

    def finalize(self):
        for p, serv in self._processes:
            serv.server_close()
            p.join(JOIN_TIMEOUT)
            if p.is_alive():
                p.terminate()

    def handle(self, msg):
        pass
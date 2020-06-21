import logging
from xmlrpc.server import SimpleXMLRPCServer

from .actor_manager import ActorManager
from .actor_request_handler import ActorRequestHandler


class ExanhoServer:
    
    def __init__(self, main_cfg, log_listener, log_queue):
        self.log = logging.getLogger(__name__)

        # self.service = ExanhoService(main_cfg.actors_config_path, log_queue)
        self.manager = ActorManager(main_cfg.actors_config_path, log_queue)

        self.service_host = main_cfg.host
        self.service_port = main_cfg.port

        self.log_listener = log_listener
        self.log_queue = log_queue


    def start(self):
        self.log.info('Exanho is starting...')

        # 1. Load config
        self.manager.load_config()
        self.log.info(f'Manager context has been initialized: joinable_queues({len(self.manager.context.joinable_queues)})')

        # 2. Install actors from configuration file
        self.manager.install_actors_from_file()
        self.log.info('All actors have been configured.')

        # 3. Hosting SimpleXMLRPCServer
        server = SimpleXMLRPCServer((self.service_host, self.service_port), requestHandler=ActorRequestHandler, logRequests=False)
        server.register_introspection_functions()

        for method in (self.manager.install_actor, self.manager.uninstall_actor, self.manager.get_actor_list, self.manager.get_config):
            server.register_function(method)

        self.log.info('The XMLRPCServer has been created')

        try:
            server.serve_forever()
        except (KeyboardInterrupt):
            pass
        except:
            pass

        self.stop()            

    def stop(self):
        self.log.info('Exanho is stopping ...')

        for name, actor in self.manager.actors.items():
            self.log.info(f'Actor "{name}" is stopping ...')
            actor.close()
            actor.join()
            self.log.info(f'Actor "{name}" has been stopped.')

        self.log_queue.put_nowait(None)
        self.log_listener.join()

        self.log.info('Exanho server has been stopped.')

    def validate(self):
        has_db_model_configs = self.manager.get_has_db_model_configs()

        if not has_db_model_configs:
            print(f'There is nothing to validate from a actors file')
            return

        from . import db_validate as db
        results, canceled = db.validate(has_db_model_configs)
        
        if canceled:
            print('Validation canceled')
            return 

        for result in results:
            module, valid, errors, warnings = result
            if valid:
                print(f'{module} is valid')
            else:
                print(f'{module} is not valid')
            if errors:
                print('Errors:')
                for error in errors:
                    print(error)
            if warnings:
                print('Warnings:')
                for warning in warnings:
                    print(warning)
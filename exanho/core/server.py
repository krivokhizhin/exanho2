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
        self.manager.load_config()

        import concurrent.futures
        from exanho.orm.sqlalchemy import validate

        futures = dict()

        with concurrent.futures.ProcessPoolExecutor() as executor:
            for connecting in self.manager.context.connectings:
                self.log.debug(f'connecting: {connecting}')
                future = executor.submit(validate, *self.manager.context.get_url_with_models(connecting))
                futures[future] = connecting

        for future in concurrent.futures.as_completed(futures):
            err = future.exception()
            if err is None:
                valid, errors, warnings = future.result()
                if valid:
                    self.log.info(f'Model is valid for connecting "{connecting}". Warnings: {", ".join(warnings)}')
                else:
                    self.log.error(f'Model is not valid for connecting "{connecting}". Errors: {", ".join(errors)}. Warnings: {", ".join(warnings)}')
            else:
                self.log.exception(connecting, err.args)

    def create_model(self):
        self.manager.load_config()

        import concurrent.futures
        from exanho.orm.sqlalchemy import recreate

        futures = dict()

        with concurrent.futures.ProcessPoolExecutor() as executor:
            for connecting in self.manager.context.connectings:
                future = executor.submit(recreate, *self.manager.context.get_url_with_models(connecting))
                futures[future] = connecting

        for future in concurrent.futures.as_completed(futures):
            err = future.exception()
            if err is None:
                self.log.info(f'Models have been created for connecting "{connecting}"')
            else:
                self.log.exception(connecting, err.args[0])


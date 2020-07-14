
from collections import defaultdict
from multiprocessing import JoinableQueue

from .actors.configs import create_actor_config as actor_config_factory
from .exanho_config import ContextConfig

class Context:

    def __init__(self, log_queue):
        self._log_queue = log_queue
        self._context_config = None
        self._actor_configs = dict()
        self._connectings = dict()
        self._queues = defaultdict(JoinableQueue)
        self._services = dict()

    @property
    def log_queue(self):
        return self._log_queue

    @property
    def connectings(self):
        return self._connectings

    @property
    def joinable_queues(self):
        return self._queues

    @property
    def config(self):
        return self._context_config, self._actor_configs

    def set_config(self, context_dict:dict, actor_config_list:list):
        self._context_config = ContextConfig.create_instance(context_dict)

        if self._context_config.db_connectings:
            for conecting in self._context_config.db_connectings:
                self._connectings[conecting.name] = conecting.url

        if self._context_config.joinable_queues:
            for queue_config in self._context_config.joinable_queues:
                self._queues[queue_config.name] = JoinableQueue(queue_config.maxsize)

        if self._context_config.service_endpoints:
            for service_endpoint in self._context_config.service_endpoints:
                self._services[service_endpoint.interface.lower()] = self._check_and_modify_endpoint(service_endpoint.host, service_endpoint.port)

        for actor_config_dict in actor_config_list:
            actor_config = actor_config_factory(actor_config_dict)
            if self._actor_configs.get(actor_config.name) is None:
                self._actor_configs[actor_config.name] = actor_config
            else:
                raise Exception(f'The name of the {actor_config.name} worker is not unique')

    def _check_and_modify_endpoint(self, host, port, default_host='localhost'):
        if port is None or type(port) != int or port < 1024:
            raise Exception('The port value must be greater than 1023')

        if port in [port for host, port in self._services.values()]:
            raise Exception(f'The {port} port is already in use')

        if host is None or host == '':
            host = default_host

        return (host, port)

    def get_service_endpoint(self, interface_key):
        return self._services.get(interface_key.lower(), (None, None))
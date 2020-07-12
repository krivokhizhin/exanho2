
from abc import ABC
from collections import defaultdict
from multiprocessing import JoinableQueue

from .actors.configs import is_service_config, create_actor_config as actor_config_factory
from .exanho_config import ContextConfig, ExanhoConfig
from ..core.common import create_client_class

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

        for actor_config_dict in actor_config_list:
            actor_config = actor_config_factory(actor_config_dict)
            if self._actor_configs.get(actor_config.name) is None:
                self._actor_configs[actor_config.name] = actor_config
            else:
                raise Exception(f'The name of the {actor_config.name} worker is not unique')

        self.registry_services()

    def registry_services(self):
        pass
        # for actor_config in self._services.values():
        #     if not is_service_config(actor_config):
        #         continue

    def registry_service(self, interface, host, port, secretkey=None):
        if not issubclass(interface, ABC):
            raise Exception(f'{interface} is not an interface (subclass of ABC)')

        if interface in self._services:
            return

        self._services[interface] = create_client_class(interface, host, port, secretkey)

    def get_service(self, interface):
        service_class = self._services.get(interface)

        if service_class is None:
            return None

        return service_class()

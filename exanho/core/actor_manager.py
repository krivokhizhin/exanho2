import logging
from collections import defaultdict
from multiprocessing import JoinableQueue

from .manager_context import ContextConfig
from .config import json_actors
from .actors import Actor, actor_factory
from .actors.configs import create_actor_config as actor_config_factory

class Context:

    def __init__(self, log_queue):
        self._log_queue = log_queue
        self._queues = defaultdict(JoinableQueue)

    @property
    def log_queue(self):
        return self._log_queue

    @property
    def joinable_queues(self):
        return self._queues

class ActorManager:

    def __init__(self, config_path, log_queue):
        self.log = logging.getLogger(__name__)

        self.config_path = config_path
        self.context = Context(log_queue)
        self.actors = defaultdict(Actor)

    def initialize_context(self):
        context = json_actors.read_context_from_file(self.config_path)
        if not context:
            raise RuntimeError(f'No configuration for actors found in the specified file.')

        context_config = ContextConfig.create_instance(context)

        if context_config.joinable_queues:
            for queue_config in context_config.joinable_queues:
                self.context.joinable_queues[queue_config.name] = JoinableQueue(queue_config.maxsize)

    def install_config(self):
        configs = json_actors.read_actors_from_file(self.config_path)
        if not configs:
            raise RuntimeError(f'No configuration for actors found in the specified file.')
        
        for config in configs:  
            actor_config = actor_config_factory(config)
            self.install_actor(actor_config)

    def create_actor_config(self, config: dict):
        return actor_config_factory(config)

    def install_actor(self, config):
        actor = actor_factory.create(config, self.context)
        self.actors[config.name] = actor
        actor.start()

    def uninstall_actor(self, actor_name: str):
        actor = self.actors.get(actor_name, None)
        if not actor:
            raise RuntimeError(f'No actor named {actor_name} was found.')

        actor.close()
        actor.join()

        del self.actors[actor_name]

    def save_config(self):
        configs = [ actor.config.serialize() for name, actor in self.actors.items()]
        json_actors.write_actors_file(configs, self.config_path)

    def get_config(self, indent=4, saved=False):
        if saved:
            return json_actors.get_actor_configs_from_file(self.config_path, indent)
        else:
            configs = [ actor.config.serialize() for actor in self.actors.values()]
            return json_actors.get_actor_configs(configs, indent)

    def get_actor_list(self):
        return list(self.actors.keys())

    def get_actor_config(self, actor_name: str, indent=4):
        actor = self.actors.get(actor_name, None)
        if not actor:
            raise RuntimeError(f'No actor named {actor_name} was found.')

        config = actor.config.serialize()
        return json_actors.get_actor_config(config, indent)

    def get_has_db_model_configs(self):

        configs = json_actors.rread_actors_from_configead_actors_file(self.config_path)
        if not configs:
            raise RuntimeError(f'No configuration for actors found in the specified file.')
        
        has_db_model_configs = []

        for config in configs:  
            actor_config = actor_config_factory(config)

            if hasattr(actor_config, 'services'):
                for service in  actor_config.services:
                    if service.db_domain:
                        has_db_model_configs.append({'module':service.handler_module, 'url':service.db_domain.url})

            if hasattr(actor_config, 'workers'):
                for worker in  actor_config.workers:
                    if worker.db_domain:
                        has_db_model_configs.append({'module':worker.module, 'url':worker.db_domain.url})

        return has_db_model_configs
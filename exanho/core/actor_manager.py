import logging
from collections import defaultdict

from .manager_context import Context
from .config import json_actors
from .actors import Actor, actor_factory
from .actors.configs import create_actor_config as actor_config_factory

LAUNCH_WAIT = 5

class ActorManager:

    def __init__(self, config_path, log_queue):
        self.log = logging.getLogger(__name__)

        self.config_path = config_path
        self.context = Context(log_queue)
        self.actors = defaultdict(Actor)

    def load_config(self):
        context, actors = json_actors.read_config_from_file(self.config_path)
        self.context.set_config(context, actors)

    def install_actors_from_file(self):
        context_config, actors_dict = self.context.config
        for actor_config in actors_dict.values():
            actor = actor_factory.create(actor_config, self.context)
            self.actors[actor_config.name] = actor
            actor.start()
            actor.launched.wait(LAUNCH_WAIT)

    def install_actor(self, config:str):
        actor_config = json_actors.convert_config_to_dict(config)
        actor = actor_factory.create(actor_config, self.context)
        self.actors[actor_config.name] = actor
        actor.start()

        self.save_config()

    def uninstall_actor(self, actor_name: str):
        actor = self.actors.get(actor_name, None)
        if not actor:
            raise Exception(f'No actor named "{actor_name}" was found.')

        actor.close()
        actor.join()

        del self.actors[actor_name]

        self.save_config()

    def save_config(self):
        context_config, actors_dict = self.context.config
        json_actors.write_actors_file(context_config, actors_dict.values(), self.config_path)

    def get_config(self, indent=4) -> str:
        return json_actors.get_config_from_file(self.config_path, indent)

    def get_actor_list(self) -> list:
        return list(self.actors.keys())

    def get_actor_config(self, actor_name: str, indent=4):
        actor = self.actors.get(actor_name, None)
        if not actor:
            raise Exception(f'No actor named {actor_name} was found.')

        config = actor.config.serialize()
        return json_actors.get_actor_config(config, indent)

    def get_has_db_model_configs(self):

        configs = json_actors.read_actors_from_file(self.config_path)
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
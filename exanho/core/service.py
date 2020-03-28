import logging
from collections import defaultdict

from .common import try_logged
from .config import json_actors
from .contract import IExanhoService
from .actors import Actor, actor_factory
from .actors.configs import create_actor_config as actor_config_factory


class ExanhoExit(Exception):
    pass

class ExanhoService(IExanhoService):

    def __init__(self, config_path, log_queue):
        self.log = logging.getLogger(__name__)

        self.config_path = config_path
        self.log_queue = log_queue

        self.actors = defaultdict(Actor)
   
    @try_logged 
    def install_actor(self, config, save=True):
        actor = actor_factory.create(config, self.log_queue)
        # creator.validate()(config)
        self.actors[config.name] = actor
        actor.start()

        if save:
            configs = [ actor.config.json_obj for name, actor in self.actors.items()]
            json_actors.write_actor_configs(configs, self.config_path)

    @try_logged
    def unistall_actor(self, actor_name, save=True):
        pass

    @try_logged
    def install_config(self):
        configs = json_actors.read_actors_file(self.config_path)
        if not configs:
            raise RuntimeError(f'No configuration for actors found in the specified file.')
        
        for config in configs:
            actor_config = actor_config_factory(config)
            self.install_actor(actor_config, save=False)

    @try_logged
    def get_config(self):
        pass

    @try_logged
    def get_actor_config(self, actor_name):
        if actor_name not in self.actors:
            raise RuntimeError(f'No actor named {actor_name} was found.')

        config = self.actors[actor_name].config.json_obj
        self.log.debug(config.__dict__)
        return json_actors.get_config_str(config)

    @try_logged
    def get_actor_list(self):
        pass

    @try_logged
    def shutdown(self):
        return ExanhoExit

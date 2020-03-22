import logging
from collections import defaultdict

from .common import try_logged
from .config import read_actor_configs
from .contract import IExanhoService
from .actors import Actor, actor_factory


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

    @try_logged
    def unistall_actor(self, actor_name, save=True):
        pass

    @try_logged
    def install_config(self):
        actor_configs = read_actor_configs(self.config_path)
        for actor_config in actor_configs:
            self.install_actor(actor_config, save=False)

    @try_logged
    def get_config(self):
        pass

    @try_logged
    def get_actor_config(self, actor_name):
        pass

    @try_logged
    def get_actor_list(self):
        pass

    @try_logged
    def shutdown(self):
        return ExanhoExit

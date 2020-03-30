import logging
from collections import defaultdict

from . import IExanhoService, ActorManager
from .common import try_logged
from .config import json_actors

class ExanhoExit(Exception):
    pass

class ExanhoService(IExanhoService):

    def __init__(self, manager: ActorManager, config_path: str):
        self.log = logging.getLogger(__name__)
        self.manager = manager
        self.config_path = config_path
   
    @try_logged 
    def install_actor(self, config: str, save=False):
        config_dict = json_actors.convert_config_to_dict(config)
        actor_config = self.manager.create_actor_config(config_dict)
        actor = self.manager.install_actor(actor_config)

        if save:
            self.manager.save_config()

    @try_logged
    def uninstall_actor(self, actor_name: str, save=False):
        self.manager.uninstall_actor(actor_name)

        if save:
            self.manager.save_config()

    @try_logged
    def get_config(self, indent=4, saved=False):
        return self.manager.get_config(int(indent), bool(saved))

    @try_logged
    def get_actor_list(self):
        return self.manager.get_actor_list()

    @try_logged
    def get_actor_config(self, actor_name: str, indent=4):
        return self.manager.get_actor_config(actor_name, int(indent))

    @try_logged
    def shutdown(self):
        return ExanhoExit

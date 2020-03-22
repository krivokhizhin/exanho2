from abc import ABC, abstractmethod

class IExanhoService(ABC):
    
    @abstractmethod
    def install_actor(self, config, save=True):
        pass

    @abstractmethod
    def unistall_actor(self, save=True):
        pass

    @abstractmethod
    def install_config(self, config):
        pass

    @abstractmethod
    def get_config(self):
        pass

    @abstractmethod
    def get_actor_config(self, actor_name):
        pass

    @abstractmethod
    def get_actor_list(self):
        pass

    @abstractmethod
    def shutdown(self):
        pass
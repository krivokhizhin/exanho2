from abc import ABC, abstractmethod

class IExanhoService(ABC):
    
    @abstractmethod
    def install_actor(self, config: str, save=True):
        pass

    @abstractmethod
    def uninstall_actor(self, save=True):
        pass

    @abstractmethod
    def get_config(self):
        pass

    @abstractmethod
    def get_actor_list(self):
        pass

    @abstractmethod
    def get_actor_config(self, actor_name: str):
        pass

    @abstractmethod
    def shutdown(self):
        pass
from abc import ABC, abstractmethod

class IExanhoService(ABC):
    
    @abstractmethod
    def install_unit(self, config, log_queue, save=True):
        pass

    @abstractmethod
    def unistall_unit(self, unit_name, save=True):
        pass

    @abstractmethod
    def install_config(self, config):
        pass

    @abstractmethod
    def get_config(self):
        pass

    @abstractmethod
    def get_unit_config(self, unit_name):
        pass

    @abstractmethod
    def get_unit_list(self):
        pass
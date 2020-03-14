from .units import ServiceBase

class ExanhoService(ServiceBase):
    
    def install_unit(self, config, log_queue, save=True):
        pass

    def unistall_unit(self, unit_name, save=True):
        pass

    def install_config(self, config):
        pass

    def get_config(self):
        pass

    def get_unit_config(self, unit_name):
        pass

    def get_unit_list(self):
        pass
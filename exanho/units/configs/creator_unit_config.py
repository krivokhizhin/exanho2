from . import TCPServerUnitConfig

def create_unit_config(config):
    if config.kind.lower() == 'TCPServerUnit'.lower():
        return TCPServerUnitConfig.create_instance(config)
    
    raise Exception('Unknown type of unit configuration: {}.'.format(config.kind)) 
from configparser import ConfigParser
import os

from inspect import currentframe, getframeinfo
from pathlib import Path

from .ini_options import config_filename, main_section, host_option, port_option, actors_config_option, logging_pub_bind_option, logging_maxsize_option, logging_config_option
from . import AppCfg
from ..common import JsonObject
from ..actors.configs import create_actor_config

def read_sys_config():
    filename = getframeinfo(currentframe()).filename
    resolver = Path(filename).resolve()
    #print('\nresolver.parents:\n{}'.format(list(resolver.parents)))
    config_path = str(resolver.parents[2]) + '/' + config_filename

    cfg = ConfigParser()
    if os.path.exists(config_path):
        cfg.read(config_path)    
    else:
        raise Exception('{} is not exists.'.format(config_path))

    if main_section not in cfg.sections():
        raise Exception('There is "{}" section not in {} .'.format(main_section, config_path))

    main_cfg = AppCfg(
        cfg.get(main_section, host_option),
        int(cfg.get(main_section, port_option)),
        cfg.get(main_section, actors_config_option),
        cfg.get(main_section, logging_pub_bind_option),
        int(cfg.get(main_section, logging_maxsize_option)),
        cfg.get(main_section, logging_config_option)
        )    

    return main_cfg

def read_actor_configs(actor_config_file):
    actors_cfg = JsonObject.create_from_file(actor_config_file)
    actor_configs = list(map(create_actor_config, actors_cfg.exanho_actors))
    return actor_configs

from configparser import ConfigParser
import os

from inspect import currentframe, getframeinfo
from pathlib import Path

from .ini_options import *
from . import AppCfg
from ..common import JsonObject
from ..units.configs import create_unit_config

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

    # clients = {}
    # clients_section_names = [section_name for section_name in cfg.sections() if str(section_name).lower().endswith(client_section_posfix)]
    # for section_name in clients_section_names:
    #     clients[cfg.get(section_name, client_token_option)] = cfg.get(section_name, client_name_option)

    main_cfg = AppCfg(
        cfg.get(main_section, host_option),
        int(cfg.get(main_section, port_option)),
        cfg.get(main_section, units_config_option),
        cfg.get(main_section, logging_pub_bind_option),
        int(cfg.get(main_section, logging_maxsize_option)),
        cfg.get(main_section, logging_config_option)
        )    

    return main_cfg

def read_unit_configs(unit_config_file):
    units_cfg = JsonObject.create_from_file(unit_config_file)
    unit_configs = list(map(create_unit_config, units_cfg.exanho_units))
    return unit_configs

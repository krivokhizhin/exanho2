import argparse
# import logging

from . import server
from . import installer
from .config import read_sys_config, read_unit_configs
# from .config import start_log_listener

def run():
    args = parse_arguments()

    # 1. read config file 
    main_cfg = read_sys_config()

    # 2. start logging
    # log_listener, log_queue = start_log_listener(main_cfg)

    # h = logging.handlers.QueueHandler(log_queue)
    # log = logging.getLogger()
    # log.addHandler(h)
    # log.setLevel(logging.DEBUG)

    # log.info("Logging has been configured.")

    # 3. read service configurations 
    unit_configs = read_unit_configs(main_cfg.units_config)

    # log.info("The worker configurations has been read.")

    # exanho = server.ExanhoServer(main_cfg, workers_cfg, log_listener, log_queue)
    exanho = server.ExanhoServer(main_cfg, unit_configs, None, None)

    if args.install:
        installer.install()
    elif args.uninstall:
        installer.uninstall()
    elif args.validate:
        exanho.validate()
    else:
        exanho.start()

def parse_arguments():
    parser = argparse.ArgumentParser(
            usage='%(prog)s [options]',
            description='Execution and hosting framework (exanho, ExAnHo)'
            )
    parser.add_argument('-install', action='store_true',
            help='ExAnHo installation as daemon proccess')
    parser.add_argument('-uninstall', action='store_true',
            help='uninstalling ExAnHo as daemon proccess')
    parser.add_argument('-validate', action='store_true',
            help='validate ExAnHo configuration')

    arguments = parser.parse_args()

    return arguments
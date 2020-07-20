import argparse
import logging

from .server import ExanhoServer
from . import installer
from .config import read_sys_config
from .log_listener import start_log_listener

def run():
    args = parse_arguments()

    if args.install:
        installer.install()
        return

    if args.uninstall:
        installer.uninstall()
        return

    # 1. read config file 
    main_cfg = read_sys_config()

    # 2. start logging
    log_thread, log_queue = start_log_listener(main_cfg.logging_config, main_cfg.logging_maxsize)

    log = logging.getLogger(__name__)
    log.info("Logging has been configured.")

    exanho = ExanhoServer(main_cfg, log_thread, log_queue)

    if args.validate:
        exanho.validate()
    elif args.create:
        exanho.create_model()
    else:
        exanho.start()

def parse_arguments():
    parser = argparse.ArgumentParser(
            usage='%(prog)s [options]',
            description='Execution and hosting framework (exanho, ExAnHo)'
            )
    parser.add_argument('-install', action='store_true',
            help='ExAnHo installation as systemd service')
    parser.add_argument('-uninstall', action='store_true',
            help='uninstalling ExAnHo as systemd service')
    parser.add_argument('-validate', action='store_true',
            help='validate DB model')
    parser.add_argument('-create', action='store_true',
            help='create model in DB')

    arguments = parser.parse_args()

    return arguments
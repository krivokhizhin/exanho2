# import concurrent.futures
# import multiprocessing
import logging
# import logging.config
# import logging.handlers
# import importlib
# import operator

from multiprocessing import AuthenticationError
from multiprocessing.connection import Listener
from threading import Thread
import time
import uuid
import select

from .rpcserver import RPCHandler
from . import UnitManager

# from .config import start_log_listener

class ExanhoServer:
    
    def __init__(self, main_cfg, unit_configs, log_listener, log_queue):
        self.main_cfg = main_cfg
        self.unit_configs = unit_configs
        self.log_listener = log_listener
        self.manager = UnitManager(log_queue)

        self.log = logging.getLogger(__name__)

    def start(self):
        self.log.info('Exanho is starting...')

        if self.unit_configs:
            for unit_config in self.unit_configs:
                self.manager.install_unit(unit_config)

        self.log.info('All units have been configured.')

        is_exit = True
        while is_exit:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                is_exit = False

        self.stop()            

    def stop(self):
        self.manager.log_queue.put_nowait(None)
        self.log_listener.join()
        self.log.info('Exanho has been stopped.')

    def validate(self):
        pass
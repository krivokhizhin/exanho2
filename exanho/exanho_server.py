import collections
import logging
import multiprocessing
import time

from socketserver import TCPServer
from threading import Thread

from .config import read_unit_configs
from . import ExanhoService
from . import run_unit_wrapper
from .units.creators.get_creator import get_creator

class ExanhoServer:
    
    def __init__(self, main_cfg, log_listener, log_queue):
        self.log = logging.getLogger(__name__)

        self.main_cfg = main_cfg
        self.log_listener = log_listener
        self.log_queue = log_queue
        self.serv = None


    def start(self):
        self.log.info('Exanho is starting...')   

        # 1. Hosting and start ExanhoService
        TCPServer.allow_reuse_address = True
        self.serv = TCPServer((self.main_cfg.host, self.main_cfg.port), ExanhoService)

        manage_thread = Thread(target=self.serv.serve_forever)
        manage_thread.daemon = True
        manage_thread.start()

        self.log.info('The UnitManager thread has been started.')

        # 2. read unit configurations 
        self._install_from_config(self.main_cfg.unit_config_path, self.log_queue)
        self.log.info("The unit configurations has been read.")

        self.log.info('All units have been configured.')

        is_exit = True
        try:
            while manage_thread.is_alive():
                time.sleep(1)
        except KeyboardInterrupt:
            self.log.info('KeyboardInterrupt pressed.')

        self.stop()            

    def stop(self):
        self.log.info('Exanho is stopping ...')
        self.serv.shutdown()
        self.serv.server_close()
        self.log_queue.put_nowait(None)
        self.log_listener.join()
        self.log.info('Exanho has been stopped.')

    def validate(self):
        pass

    def _install_from_config(self, config_path, log_queue):
        unit_configs = read_unit_configs(config_path)
        for unit_config in unit_configs:
            creator = get_creator(unit_config.kind)
            # creator.validate()(config)

            process = multiprocessing.Process(target=run_unit_wrapper, args=(creator, ), kwargs={'config':unit_config, 'log_queue':log_queue}, name=unit_config.name)
            process.daemon = True
            process.start()

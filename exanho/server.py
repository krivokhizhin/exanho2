import logging
import time

from socketserver import TCPServer
from threading import Thread

from .rpcserver import RPCHandler
from . import UnitManager

# from .config import start_log_listener

class ExanhoServer:
    
    def __init__(self, main_cfg, unit_configs, log_listener, log_queue):
        self.log = logging.getLogger(__name__)

        self.main_cfg = main_cfg
        self.unit_configs = unit_configs
        self.log_listener = log_listener
        self.manager = UnitManager(log_queue)

        TCPServer.allow_reuse_address = True
        self.serv = TCPServer((self.main_cfg.host, self.main_cfg.port), self.manager)


    def start(self):
        self.log.info('Exanho is starting...')

        manage_thread = Thread(target=self.serv.serve_forever)
        manage_thread.daemon = True
        manage_thread.start()

        self.log.info('The UnitManager thread has been started.')

        if self.unit_configs:
            for unit_config in self.unit_configs:
                self.manager.install_unit(unit_config)

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
        self.manager.log_queue.put_nowait(None)
        self.log_listener.join()
        self.log.info('Exanho has been stopped.')

    def validate(self):
        pass
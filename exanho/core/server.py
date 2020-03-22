import collections
import logging
import multiprocessing
import socket
import time
from queue import Queue
from threading import Thread

from . import ExanhoExit, ExanhoService
from .common import receive_rpc_data, send_rpc_data


class ExanhoServer:
    
    def __init__(self, main_cfg, log_listener, log_queue):
        self.log = logging.getLogger(__name__)

        self.service = ExanhoService(main_cfg.actors_config_path, log_queue)

        self.service_host = main_cfg.host
        self.service_port = main_cfg.port

        self.log_listener = log_listener
        self.log_queue = log_queue
        
        self.mailbox = Queue()


    def start(self):
        self.log.info('Exanho is starting...')   

        # 1. Hosting and start ExanhoService        

        t = Thread(target=self.host_service, args=(self.service_host, self.service_port, ))
        t.daemon = True
        t.start()

        self.log.info('The ExanhoService has been hosted..')

        # 2. Install actors from configuration file
        self.service.install_config()
        self.log.info('All actors have been configured.')
        
        while True:
            try:
                args, kwargs = self.mailbox.get()
                func_name, *args = args
                self.mailbox.task_done()
                result = getattr(self.service, func_name)(*args,**kwargs)
                self.mailbox.put(result)
                self.mailbox.join()
                if result is ExanhoExit:
                    raise ExanhoExit()
            except (KeyboardInterrupt, ExanhoExit):
                break
            except:
                pass

        self.stop()            

    def stop(self):
        self.log.info('Exanho is stopping ...')

        for name, actor in self.service.actors.items():
            actor.close()
            actor.join()
            self.log.info(f'Actor "{name}" has been stopped.')

        self.log_queue.put_nowait(None)
        self.log_listener.join()

        self.log.info('Exanho server has been stopped.')

    def validate(self):
        pass

    def host_service(self, host, port):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((host, port))
        serversocket.listen(5)

        while True:
            (clientsocket, address) = serversocket.accept() 
            result = receive_rpc_data(clientsocket)
            self.mailbox.put(result)
            self.mailbox.join()
            result = self.mailbox.get()
            self.mailbox.task_done()
            if result is ExanhoExit:
                send_rpc_data(clientsocket, 'OK')
                break
            else:
                send_rpc_data(clientsocket, result)

        self.log.info('The ExanhoService has been stopped.')

# import concurrent.futures
# import multiprocessing
# import logging
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
from . import WorkerManager

# from .config import start_log_listener

class ExanhoServer:

    # logger = logging.getLogger(__name__)
    
    def __init__(self, main_cfg, unit_configs, log_listener, log_queue):
        self.main_cfg = main_cfg
        self.unit_configs = unit_configs
        self.log_listener = log_listener
        self.manager = WorkerManager(log_queue)

        # self.logger = logging.getLogger(__name__)

    def rpc_server(self, handler, address, authkey):
        sock = Listener(address, authkey=authkey)
        exit_token = str(uuid.uuid4()).encode('ascii')
        print(exit_token)
        while True:
            try:
                can_recv, _, can_exit = select.select([sock.accept()],[],[])
                for client in can_recv:
                    t = Thread(target=handler.handle_connection, args=(client, exit_token,))
                    t.daemon = True
                    t.start()
            except AuthenticationError:
                pass

    def start(self):

        print('START')

        if self.unit_configs:
            for unit_config in self.unit_configs:
                self.manager.install_worker(unit_config)

        print('install_worker')

        is_exit = True
        while is_exit:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                is_exit = False

        # is_exit = False

        # while not is_exit:
        #     try:
        #         control_request_dto = socket.recv_json(object_hook=JsonObject)
        #         self.logger.debug(f'Received - {control_request_dto}')

        #         if control_request_dto.jsonrpc != self.main_cfg.jsonrpc_version:
        #             raise Exception(f"The client json-rpc version '{control_request_dto.jsonrpc}' version does not match the server version '{self.main_cfg.jsonrpc_version}'.")

        #         if control_request_dto.client_token not in self.main_cfg.clients:
        #             raise Exception("The client token '{}' is not valid.".format(control_request_dto.client_token))

        #         response = ResponseDto(control_request_dto.id, self.main_cfg.jsonrpc_version)
        #         try:
        #             response.set_result(operator.methodcaller(control_request_dto.method, control_request_dto.params)(self.manager))
        #         except ExitException as ex:
        #             is_exit = True
        #         except Exception as ex:
        #             response.set_result(ErrorRequestResult(ResponseCode.ERROR, ex.args[0]))
        #             self.logger.exception(ex)

        #         socket.send_json(response.serialize_for_json())

        #     except KeyboardInterrupt:
        #         self.logger.info(f'KeyboardInterrupt')
        #         is_exit = True
        #     except Exception as ex:
        #         self.logger.exception(ex)
        #         error_res = ErrorRequestResult(ResponseCode.ERROR, ex.args[0])
        #         response = ResponseDto(ResponseCode.UNKNOWN.value, self.main_cfg.jsonrpc_version, error_res)
        #         socket.send_json(response.serialize_for_json())
        #         self.logger.exception(ex)

        self.stop()            

    def stop(self):
        # self.manager.log_queue.put_nowait(None)
        # self.log_listener.join()
        print('STOP')

    def validate(self):
        pass
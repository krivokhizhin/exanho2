
import multiprocessing
import logging
import time
# import logging.config
# import logging.handlers

# from .zmq_log_handler import ZeroMQSocketHandler 

from ..config import AppCfg

def start_log_listener(main_cfg : AppCfg):
    #multiprocessing.log_to_stderr()
    log_queue = multiprocessing.Queue(main_cfg.logging_maxsize)
    log_listener = multiprocessing.Process(target=_log_listener_process, args=(main_cfg, log_queue, _listener_configurer))
    log_listener.daemon = True
    log_listener.start()

    while not log_listener.is_alive:
        time.sleep(1)

    return log_listener, log_queue

def _listener_configurer(main_cfg : AppCfg):

    # root = logging.getLogger()
    # f = logging.Formatter('%(asctime)s %(levelname)-8s %(processName)-10s %(name)s %(message)s')

    # file_handler = logging.handlers.RotatingFileHandler('rosmet.log', 'a', 5*1024*1024, 10)
    # file_handler.setFormatter(f)
    # root.addHandler(file_handler)

    # zmq_handler = ZeroMQSocketHandler(main_cfg.logging_pub_bind)
    # zmq_handler.setFormatter(f)
    # root.addHandler(zmq_handler)
    
    # logging.config.fileConfig(main_cfg.logging_config)
    # logger = logging.getLogger('rosmet')
    # handler = ZeroMQSocketHandler(main_cfg.logging_pub_bind)
    # formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(processName)-10s %(name)s %(message)s')
    # handler.setFormatter(formatter)
    # handler.setLevel(logging.DEBUG)
    # logger.addHandler(handler)
    # logger.propagate = 0

    import logging.config
    from .zmq_log_handler import ZeroMQSocketHandler 
    from ..config import logconfig
    logging.config.dictConfig(logconfig)

def _log_listener_process(main_cfg : AppCfg, queue, configurer):    
    configurer(main_cfg)
    while True:
        try:
            record = queue.get()
            if record is None:  # We send this as a sentinel to tell the listener to quit.
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)  # No level or filter logic applied - just do it!
        except Exception:
            import sys, traceback
            print('Whoops! Problem:', file=sys.stderr)
            traceback.print_exc(file=sys.stderr)

    print('********************The log_listener has stopped working.******************************')
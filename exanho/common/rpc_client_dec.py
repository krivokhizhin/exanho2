import socket
from functools import wraps

from . import rpc_utilities as util

def init_socket(host, port):
    '''
    ...
    '''
    def decorate(func):
        def wrapper(this, *args, **kwargs):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                util.send_rpc_data(sock, func.__name__, *args, **kwargs)
                return util.receive_rpc_data(sock)
        return wrapper
    return decorate

def implement_rpc_client(host, port):
    def decorate(cls):
        for attr in cls.__abstractmethods__:
            setattr(cls, attr, init_socket(host, port)(getattr(cls, attr)))
        cls.__abstractmethods__ = frozenset()
        return cls
    return decorate
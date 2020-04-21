import socket
from functools import wraps

from . import rpc_utilities as util
from .authenticate import client_authenticate

def init_socket(host, port, secretkey):
    '''
    ...
    '''
    def decorate(func):
        def wrapper(this, *args, **kwargs):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                if secretkey:
                    client_authenticate(sock, secretkey)
                util.send_rpc_data(sock, func.__name__, *args, **kwargs)
                return util.receive_rpc_data(sock)
        return wrapper
    return decorate

def implement_rpc_client(host, port, secretkey=None):
    def decorate(cls):
        for attr in cls.__abstractmethods__:
            setattr(cls, attr, init_socket(host, port, secretkey)(getattr(cls, attr)))
        cls.__abstractmethods__ = frozenset()
        return cls
    return decorate

def create_client_class(interface, host, port, secretkey=None):
    _class = type('RpcClient', (interface,), {})
    _class = implement_rpc_client(host, port, secretkey)(_class)
    return _class
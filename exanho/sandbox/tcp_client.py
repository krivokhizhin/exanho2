# import socket
import sys
# import json
import operator

from core.i_service import IExanhoService
from core.common import implement_rpc_client
from interfaces import ISampleService

@implement_rpc_client('localhost', 3110, b'peekaboo')
class ExanhoClient(IExanhoService):
    pass

@implement_rpc_client('localhost', 3120, b'qwerty')
class SampleClient(ISampleService):
    pass

clients = {
    'exanho': ExanhoClient(),
    'sample': SampleClient()
}

def send():
    client, method, params = clients[sys.argv[1]], sys.argv[2], sys.argv[3:]
    print("Will be sent:     {}.{}({})".format(client.__class__.__name__, method, params))
    received = operator.methodcaller(method, *params)(client)
    print("Received: {}".format(received))
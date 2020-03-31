# import socket
import sys
# import json
import operator

from core import IExanhoService
from core.common import implement_rpc_client
from interfaces import ISampleService

@implement_rpc_client('localhost', 3110, b'peekaboo1')
class ExanhoClient(IExanhoService):
    pass

@implement_rpc_client('localhost', 3120)
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
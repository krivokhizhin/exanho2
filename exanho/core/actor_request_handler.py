from xmlrpc.server import SimpleXMLRPCRequestHandler

PATH = '/actor'

class ActorRequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = (PATH, )
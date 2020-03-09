import json
import operator

from .common import ExitException

class RPCHandler:
    def __init__(self, service):
        self.service = service
        self._functions = { }

    def register_function(self, func):
        self._functions[func.__name__] = func

    def __getattr__(self, name):
        return getattr(self.service, name)

    def handle_connection(self, connection, exit_token):
        try:
            while True:
                func_name, args, kwargs = json.loads(connection.recv())
                try:
                    r = getattr(self, func_name)(*args,**kwargs)
                    connection.send(json.dumps(r))
                except ExitException as e:
                    connection.send(json.dumps('EXIT'))
                except Exception as e:
                    connection.send(json.dumps(str(e)))
        except EOFError:
            pass
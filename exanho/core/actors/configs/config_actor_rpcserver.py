from ...common import JsonObject
from ...contract import HasDbConnect, HasHandler, ActorConfig

class RpcServerActorConfig(HasDbConnect, HasHandler, ActorConfig):  
    
    def __init__(self, json_obj: JsonObject):
        super().__init__(json_obj)

        self._host = json_obj.address.host
        self._port = int(json_obj.address.port)

        self._concurrency_degree = int(json_obj.concurrency.degree) if json_obj.concurrency and json_obj.concurrency.degree else 0
        self._concurrency_type = json_obj.concurrency.type.lower() if json_obj.concurrency and json_obj.concurrency.degree else None

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def concurrency_type(self):
        return self._concurrency_type

    @property
    def concurrency_degree(self):
        return self._concurrency_degree
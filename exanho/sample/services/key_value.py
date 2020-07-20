import logging
import time

from exanho.core.common import try_logged, Timer
from exanho.core.actors import ServiceBase
from exanho.interfaces import IKeyValueService
from exanho.orm.sqlalchemy import Sessional

from ..model import ValueType, KeyValue

class KeyValueService(IKeyValueService, ServiceBase):

    logger = logging.getLogger(__name__)
    
    @try_logged
    @Sessional
    def create(self, value):

        value_type = None
        rec_value = None
        if isinstance(value, str):
            value_type = ValueType.str
            rec_value = value
        elif isinstance(value, int):
            value_type = ValueType.int
            rec_value = str(value)
        else:
            raise TypeError(f'The type "{type(value)}" is not supported')

        session = Sessional.domain.Session
        record = KeyValue(type=value_type, value=rec_value)
        session.add(record)
        session.flush()
        
        return record.key

    @try_logged
    @Sessional
    def read(self, key):
        session = Sessional.domain.Session
        record = session.query(KeyValue).get(key)

        if record is None:
            return None

        if record.type == ValueType.str:
            return record.value
        if record.type == ValueType.int:
            return int(record.value)

        raise TypeError(f'The type "{record.type}" is not supported')
   
    @try_logged
    def update(self, key, value):
        pass
    
    @try_logged
    def delete(self, key):
        pass
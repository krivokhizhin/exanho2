import logging

from exanho.core.common import try_logged
from exanho.core.actors import ServiceBase
from exanho.interfaces import IPycadesHelperService

from ..utilities import hash_gost_2012_512, hash_gost_2012_256, hash_gost_3411

class PycadesHelperService(IPycadesHelperService, ServiceBase):

    logger = logging.getLogger(__name__)
    
    @try_logged
    def hash_gost_2012_512(self, data:bytes):
        return hash_gost_2012_512(data)
    
    @try_logged
    def hash_gost_2012_256(self, data:bytes):
        return hash_gost_2012_256(data)
    
    @try_logged
    def hash_gost_3411(self, data:bytes):
        return hash_gost_3411(data)
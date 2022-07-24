import logging

from exanho.core.common import try_logged
from exanho.core.actors import ServiceBase
from exanho.interfaces import IPycadesHelperService

import exanho.pycades.utilities as util

class PycadesHelperService(IPycadesHelperService, ServiceBase):

    logger = logging.getLogger(__name__)
    
    @try_logged
    def hash_gost_2012_512(self, data:bytes):
        return util.hash_gost_2012_512(data)
    
    @try_logged
    def hash_gost_2012_256(self, data:bytes):
        return util.hash_gost_2012_256(data)
    
    @try_logged
    def hash_gost_3411(self, data:bytes):
        return util.hash_gost_3411(data)

    @try_logged
    def sign(self, content: str, thumbprint: str, encoding_type:str, detached=True):
        return util.sign(content, thumbprint, encoding_type, detached)

    @try_logged
    def sign_hash(self, hash: str, thumbprint: str, hash_alg:int):
        return util.sign_hash(hash, thumbprint, hash_alg)
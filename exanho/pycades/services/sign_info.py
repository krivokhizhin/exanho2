import logging

from exanho.core.common import try_logged
from exanho.core.actors import ServiceBase
from exanho.interfaces import ISignInfoService

from ..sign_info import by_content_sign, by_file_hash_sign, by_hash_sign

class SignInfoService(ISignInfoService, ServiceBase):

    logger = logging.getLogger(__name__)
    
    @try_logged
    def by_content_sign(self, content:str, sign:str, encoding_type:str):
        return by_content_sign(content, sign, encoding_type)
    
    @try_logged
    def by_file_hash_sign(self, _file:bytes, sign:str, hash_alg:int):
        return by_file_hash_sign(_file, sign, hash_alg)
    
    @try_logged
    def by_hash_sign(self, hash:str, sign:str, hash_alg:int):
        return by_hash_sign(hash, sign, hash_alg)
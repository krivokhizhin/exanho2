import logging
import time

from exanho.core.common import try_logged, Timer
from exanho.core.actors import ServiceBase
from exanho.interfaces import ISampleService2
from exanho.orm.sqlalchemy import has_domain

@has_domain
class SampleService2(ISampleService2, ServiceBase):

    logger = logging.getLogger(__name__)

    @try_logged
    def echo(self, *args, **kwargs):
        return 'echo', args, kwargs
    
    @try_logged
    def put(self, *args, **kwargs):
        pass
    
    @try_logged
    def get(self, *args, **kwargs):
        pass
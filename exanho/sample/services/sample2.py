import logging
import time

from exanho.core.common import try_logged, Timer
from exanho.core.actors import ServiceBase
from exanho.interfaces import ISampleService2

class SampleService2(ISampleService2, ServiceBase):

    logger = logging.getLogger(__name__)

    @try_logged
    def echo(self, *args, **kwargs):
        return 'echo', args, kwargs
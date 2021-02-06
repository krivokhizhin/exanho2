from .drivers import IVkDriver
from .dto import VkResponse
from .dto.bot import LongPollResponse

URL_VK_BOT = '{server}?act=a_check&key={key}&ts={ts}&wait={wait}'
MIN_WAIT = 1
MAX_WAIT = 90
WAIT = 25

class VkBotSession:

    def __init__(self, driver:IVkDriver, server:str, key:str, ts:int=0, wait:int=WAIT) -> None:
        self.driver = driver
        self.server = server
        self.key = key
        self.ts = ts
        self.set_wait(wait)

    def set_wait(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Expected a int, received a {type(value)}')
        
        self.wait = min(MAX_WAIT, max(MIN_WAIT, value))
        
    def pool_events(self) -> LongPollResponse:
        url = URL_VK_BOT.format(server=self.server, key=self.key, ts=self.ts, wait=self.wait)
        resp_obj = self.driver.get_response(url)
        resp = VkResponse.create(resp_obj, LongPollResponse)
        return resp.response

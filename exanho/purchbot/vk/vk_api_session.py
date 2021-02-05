from .drivers import IVkDriver
from .dto import VkResponse
from .dto.groups import GetLongPollServerResponse

URL_VK_API = 'https://api.vk.com/method/'
API_VERSION = '5.126'

class VkApiSession:

    def __init__(self, driver:IVkDriver, access_token:str, v:str=API_VERSION) -> None:
        self.driver = driver
        self.access_token = access_token
        self.v = v
        
    def groups_getLongPollServer(self, group_id:int) -> GetLongPollServerResponse:
        dto = None
        url = '{}{}'.format(URL_VK_API, 'groups.getLongPollServer')
        try:
            resp_obj = self.driver.get_response(url, params={'group_id':group_id, 'v':self.v, 'access_token':self.access_token})
            resp = VkResponse.create(resp_obj, GetLongPollServerResponse)
            dto = resp.response
        except:
            raise

        return dto

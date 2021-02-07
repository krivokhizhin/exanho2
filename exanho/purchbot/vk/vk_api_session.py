from .drivers import IVkDriver
from .dto import VkResponse, OkResponse
from .dto.groups import GetLongPollServerResponse

URL_VK_API = 'https://api.vk.com/method/'
API_VERSION = '5.126'

class VkApiSession:

    def __init__(self, driver:IVkDriver, access_token:str, v:str=API_VERSION) -> None:
        self.driver = driver
        self.access_token = access_token
        self.v = v

    def messages_send(self, **kwargs) -> OkResponse:
        assert isinstance(kwargs, dict)

        kwargs.update({'v':self.v, 'access_token':self.access_token})
        url = '{}{}'.format(URL_VK_API, 'messages.send')
        resp_obj = self.driver.get_response(url, params=kwargs)
        resp:VkResponse = VkResponse.create(resp_obj, OkResponse)
        return resp.response
        
    def groups_getLongPollServer(self, group_id:int) -> GetLongPollServerResponse:
        url = '{}{}'.format(URL_VK_API, 'groups.getLongPollServer')
        resp_obj = self.driver.get_response(url, params={'group_id':group_id, 'v':self.v, 'access_token':self.access_token})
        resp:VkResponse = VkResponse.create(resp_obj, GetLongPollServerResponse)
        return resp.response

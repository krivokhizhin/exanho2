from .drivers import IVkDriver
from .dto import JSONObject, VkResponse, OkResponse
from .dto import util as dto_util
from .dto.groups import GetLongPollServerResponse
from .ui.element_builder import UIElementBuilder
from .dto.messages import *

URL_VK_API = 'https://api.vk.com/method/'
API_VERSION = '5.130'

class VkApiSession:

    def __init__(self, driver:IVkDriver, access_token:str, v:str=API_VERSION) -> None:
        self.driver = driver
        self.access_token = access_token
        self.v = v

    def messages_send(self, content:str) -> SendResponse:
        assert isinstance(content, str)

        json_obj:JSONObject = dto_util.deform(content, JSONObject)
        send_options = SendOptions()
        send_options.fill(json_obj)

        builder = UIElementBuilder()
        builder.build_ui_element(send_options)
        options_dict = builder.items

        options_dict.update({'v':self.v, 'access_token':self.access_token})
        url = '{}{}'.format(URL_VK_API, 'messages.send')
        resp_obj = self.driver.post(url, params=options_dict)
        resp:VkResponse = VkResponse.create(resp_obj, SendResponse)
        return resp.response

    def messages_sendMessageEventAnswer(self, content:str) -> SendResponse:
        assert isinstance(content, str)

        json_obj:JSONObject = dto_util.deform(content, JSONObject)
        send_options = SendMessageEventAnswerOptions()
        send_options.fill(json_obj)

        builder = UIElementBuilder()
        builder.build_ui_element(send_options)
        options_dict = builder.items

        options_dict.update({'v':self.v, 'access_token':self.access_token})
        url = '{}{}'.format(URL_VK_API, 'messages.sendMessageEventAnswer')
        resp_obj = self.driver.post(url, params=options_dict)
        resp:VkResponse = VkResponse.create(resp_obj, SendResponse)
        return resp.response
        
    def groups_getLongPollServer(self, group_id:int) -> GetLongPollServerResponse:
        url = '{}{}'.format(URL_VK_API, 'groups.getLongPollServer')
        resp_obj = self.driver.get(url, params={'group_id':group_id, 'v':self.v, 'access_token':self.access_token})
        resp:VkResponse = VkResponse.create(resp_obj, GetLongPollServerResponse)
        return resp.response

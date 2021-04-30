from exanho.purchbot.vk.ui import payload
import logging
import io
from multiprocessing import shared_memory

from exanho.core.common import Error

from .drivers import IVkDriver
from .dto import JSONObject, VkResponse, OkResponse, IVkDto
from ..utils import json64 as json_util
from .dto.groups import GetLongPollServerResponse
from .ui.element_builder import UIElementBuilder
from .dto.messages import *
from .dto.docs import *
from .dto.attachments import *

log = logging.getLogger(__name__)

URL_VK_API = 'https://api.vk.com/method/'
API_VERSION = '5.130'
DEFAULT_METHOD_WEIGHT = 1

class VkApiSession:

    def __init__(self, driver:IVkDriver, access_token:str, v:str=API_VERSION) -> None:
        self.driver = driver
        self.access_token = access_token
        self.v = v
        self.method_weights = {
            'attachment_send': 3
        }

    def method_weight(self, method_name:str) -> int:
        assert isinstance(method_name, str)

        if method_name in self.method_weights:
            return self.method_weights[method_name]
        else:
            return DEFAULT_METHOD_WEIGHT

    def messages_send(self, content:str, **kwargs) -> SendResponse:
        options_dict = None
        if kwargs:
            options_dict = kwargs
        else:
            assert isinstance(content, str)

            json_obj:JSONObject = json_util.deform(content, JSONObject)
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

        json_obj:JSONObject = json_util.deform(content, JSONObject)
        send_options = SendMessageEventAnswerOptions()
        send_options.fill(json_obj)

        builder = UIElementBuilder()
        builder.build_ui_element(send_options)
        options_dict = builder.items

        options_dict.update({'v':self.v, 'access_token':self.access_token})
        url = '{}{}'.format(URL_VK_API, 'messages.sendMessageEventAnswer')
        resp_obj = self.driver.post(url, params=options_dict)
        resp:VkResponse = VkResponse.create(resp_obj, SendResponse)
        log.debug(f'{send_options.event_data}: {json_util.convert_obj_to_json_str(resp.response, IVkDto)}')
        return resp.response
        
    def groups_getLongPollServer(self, group_id:int) -> GetLongPollServerResponse:
        url = '{}{}'.format(URL_VK_API, 'groups.getLongPollServer')
        resp_obj = self.driver.get(url, params={'group_id':group_id, 'v':self.v, 'access_token':self.access_token})
        resp:VkResponse = VkResponse.create(resp_obj, GetLongPollServerResponse)
        return resp.response

    def docs_getMessagesUploadServer(self, content:str, **kwargs) -> GetMessagesUploadServerResponse:
        options_dict = None
        if kwargs:
            options_dict = kwargs
        else:
            assert isinstance(content, str)

            json_obj:JSONObject = json_util.deform(content, JSONObject)
            send_options = GetMessagesUploadServerOptions()
            send_options.fill(json_obj)

            builder = UIElementBuilder()
            builder.build_ui_element(send_options)
            options_dict = builder.items

        options_dict.update({'v':self.v, 'access_token':self.access_token})
        url = '{}{}'.format(URL_VK_API, 'docs.getMessagesUploadServer')
        resp_obj = self.driver.post(url, params=options_dict)
        resp:VkResponse = VkResponse.create(resp_obj, GetMessagesUploadServerResponse)
        return resp.response

    def upload_file(self, shm_name:str, shm_size:int, filename:str, upload_url:str) -> UploadFileResponse:
        resp = None
        shm = shared_memory.SharedMemory(shm_name)
        content_buffer = shm.buf[:shm_size]

        with io.BytesIO(content_buffer.tobytes()) as bd:
            resp_obj = self.driver.upload_file(upload_url, filename=filename, file=bd)
            resp:VkResponse = VkResponse.create(resp_obj, UploadFileResponse)

        content_buffer.release()
        shm.close()
        shm.unlink()

        return resp.response

    def docs_save(self, content:str, **kwargs) -> SaveDocsResponse:
        options_dict = None
        if kwargs:
            options_dict = kwargs
        else:
            assert isinstance(content, str)

            json_obj:JSONObject = json_util.deform(content, JSONObject)
            send_options = SaveDocsOptions()
            send_options.fill(json_obj)

            builder = UIElementBuilder()
            builder.build_ui_element(send_options)
            options_dict = builder.items

        options_dict.update({'v':self.v, 'access_token':self.access_token})
        url = '{}{}'.format(URL_VK_API, 'docs.save')
        resp_obj = self.driver.post(url, params=options_dict)
        resp:VkResponse = VkResponse.create(resp_obj, SaveDocsResponse)
        return resp.response

    def attachment_send(self, content:str):
        assert isinstance(content, str)

        json_obj:JSONObject = json_util.deform(content, JSONObject)
        send_options = SendAttachmentsOptions()
        send_options.fill(json_obj)

        if send_options.type == 'doc':

            # get upload_url
            upload_url_resp = self.docs_getMessagesUploadServer(
                None, # content
                type='doc',
                peer_id=send_options.peer_id
            )
            if upload_url_resp.error:
                raise Error(f'VK docs.getMessagesUploadServer call failed with error: code={upload_url_resp.error.error_code}, msg={upload_url_resp.error.error_msg}')        
            log.debug(json_util.convert_obj_to_json_str(upload_url_resp, IVkDto))

            # upload doc
            upload_file_resp = self.upload_file(
                send_options.shm_name,
                send_options.shm_size,
                send_options.filename,
                upload_url_resp.upload_url
            )
            if upload_file_resp.error:
                raise Error(f'VK upload doc call failed with error: code={upload_file_resp.error.error_code}, msg={upload_file_resp.error.error_msg}')
            log.debug(json_util.convert_obj_to_json_str(upload_file_resp, IVkDto))

            # save doc in user vk-storage
            doc_save_resp = self.docs_save(
                None, # content
                file=upload_file_resp.file,
                title=send_options.filename
            )
            if doc_save_resp.error:
                raise Error(f'VK upload doc call failed with error: code={doc_save_resp.error.error_code}, msg={doc_save_resp.error.error_msg}')
            log.debug(json_util.convert_obj_to_json_str(doc_save_resp, IVkDto))

            # send message with attachment
            doc_dto:DocDto = doc_save_resp.docs[0]
            attachment = 'doc{}_{}'.format(doc_dto.owner_id, doc_dto.id)
            return self.messages_send(
                None, # content
                user_id=send_options.peer_id,
                attachment=attachment,
                group_id=send_options.group_id,
                random_id=send_options.random_id,
                payload=send_options.payload
            )

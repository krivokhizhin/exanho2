import datetime
import unittest

from exanho.purchbot.utils import json64 as json_util

from exanho.purchbot.vk.dto import JSONObject
from exanho.purchbot.vk.events import provider as event_provider
from exanho.purchbot.vk.events.message import PrivateMessage, ClientInfo, MessageNew, MessageReply, MessageEvent

class TestUtils(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass


    def assertEqualPrivateMessage(self, actual:PrivateMessage, expected:PrivateMessage):
        self.assertEqual(actual.id, expected.id)
        self.assertEqual(actual.date, expected.date)
        self.assertEqual(actual.peer_id, expected.peer_id)
        self.assertEqual(actual.from_id, expected.from_id)
        self.assertEqual(actual.text, expected.text)
        self.assertEqual(actual.random_id, expected.random_id)
        self.assertEqual(actual.ref, expected.ref)
        self.assertEqual(actual.ref_source, expected.ref_source)
        self.assertEqual(actual.attachments, expected.attachments)
        self.assertEqual(actual.important, expected.important)
        self.assertEqual(actual.geo, expected.geo)
        self.assertEqual(actual.payload, expected.payload)
        self.assertEqual(actual.keyboard, expected.keyboard)
        self.assertEqual(actual.fwd_messages, expected.fwd_messages)
        self.assertEqual(actual.reply_message, expected.reply_message)
        self.assertEqual(actual.action, expected.action)
        self.assertEqual(actual.admin_author_id, expected.admin_author_id)
        self.assertEqual(actual.conversation_message_id, expected.conversation_message_id)
        self.assertEqual(actual.is_cropped, expected.is_cropped)
        self.assertEqual(actual.members_count, expected.members_count)
        self.assertEqual(actual.update_time, expected.update_time)
        self.assertEqual(actual.was_listened, expected.was_listened)
        self.assertEqual(actual.pinned_at, expected.pinned_at)
        self.assertEqual(actual.message_tag, expected.message_tag)

    def assertEqualClientInfo(self, actual:ClientInfo, expected:ClientInfo):
        self.assertEqual(actual.button_actions, expected.button_actions)
        self.assertEqual(actual.keyboard, expected.keyboard)
        self.assertEqual(actual.inline_keyboard, expected.inline_keyboard)
        self.assertEqual(actual.carousel, expected.carousel)
        self.assertEqual(actual.lang_id, expected.lang_id)

    def assertEqualMessageNew(self, actual:MessageNew, expected:MessageNew):
        
        if expected.message is None:
            self.assertIsNone(actual.message)
        else:
            self.assertIsNotNone(actual.message)
            self.assertEqualPrivateMessage(actual.message, expected.message)
        
        if expected.client_info is None:
            self.assertIsNone(actual.client_info)
        else:
            self.assertIsNotNone(actual.client_info)
            self.assertEqualClientInfo(actual.client_info, expected.client_info)

    def assertEqualMessageEvent(self, actual:MessageEvent, expected:MessageEvent):
        self.assertEqual(actual.user_id, expected.user_id)
        self.assertEqual(actual.peer_id, expected.peer_id)
        self.assertEqual(actual.event_id, expected.event_id)
        self.assertEqual(actual.payload, expected.payload)
        self.assertEqual(actual.conversation_message_id, expected.conversation_message_id)

    def test_get_message_new(self):

        json_str = '{"message": {"date": 1613670509, "from_id": 326596496, "id": 310, "out": 0, "peer_id": 326596496, "text": "Wwww", "conversation_message_id": 295, "important": false, "random_id": 0, "is_hidden": false}, "client_info": {"button_actions": ["text", "vkpay", "open_app", "location", "open_link", "open_photo", "callback", "intent_subscribe", "intent_unsubscribe"], "keyboard": true, "inline_keyboard": true, "carousel": true, "lang_id": 0}}'
        json_obj = json_util.convert_json_str_to_obj(json_str, JSONObject)

        actual = event_provider.get_message_new(json_obj)

        expected = MessageNew()
        expected.message = PrivateMessage()
        expected.message.date = datetime.datetime(2021, 2, 18, 20, 48, 29)
        expected.message.from_id = 326596496
        expected.message.id = 310
        expected.message.peer_id = 326596496
        expected.message.text = 'Wwww'
        expected.message.conversation_message_id = 295
        expected.message.important = False
        expected.message.random_id = 0
        expected.client_info = ClientInfo()
        expected.client_info.button_actions = ["text", "vkpay", "open_app", "location", "open_link", "open_photo", "callback", "intent_subscribe", "intent_unsubscribe"]
        expected.client_info.keyboard = True
        expected.client_info.inline_keyboard = True
        expected.client_info.carousel = True
        expected.client_info.lang_id = 0

        self.assertEqualMessageNew(actual, expected)

    def test_get_message_reply(self):

        json_str = '{"date": 1613670515, "from_id": -202308925, "id": 314, "out": 1, "peer_id": 326596496, "text": "\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0447\u0435\u0440\u0435\u0437 \u043f\u0440\u043e\u0431\u0435\u043b \u0418\u041d\u041d \u0438 \u041a\u041f\u041f (\u043f\u0440\u0438 \u043d\u0430\u043b\u0438\u0447\u0438\u0438) \u0443\u0447\u0430\u0441\u0442\u043d\u0438\u043a\u0430", "conversation_message_id": 299, "important": false, "random_id": 0, "payload": {"command":"detailing_product", "context":3, "page":1}, "is_hidden": false}'
        json_obj = json_util.convert_json_str_to_obj(json_str, JSONObject)

        actual = event_provider.get_message_reply(json_obj)

        expected = MessageReply()
        expected.date = datetime.datetime(2021, 2, 18, 20, 48, 35)
        expected.from_id = -202308925
        expected.id = 314
        expected.peer_id = 326596496
        expected.text = 'Введите через пробел ИНН и КПП (при наличии) участника'
        expected.conversation_message_id = 299
        expected.important = False
        expected.random_id = 0

        self.assertEqualPrivateMessage(actual, expected)

    def test_get_message_event(self):

        json_str = '{"user_id": 140038124, "peer_id": 140038124, "event_id": "0ae26189a432", "payload": {"command": "menu_section_queries"}}'
        json_obj = json_util.convert_json_str_to_obj(json_str, JSONObject)

        actual = event_provider.get_message_event(json_obj)

        expected = MessageEvent()
        expected.user_id = 140038124
        expected.peer_id = 140038124
        expected.event_id = '0ae26189a432'

        self.assertEqualMessageEvent(actual, expected)

import unittest

from exanho.purchbot.utils import json64 as json_util

from exanho.purchbot.vk.dto import JSONObject
from exanho.purchbot.vk.dto.bot import GroupEvent

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


    def assertEqualJSONObject(self, actual:JSONObject, expected:JSONObject):
        self.assertEqual(len(actual.__dict__), len(expected.__dict__))
        expected_attrs = expected.__dict__.keys()
        for attr, value in actual.__dict__.items():
            self.assertIn(attr, expected_attrs)
            if isinstance(value, JSONObject):
                self.assertEqualJSONObject(value, getattr(expected, attr))
            else:
                self.assertEqual(value, getattr(expected, attr))

    def assertEqualGroupEvent(self, actual:GroupEvent, expected:GroupEvent):
        self.assertEqual(actual.type, expected.type)
        self.assertEqualJSONObject(actual.object, expected.object)
        self.assertEqual(actual.group_id, expected.group_id)

    def test_convert_json_str_to_obj(self):

        json_str = '{"type": "group_join", "object": {"user_id": 1, "join_type" : "approved", "dict": {"a1": 1, "a2": 2}, "list": [1,"2",4.7]}, "group_id": 1}'
        json_obj = json_util.convert_json_str_to_obj(json_str, JSONObject)
        actual = GroupEvent()
        actual.fill(json_obj)

        expected_object_obj = JSONObject({"user_id": 1, "join_type" : "approved", "dict": JSONObject({"a1": 1, "a2": 2}), "list": [1,"2",4.7]})
        expected_event_obj = JSONObject({"type": "group_join", "object": expected_object_obj, "group_id": 1})

        expected = GroupEvent()
        expected.fill(expected_event_obj)

        self.assertEqualGroupEvent(actual, expected)

    def test_convert_obj_to_json_str(self):

        message_obj = JSONObject({"date": 1613670509, "from_id": 326596496, "id": 310, "out": 0, "peer_id": 326596496, "text": "Wwww", "conversation_message_id": 295, "important": False, "random_id": 0, "is_hidden": False})
        client_info_obj = JSONObject({"button_actions": ["text", "vkpay", "open_app", "location", "open_link", "open_photo", "callback", "intent_subscribe", "intent_unsubscribe"], "keyboard": True, "inline_keyboard": True, "carousel": True, "lang_id": 0})
        object_obj = JSONObject({"message": message_obj, "client_info": client_info_obj})
        event_obj = JSONObject({"type": "message_new", "object": object_obj, "group_id": 202308925})

        actual_event = GroupEvent()
        actual_event.fill(event_obj)

        actual = json_util.convert_obj_to_json_str(actual_event, GroupEvent, JSONObject)

        expected = '{"type": "message_new", "object": {"message": {"date": 1613670509, "from_id": 326596496, "id": 310, "out": 0, "peer_id": 326596496, "text": "Wwww", "conversation_message_id": 295, "important": false, "random_id": 0, "is_hidden": false}, "client_info": {"button_actions": ["text", "vkpay", "open_app", "location", "open_link", "open_photo", "callback", "intent_subscribe", "intent_unsubscribe"], "keyboard": true, "inline_keyboard": true, "carousel": true, "lang_id": 0}}, "group_id": 202308925}'
        
        self.assertEqual(actual, expected)
from collections import namedtuple

VkApiContext = namedtuple('VkApiContext', [
    'access_token',
    'group_id',
    'vk_session',
    'call_queue',
    'max_calls'
    ], defaults = [None, None, 20])
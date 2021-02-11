from collections import namedtuple

VkApiContext = namedtuple('VkApiContext', [
    'access_token',
    'group_id',
    'vk_api_session'
    ], defaults = [None])
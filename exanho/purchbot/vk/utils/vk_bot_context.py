from collections import namedtuple

VkBotContext = namedtuple('VkBotContext', [
    'access_token',
    'group_id',
    'call_queue',
    'participant_service',
    'vk_session'
    ], defaults = [None])
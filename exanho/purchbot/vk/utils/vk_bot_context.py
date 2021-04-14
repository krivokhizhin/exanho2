from collections import namedtuple

VkBotContext = namedtuple('VkBotContext', [
    'group_id',
    'call_queue',
    'participant_service'
    ])
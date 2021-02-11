from collections import namedtuple

ClientContext = namedtuple('ClientContext', [
    'client',
    'vk_user_id',
    'free_balance',
    'promo_balance',
    ], defaults = [0, 0])
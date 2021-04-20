from collections import namedtuple

ClientContext = namedtuple('ClientContext', [
    'client_id',
    'vk_user_id',
    'free_balance',
    'promo_balance',
    ], defaults = [None, 0, 0])
from xmlrpc.client import ServerProxy
from exanho.orm.domain import Domain
from ..model import *
from ..vk.utils import VkBotContext

from . import show, fix

def run():

    # host = 'localhost'
    # port = 3120
    # part_uri = f'http://{host}:{port}/RPC2'

    # vk_context = VkBotContext(
    #     access_token=None,
    #     group_id=None,
    #     call_queue=None,
    #     participant_service=ServerProxy(part_uri, allow_none=True, use_builtin_types=True),
    #     vk_session=None
    # )

    d = Domain('postgresql+psycopg2://kks:Nata1311@localhost/purchbot_test')
    with d.session_scope() as session:
        
        print('Состояние счетов оператора:')
        show.accumulated_accounts(session, show_promo=True)
        print('Состояние счетов клиентов:')
        show.client_accounts(session, show_promo=True)
        print('Остатки на транзитных счетах:')
        show.transit_account_remains(session, show_promo=True)
        print('Незавершенные заказы:')
        show.during_trades(session)
        # print('Проводки по заказу:')
        # show.acc_record_by_trade(session, 35, show_promo=True)

        # fix.set_trade_status_wo_conditions(session, 23, TradeStatus.DURING, TradeStatus.COMPLETED)

        # fix.manual_trade_executed(session, 35)
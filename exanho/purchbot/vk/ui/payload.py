import enum
import json

class PayloadCommand(enum.Enum):
    start = 0
    empty = 1
    go_to_page = 2
    menu_section_queries = 3
    menu_section_subscriptions = 4
    menu_section_reports = 5
    get_balance = 6
    menu_section_my_subscriptions = 7
    menu_section_history = 8
    request_product = 9
    detailing_trade = 10
    selection_add_info = 11
    confirm_trade = 12
    edit_trade = 13
    cancel_trade = 14
    trade_executed = 15

class Payload:

    def __init__(self, **kwargs) -> None:
        self.command = kwargs.get('command', None)
        self.product = kwargs.get('product', None)
        self.page = kwargs.get('page', None)
        self.trade = kwargs.get('trade', None)
        self.add_info = kwargs.get('add_info', None)
        self.par_number = kwargs.get('par_number', None)
        self.par_value = kwargs.get('par_value', None)
        self.content = kwargs.get('content', None)
        self.go_to = kwargs.get('go_to', None)

    def form(self) -> str:
        dic = dict([(key, value if not isinstance(value, PayloadCommand) else value.name) for key, value in self.__dict__.items() if value])        
        if len(dic) == 0:
            return None
        json_str = json.dumps(dic)
        return json_str.replace('"', '\"')

    def fill(self, command, **kwargs):
        if command:
            try:
                self.command = PayloadCommand[command]
            except:
                pass

        self.product = kwargs.get('product', None)
        self.page = kwargs.get('page', None)
        self.trade = kwargs.get('trade', None)
        self.add_info = kwargs.get('add_info', None)
        self.par_number = kwargs.get('par_number', None)
        self.par_value = kwargs.get('par_value', None)
        self.content = kwargs.get('content', None)
        self.go_to = kwargs.get('go_to', None)

    def __str__(self) -> str:
        return 'Payload: {}'.format(', '.join([f'{key}={value}' for key, value in self.__dict__.items()]))
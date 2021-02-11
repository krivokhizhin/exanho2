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

class Payload:

    def __init__(self, **kwargs) -> None:
        self.command = kwargs.get('command', None)
        self.context = kwargs.get('context', None)
        self.page = kwargs.get('page', None)

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

        self.context = kwargs.get('context', None)
        self.page = kwargs.get('page', None)
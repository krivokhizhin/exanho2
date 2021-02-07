import json
from collections import defaultdict

main_menu_name = 'main_menu'
main_menu_buttons_name = 'buttons'

class UiTemplates:

    def __init__(self, path:str) -> None:
        self.path = path.rstrip('/')
        self.ui_elements = defaultdict(dict) # main_menu = None

    def init_element(self, name:str):
        with open(self.path+'/'+name+'.json', 'r') as f:
            self.ui_elements[name] = json.load(f)

    def get_element(self, name:str) -> str:
        if name in self.ui_elements:
            return json.dumps(self.ui_elements[name])
        else:
            return None

    def set_balance_in_main_menu(self, balance:int, name=main_menu_name):
        buttons = self.ui_elements[name].get(main_menu_buttons_name)
        if buttons:
            buttons[1][0]['action']['label'] = balance # !!! HARD COD !!!
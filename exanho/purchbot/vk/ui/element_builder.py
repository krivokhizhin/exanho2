import json
import enum

from . import IContext, Payload

class UIElementBuilder:

    def __init__(self) -> None:
        self.items = dict()

    def inner_build_ui_element(self, content):
        dic = {}
        for key, value in content.__dict__.items():

            if isinstance(value, Payload):
                value = value.form()
                
            if not value and value != 0:
                continue

            key = str(key).strip('_')

            if issubclass(type(value), enum.Enum):
                value = value.name

            if isinstance(value, IContext):
                dic[key] = self.inner_build_ui_element(value)
            elif isinstance(value, list):
                dic[key] = self.prepare_list_to_build(value)
            else:
                dic[key] = value
        return dic

    def build_ui_element(self, content):
        self.items = self.inner_build_ui_element(content)

    def form(self)-> str:
        return json.dumps(self.items)

    def prepare_list_to_build(self, list_value:list) -> list:
        result = list()

        for item in list_value:
            if item:
                if isinstance(item, IContext):
                    result.append(self.inner_build_ui_element(item))
                elif isinstance(item, list):
                    result.append(self.prepare_list_to_build(item))
                else:
                    result.append(item)

        return result
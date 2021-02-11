import json
import enum

from .element_content import IContext
from .payload import Payload

class UIElementBuilder:

    def __init__(self) -> None:
        self.items = dict()

    def inner_build_ui_element(self, content):
        dic = {}
        for key, value in content.__dict__.items():

            if isinstance(value, Payload):
                value = value.form()
                
            if value is None:
                continue

            key = str(key).strip('_')

            if issubclass(type(value), enum.Enum):
                value = value.name

            if isinstance(value, IContext):
                dic[key] = self.inner_build_ui_element(value)
            elif isinstance(value, list):
                dic.setdefault(key, list())
                for item in value:
                    if isinstance(item, IContext):
                        dic[key].append(self.inner_build_ui_element(item))
                    elif isinstance(value, list):
                        inner_list = list()
                        for inner_item in item:
                            if isinstance(inner_item, IContext):
                                inner_list.append(self.inner_build_ui_element(inner_item))
                            elif isinstance(value, list):
                                raise NotImplementedError()
                            else:
                                inner_list.append(inner_item)
                        dic[key].append(inner_list)
                    else:
                        dic[key].append(item)
            else:
                dic[key] = value
        return dic

    def build_ui_element(self, content):
        self.items = self.inner_build_ui_element(content)

    def form(self)-> str:
        return json.dumps(self.items)

from exanho.purchbot.vk.ui.payload import Payload
from ..element_content import ButtonColor, ButtonType, ButtonActionContent, ButtonContent, TemplateElementContent, TemplateType, TemplateContent

class ProductList:

    def __init__(self) -> None:
        self.content = TemplateContent(
            type_ = TemplateType.carousel
        )

    def add_product(self, title:str, desc:str, btn_label:str, payload:Payload):
        self.content.elements.append(
            TemplateElementContent(
                title = title,
                description = desc,
                buttons = [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = btn_label,
                            payload = payload
                        ),
                        color = ButtonColor.primary
                    )
                ]
            )
        )
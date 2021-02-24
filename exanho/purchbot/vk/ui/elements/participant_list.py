
from exanho.purchbot.vk.ui.payload import Payload
from ..element_content import ButtonColor, ButtonType, ButtonActionContent, ButtonContent, TemplateElementContent, TemplateType, TemplateContent

MAX_LEN_TEMPLATE_TITLE = 80
MAX_LEN_TEMPLATE_DESC = 80

class ParticipantList:

    def __init__(self) -> None:
        self.content = TemplateContent(
            type_ = TemplateType.carousel
        )

    def add_participant(self, title:str, desc:str, btn_label:str, payload:Payload):
        if len(title) > MAX_LEN_TEMPLATE_TITLE:
            title = '{}..'.format(title[:MAX_LEN_TEMPLATE_TITLE-2])
        if len(desc) > MAX_LEN_TEMPLATE_DESC:
            desc = '{}..'.format(title[:MAX_LEN_TEMPLATE_DESC-2])
            
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
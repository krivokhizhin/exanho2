from ..element_content import ButtonColor, ButtonType, ButtonActionContent, ButtonContent, KeyboardContent
from ..payload import PayloadCommand, Payload

class ParticipantEvent:

    def __init__(self) -> None:
        self.content = KeyboardContent(
            buttons = [
                [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.open_link,
                            label = 'Открыть в ЕИС'
                        )
                    )
                ],
                [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = 'Запросить активность'
                        ),
                        color = ButtonColor.primary
                    )
                ],
                [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = 'Получить отчет'
                        ),
                        color = ButtonColor.primary
                    )
                ]
            ],
            inline = True
        )

    def fill_event(self, eis_href:str):
        self.content.buttons[0][0].action.link = eis_href
        self.content.buttons[0][0].action.payload = Payload(command = PayloadCommand.empty).form()
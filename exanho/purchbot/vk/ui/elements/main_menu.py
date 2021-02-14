from decimal import Decimal

from ..element_content import ButtonColor, ButtonType, ButtonActionContent, ButtonContent, KeyboardContent
from ..payload import PayloadCommand, Payload

class MainMenu:

    def __init__(self) -> None:
        self.content = KeyboardContent(
            one_time = False,
            buttons = [
                [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = '<<',
                            payload = '{\"command\":\"empty\"}'
                        ),
                        color = ButtonColor.secondary
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = '<',
                            payload = '{\"command\":\"empty\"}'
                        ),
                        color = ButtonColor.secondary
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = '.',
                            payload = '{\"command\":\"empty\"}'
                        ),
                        color = ButtonColor.secondary
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = '>',
                            payload = '{\"command\":\"empty\"}'
                        ),
                        color = ButtonColor.secondary
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = '>>',
                            payload = '{\"command\":\"empty\"}'
                        ),
                        color = ButtonColor.secondary
                    )
                ],
                [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = 'Запросы',
                            payload = Payload(command = PayloadCommand.menu_section_queries).form()
                        ),
                        color = ButtonColor.primary
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = 'Подписки',
                            payload = Payload(command = PayloadCommand.menu_section_subscriptions).form()
                        ),
                        color = ButtonColor.primary
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = 'Отчеты',
                            payload = Payload(command = PayloadCommand.menu_section_reports).form()
                        ),
                        color = ButtonColor.primary
                    )
                ],
                [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.text,
                            label = '0 (0)',
                            payload = '{\"command\":\"get_balance\"}'
                        ),
                        color = ButtonColor.secondary
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.text,
                            label = 'Мои подписки',
                            payload = '{\"command\":\"menu_section_my_subscriptions\"}'
                        ),
                        color = ButtonColor.secondary
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.text,
                            label = 'История',
                            payload = '{\"command\":\"menu_section_history\"}'
                        ),
                        color = ButtonColor.secondary
                    )
                ],
                [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.vkpay,
                            hash = 'action=transfer-to-group&group_id=202308925&aid=10'
                        )
                    )
                ]
            ]
        )

    def set_payload_for_first_btn(self, payload:Payload):
        self.content.buttons[0][0].action.payload = payload

    def set_payload_for_prev_btn(self, payload:Payload):
        self.content.buttons[0][1].action.payload = payload

    def set_label_for_page_btn(self, label:str):
        self.content.buttons[0][2].action.label = label

    def set_payload_for_next_btn(self, payload:Payload):
        self.content.buttons[0][3].action.payload = payload

    def set_payload_for_last_btn(self, payload:Payload):
        self.content.buttons[0][4].action.payload = payload

    def set_label_for_balance(self, free:Decimal, promo:Decimal):
        label = '{:.0f}'.format(free) + ' ({:.0f})'.format(promo) if promo > 0 else ''
        self.content.buttons[2][0].action.label = label
from ..element_content import ButtonColor, ButtonType, ButtonActionContent, ButtonContent, KeyboardContent
from ..payload import PayloadCommand, Payload

class ConfirmOrder:

    def __init__(self) -> None:
        self.content = KeyboardContent(
            buttons = [
                [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.vkpay,
                            hash = 'action=transfer-to-group&group_id=202308925&aid=10'
                        )
                    )
                ],
                [
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = 'Подтвердить'
                        ),
                        color = ButtonColor.positive
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = 'Редактировать'
                        ),
                        color = ButtonColor.secondary
                    ),
                    ButtonContent(
                        action = ButtonActionContent(
                            type_ = ButtonType.callback,
                            label = 'Отмена'
                        ),
                        color = ButtonColor.negative
                    )
                ]
            ],
            inline = True
        )

    def set_order(self, order_id:int):
        self.content.buttons[1][0].action.payload = Payload(command = PayloadCommand.confirm_order, order=order_id).form()
        self.content.buttons[1][1].action.payload = Payload(command = PayloadCommand.edit_order, order=order_id).form()
        self.content.buttons[1][2].action.payload = Payload(command = PayloadCommand.cancel_order, order=order_id).form()
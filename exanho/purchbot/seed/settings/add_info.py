from sqlalchemy.orm.session import Session as OrmSession

from exanho.purchbot.model import AddInfoCode, AddInfoSettings

def seed(session:OrmSession):

    add_info1 = session.query(AddInfoSettings).filter(AddInfoSettings.code == AddInfoCode.PARTICIPANT).one_or_none()
    if add_info1 is None:
        add_info1 = AddInfoSettings(
            code = AddInfoCode.PARTICIPANT,
            name = 'ID участника закупок',
            ui_prompt = 'Введите через пробел ИНН и КПП (при наличии) участника'
        )
        session.add(add_info1)

    add_info2 = session.query(AddInfoSettings).filter(AddInfoSettings.code == AddInfoCode.CUSTOMER).one_or_none()
    if add_info2 is None:
        add_info2 = AddInfoSettings(
            code = AddInfoCode.CUSTOMER,
            name = 'ID заказчика закупок',
            ui_prompt = 'Введите через пробел ИНН и КПП заказчика'
        )
        session.add(add_info2)

    add_info1 = session.query(AddInfoSettings).filter(AddInfoSettings.code == AddInfoCode.PARTICIPANT).one_or_none()
    if add_info1 is None:
        add_info1 = AddInfoSettings(
            code = AddInfoCode.NOTIFICATION,
            name = 'Код закупки',
            ui_prompt = 'Введите код закупки'
        )
        session.add(add_info1)

    add_info1 = session.query(AddInfoSettings).filter(AddInfoSettings.code == AddInfoCode.PARTICIPANT).one_or_none()
    if add_info1 is None:
        add_info1 = AddInfoSettings(
            code = AddInfoCode.CONTRACT,
            name = 'Реестровый номер контракта',
            ui_prompt = 'Введите реестровый номер контракта'
        )
        session.add(add_info1)

    session.flush()
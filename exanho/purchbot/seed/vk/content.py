from sqlalchemy.orm.session import Session as OrmSession

from exanho.purchbot.model import VkDialogContent, AddInfoCode

def _seed_content(session:OrmSession, group:str, topic:str, content:str):

    vk_content = session.query(VkDialogContent).filter(VkDialogContent.topic == topic, VkDialogContent.group == group).one_or_none()
    if vk_content is None:
        vk_content = VkDialogContent(
            topic = topic,
            group = group,
            content = content
        )
        session.add(vk_content)

def seed(session:OrmSession):

    _seed_content(session, 'QUE_PAR_ACT', 'list_desc', 'Потребуется указать ИНН и КПП (при наличии) участника')
    _seed_content(session, 'QUE_PAR_ACT', 'list_button', 'Запросить')

    _seed_content(session, 'QUE_PAR_HIS', 'list_desc', 'Потребуется указать ИНН и КПП (при наличии) участника')
    _seed_content(session, 'QUE_PAR_HIS', 'list_button', 'Запросить')

    _seed_content(session, 'REP_PAR_ACT', 'list_desc', 'Потребуется указать ИНН и КПП (при наличии) участника')
    _seed_content(session, 'REP_PAR_ACT', 'list_button', 'Получить')

    _seed_content(session, 'REP_PAR_HIS', 'list_desc', 'Потребуется указать ИНН и КПП (при наличии) участника')
    _seed_content(session, 'REP_PAR_HIS', 'list_button', 'Получить')

    _seed_content(session, 'REP_PARS_CON', 'list_desc', '+ учет незавершенных контрактов')
    _seed_content(session, 'REP_PARS_CON', 'list_button', 'Получить')

    _seed_content(session, 'SUB_PAR', 'list_desc', 'Потребуется указать ИНН и КПП (при наличии) участника')
    _seed_content(session, 'SUB_PAR', 'list_button', 'Подписаться')


    _seed_content(session, AddInfoCode.__name__, AddInfoCode.PARTICIPANT.name, 'Введите через пробел ИНН и КПП (при наличии) участника')
    _seed_content(session, AddInfoCode.__name__, AddInfoCode.CUSTOMER.name, 'Введите через пробел ИНН и КПП заказчика')
    _seed_content(session, AddInfoCode.__name__, AddInfoCode.NOTIFICATION.name, 'Введите код закупки')
    _seed_content(session, AddInfoCode.__name__, AddInfoCode.CONTRACT.name, 'Введите реестровый номер контракта')
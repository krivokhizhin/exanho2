# from sqlalchemy.orm.session import Session as OrmSession
# from exanho.orm.domain import Domain

# from exanho.purchbot.model import VkContent

# def run():

#     d = Domain('postgresql+psycopg2://kks:Nata1311@localhost/purchbot_test')
#     with d.session_scope() as session:
#         assert isinstance(session, OrmSession)

#         vk_content1 = session.query(VkContent).filter(VkContent.key == 'query_product_list_message').one_or_none()
#         if vk_content1 is None:
#             vk_content1 = VkContent(
#                 key = 'query_product_list_message',
#                 value = 'Запросы:'
#             )
#             session.add(vk_content1)

#         vk_content2 = session.query(VkContent).filter(VkContent.key == 'sub_product_list_message').one_or_none()
#         if vk_content2 is None:
#             vk_content2 = VkContent(
#                 key = 'sub_product_list_message',
#                 value = 'Подписки:'
#             )
#             session.add(vk_content2)

#         vk_content3 = session.query(VkContent).filter(VkContent.key == 'report_product_list_message').one_or_none()
#         if vk_content3 is None:
#             vk_content3 = VkContent(
#                 key = 'report_product_list_message',
#                 value = 'Отчеты:'
#             )
#             session.add(vk_content3)

#         vk_content4 = session.query(VkContent).filter(VkContent.key == 'query_product_list_message').one_or_none()
#         if vk_content4 is None:
#             vk_content4 = VkContent(
#                 key = 'query_product_list_hint',
#                 value = 'Для выбора нажмите соответствующую кнопку'
#             )
#             session.add(vk_content4)
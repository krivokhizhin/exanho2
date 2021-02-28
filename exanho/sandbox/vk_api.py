import csv
import io
from multiprocessing import shared_memory
from xmlrpc.client import ServerProxy
import pickle

from exanho.eis44.interfaces import ContractInfo

from exanho.purchbot.vk.dto.json_object import JSONObject
from exanho.purchbot.vk.drivers import BuildInDriver, RequestsDriver
from exanho.purchbot.vk.dto import util as dto_util
from exanho.purchbot.vk import VkApiSession
from exanho.purchbot.vk.dto.docs import *
from exanho.purchbot.vk.dto.messages import *
from exanho.purchbot.vk.dto.attachments import *

URL_VK_API = 'https://api.vk.com/method/'
API_VERSION = '5.130'

access_token = ''
group_id = 202308925
file_path = '/home/kks/projects/purchbot/rep_par_act_RRR_YYYYMMDD.csv'
filename = 'rep_par_act_EEE_YYYYMMDD.csv'

def run():

    host, port, path = 'localhost', 3120, 'RPC2'
    uri = f'http://{host}:{port}/{path}'

    rpc_client = ServerProxy(uri, allow_none=True, use_builtin_types=True)
    print(pickle.loads(rpc_client.get_participant_list('2312054894', '010543001', 1, 10)))
    report:list = pickle.loads(rpc_client.get_current_activity_report(72))
    print(report)

    shm_name = None
    shm_size = None

    with io.StringIO() as buffer:
        fieldnames = ['N', 'reg_num', 'state', 'publish_dt', 'subject', 'price', 'currency_code', 'right_to_conclude', 'start_date', 'end_date', 'supplier_number', 'href']
        writer = csv.DictWriter(buffer, fieldnames=fieldnames,  dialect=csv.excel)
        writer.writeheader()

        sort_number = 0

        for exec_cntr in report:
            assert isinstance(exec_cntr, ContractInfo)
            sort_number += 1
            writer.writerow({
                'N': sort_number,
                'reg_num': f'\'{exec_cntr.reg_num}',
                'state': exec_cntr.state,
                'publish_dt': exec_cntr.publish_dt,
                'subject': exec_cntr.subject,
                'price': exec_cntr.price,
                'currency_code': exec_cntr.currency_code,
                'right_to_conclude': exec_cntr.right_to_conclude,
                'start_date': exec_cntr.start_date,
                'end_date': exec_cntr.end_date,
                'supplier_number': exec_cntr.supplier_number,
                'href': exec_cntr.href
            })

        content = buffer.getvalue().encode(encoding='utf-8')
        shm_size = len(content)

        shm_a = shared_memory.SharedMemory(create=True, size=shm_size)
        shm_name = shm_a.name
        shm_a.buf[:shm_size] = content
        shm_a.close()


    # shm_b = shared_memory.SharedMemory(shm_name)
    # content_buffer = shm_b.buf[:shm_size]

    # with io.BytesIO(content_buffer.tobytes()) as bd:
    # with io.FileIO(file_path, mode='w') as fd:
    #     fd.write(content_buffer.tobytes())

    driver = RequestsDriver()
    vk_api_session = VkApiSession(driver, access_token)

    options = SendAttachmentsOptions(
        shm_name = shm_name,
        shm_size = shm_size,
        filename = filename,
        peer_id = 326596496,
        type = 'doc',
        group_id = group_id,
        random_id = 0
    )

    resp = vk_api_session.attachment_send(dto_util.form(options, SendAttachmentsOptions))

    # upload_url_options = GetMessagesUploadServerOptions(
    #     type='doc',
    #     peer_id=326596496
    # )
    # resp1 = vk_api_session.docs_getMessagesUploadServer(dto_util.form(upload_url_options, GetMessagesUploadServerOptions))

    # url = '{}{}'.format(URL_VK_API, 'docs.getMessagesUploadServer')
    # params = {'type': 'doc', 'peer_id': 326596496, 'v': API_VERSION, 'access_token': access_token}
    # resp = driver.post(url, params=params)
    # resp_obj = dto_util.convert_json_str_to_obj(resp, JSONObject)
    # print(resp_obj.response.upload_url)


    # resp2 = vk_api_session.upload_file(shm_name, shm_size, filename, resp1.upload_url)

    # with io.BytesIO(content_buffer.tobytes()) as bd: # open(file_path, 'rb') as f:
    #     resp = driver.upload_file(resp_obj.response.upload_url, filename=filename, file=bd)
    # resp_obj = dto_util.convert_json_str_to_obj(resp, JSONObject)
    # print(resp_obj.file)


    # docs_save_options = DocsSaveOptions(
    #     file=resp2.file,
    #     title=filename
    # )
    # resp3 = vk_api_session.docs_save(dto_util.form(docs_save_options, DocsSaveOptions))

    # url = '{}{}'.format(URL_VK_API, 'docs.save')
    # params = {'file': resp_obj.file, 'title': filename, 'tags': filename, 'v': API_VERSION, 'access_token': access_token}
    # resp = driver.post(url, params=params)
    # resp_obj = dto_util.convert_json_str_to_obj(resp, JSONObject)
    # attachment = 'doc{}_{}'.format(resp_obj.response.doc.owner_id, resp_obj.response.doc.id)
    # print(attachment)

    # doc_dto:DocDto = resp3.docs[0]
    # attachment = 'doc{}_{}'.format(doc_dto.owner_id, doc_dto.id)

    # send_options = SendOptions(
    #     user_id=326596496,
    #     attachment=attachment,
    #     group_id=group_id,
    #     random_id=0
    # )

    # resp4 = vk_api_session.messages_send(dto_util.form(send_options, SendOptions))

    # url = '{}{}'.format(URL_VK_API, 'messages.send')
    # params = {'user_id': 326596496, 'attachment': attachment, 'group_id': group_id, 'random_id': 0, 'v': API_VERSION, 'access_token': access_token}
    # resp = driver.post(url, params=params)
    # print(resp)

    # content_buffer.release()
    # shm_b.close()
    # shm_b.unlink()
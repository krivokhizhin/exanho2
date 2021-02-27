

from exanho.purchbot.vk.dto.json_object import JSONObject
from exanho.purchbot.vk.drivers import BuildInDriver, RequestsDriver
from exanho.purchbot.vk.dto import util as dto_util
from exanho.purchbot.vk import VkApiSession

URL_VK_API = 'https://api.vk.com/method/'
API_VERSION = '5.130'

access_token = '79f8b669b1d60157a7295fab4d9fa6942d93bdef8edd0e6bb124d351ad738c8fa7e28cf2adb0d3599135d'
group_id = 202308925
file_path = '/home/kks/projects/purchbot/rep_par_act_NNN_YYYYMMDD.csv'
filename = 'rep_par_act_NNN_YYYYMMDD.csv'

def run():
    driver = RequestsDriver()
    # vk_api_session = VkApiSession(driver, access_token)

    url = '{}{}'.format(URL_VK_API, 'docs.getMessagesUploadServer')
    params = {'type': 'doc', 'peer_id': 326596496, 'v': API_VERSION, 'access_token': access_token}
    resp = driver.post(url, params=params)
    resp_obj = dto_util.convert_json_str_to_obj(resp, JSONObject)
    print(resp_obj.response.upload_url)


    with open(file_path, 'rb') as f:
        resp = driver.upload_file(resp_obj.response.upload_url, filename=filename, file=f)
    resp_obj = dto_util.convert_json_str_to_obj(resp, JSONObject)
    print(resp_obj.file)


    url = '{}{}'.format(URL_VK_API, 'docs.save')
    params = {'file': resp_obj.file, 'title': filename, 'tags': filename, 'v': API_VERSION, 'access_token': access_token}
    resp = driver.post(url, params=params)
    resp_obj = dto_util.convert_json_str_to_obj(resp, JSONObject)
    attachment = 'doc{}_{}'.format(resp_obj.response.doc.owner_id, resp_obj.response.doc.id)
    print(attachment)


    url = '{}{}'.format(URL_VK_API, 'messages.send')
    params = {'user_id': 326596496, 'attachment': attachment, 'group_id': group_id, 'random_id': 0, 'v': API_VERSION, 'access_token': access_token}
    resp = driver.post(url, params=params)
    print(resp)
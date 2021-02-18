from xmlrpc.client import ServerProxy
import pickle

from exanho.eis44.interfaces.namedtuple_dto import *

def run():
    host, port, path = 'localhost', 3120, 'RPC2'
    uri = f'http://{host}:{port}/{path}'

    try:
        rpc_client = ServerProxy(uri, allow_none=True, use_builtin_types=True)
        print(pickle.loads(rpc_client.get_participants('7713056834')))
        print(pickle.loads(rpc_client.get_current_activity(2573)))
        print(pickle.loads(rpc_client.get_experience(2573)))
        # print(pickle.loads(rpc_client.get_summary_contracts('0105069779', '010501001')))
        # print(pickle.loads(rpc_client.get_summary_contracts('*', '*')))
        # print(pickle.loads(rpc_client.get_contracts('0105069779', {'state':'DISCONTINUED'})))#, '010501001', 'DISCONTINUED')))
    except Exception as ex:
        print(ex)

    print("!!!!!!!!!!!!!!!")

if __name__ == "__main__":
    run()
    # host, port, path = sys.argv[1:4]
    # uri = f'http://{host}:{port}/{path}'

    # try:
    #     manager = ServerProxy(uri)
    #     print(manager.get_config())
    #     print(manager.get_actor_list())
    # except Exception as ex:
    #     print(ex)
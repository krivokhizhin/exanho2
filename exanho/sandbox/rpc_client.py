import sys
from xmlrpc.client import ServerProxy

if __name__ == "__main__":
    host, port, path = sys.argv[1:4]
    uri = f'http://{host}:{port}/{path}'

    try:
        manager = ServerProxy(uri)
        print(manager.get_config())
        print(manager.get_actor_list())
    except Exception as ex:
        print(ex)
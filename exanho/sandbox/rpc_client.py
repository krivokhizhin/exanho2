import sys
from xmlrpc.client import ServerProxy

if __name__ == "__main__":
    host, port, path = sys.argv[1:4]
    # uri = f'http://{host}:{port}/{path}'
    uri = f'http://{host}:{port}'

    data = 'pycades in single component'
    print(data)

    try:
        manager = ServerProxy(uri)
        print(manager.hash_gost_2012_512(data.encode()))
        print(manager.hash_gost_2012_256(data.encode()))
        print(manager.hash_gost_3411(data.encode()))
    except Exception as ex:
        print(ex)
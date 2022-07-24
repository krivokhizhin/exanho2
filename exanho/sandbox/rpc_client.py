import sys
from xmlrpc.client import ServerProxy

if __name__ == "__main__":
    host, port, port2 = '192.168.0.52', 3121, 3120 #sys.argv[1:4]
    # uri = f'http://{host}:{port}/{path}'
    uri = f'http://{host}:{port}'
    print(uri)

    with open('/home/kks/Документы/АСТГОЗ/223/data_xml.txt', 'r') as f:
        data = f.read()
    print(data)

    try:
        manager = ServerProxy(uri)
        # print('hash_gost_2012_512', manager.hash_gost_2012_512(data.encode()))
        # print('hash_gost_2012_256', manager.hash_gost_2012_256(data.encode()))
        # print('hash_gost_3411', manager.hash_gost_3411(data.encode()))
        
        sign = manager.sign(data, '2B81AAE4A2AD41DFF3A95A5BB7A13B04502A2437', 'BASE64')

    except Exception as ex:
        print(ex)

    uri2 = f'http://{host}:{port2}'
    print(uri2)
    try:
        manager2 = ServerProxy(uri2)
        # print('hash_gost_2012_512', manager.hash_gost_2012_512(data.encode()))
        # print('hash_gost_2012_256', manager.hash_gost_2012_256(data.encode()))
        # print('hash_gost_3411', manager.hash_gost_3411(data.encode()))
        
        print(manager2.by_content_sign(data, sign, 'BASE64'))

    except Exception as ex:
        print(ex)

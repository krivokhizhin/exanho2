from sqlalchemy.orm.session import Session as OrmSession
import csv
from datetime import datetime
import io
import json
from multiprocessing import JoinableQueue, shared_memory

from exanho.core.common import meminfo, get_used_memory_level
from exanho.purchbot.utils import order_manager as order_mngr

INDICATOR_LEN = 10
CHUNK_SIZE = 4092

def convert_rpc_data(*args, **kwargs):
    data = json.dumps((args, kwargs)).encode("ascii")
    data = len(data).to_bytes(INDICATOR_LEN, byteorder='big') + data
    return data

def receive_rpc_data(data):
    msglen = int.from_bytes(data[:INDICATOR_LEN], byteorder='big')

    chunks = []
    bytes_recd = 0
    while bytes_recd < msglen:
        chunk = data[INDICATOR_LEN : ]
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)

    return json.loads(b''.join(chunks)) # func_name, args, kwargs for request

def test_byte_work():
    args = ['config', 'log_queue']
    kwargs = {}
    data = convert_rpc_data('func_name', *args, **kwargs)
    print(data)

    args, kwargs = receive_rpc_data(data)
    func_name, *args = args
    print(func_name)
    print(args)
    print(kwargs)

def csv_work(session:OrmSession):
    
    shm_name = None
    shm_size = None
    tmst = datetime.today().strftime('%Y%m%d%H%M%S')
    filename = f'/home/kks/history_{tmst}.csv'

    with io.StringIO() as buffer:
        fieldnames = ['N', 'ID', u'Дата', u'Продукт', u'Стоимость', u'Контекст']
        # [u'N', u'ID', u'Дата', u'Продукт', u'Стоимость', u'Контекст']
        # map(lambda x: x.encode('cp1251'), [u'N', u'ID', u'Дата', u'Продукт', u'Стоимость', u'Контекст'])
        writer = csv.DictWriter(buffer, fieldnames=fieldnames, dialect=csv.excel)
        writer.writeheader()

        # writer = csv.writer(wrapper, dialect=csv.excel)
        # writer.writerow(map(lambda x: x.encode('cp1251'), [u'N', u'ID', u'Дата', u'Продукт', u'Стоимость', u'Контекст']))

        sort_number = 0

        for order_id, order_updated_at, order_product, order_amount in order_mngr.get_orders_by_client(session, 2):
            sort_number += 1
            writer.writerow({
                'N': sort_number,
                'ID': order_id,
                'Дата': order_updated_at,
                'Продукт': order_product,
                'Стоимость': order_amount,
                'Контекст': '<пусто>'
            })
            # writer.writerow([
            #     sort_number,
            #     order_id,
            #     order_updated_at,
            #     order_product.encode('cp1251'),
            #     order_amount,
            #     '<пусто>'.encode('cp1251')
            # ])
        
        # wrapper = io.TextIOWrapper(io.BufferedReader(buffer), encoding='utf-8')
        # wrapper.reconfigure(encoding='cp1251')

        content = buffer.getvalue().encode(encoding='utf-8')
        shm_size = len(content)

        print(f'{shm_size}: {content}')
        print('=================================================================')

        shm_a = shared_memory.SharedMemory(create=True, size=shm_size)
        shm_name = shm_a.name
        shm_a.buf[:shm_size] = content
        shm_a.close()

        shm_b = shared_memory.SharedMemory(shm_name)
        content_buffer = shm_b.buf[:shm_size]
        data = content_buffer.tobytes()
        print(data)
        with open(filename, 'wb') as f:
            f.write(data)

        content_buffer.release()
        shm_b.close()
        shm_b.unlink()

def read_file():
    with open('/home/kks/history_20210429163348.csv', 'rb') as f:
        print(f.read())
    


def run():

    # mi = meminfo()
    # print(get_used_memory_level())
    # print(get_used_memory_level(True))

    read_file()


    # import exanho.orm.domain as domain
    # d = domain.Domain('postgresql+psycopg2://kks:Nata1311@localhost/purchbot_test')
    # with d.session_scope() as session:
    #     assert isinstance(session, OrmSession)
    #     csv_work(session)

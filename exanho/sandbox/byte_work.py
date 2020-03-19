import json

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

if __name__ == "__main__":
    args = ['config', 'log_queue']
    kwargs = {}
    data = convert_rpc_data('func_name', *args, **kwargs)
    print(data)

    args, kwargs = receive_rpc_data(data)
    func_name, *args = args
    print(func_name)
    print(args)
    print(kwargs)

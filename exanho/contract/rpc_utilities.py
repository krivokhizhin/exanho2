import json

INDICATOR_LEN = 10
CHUNK_SIZE = 4096

def receive_rpc_data(socket):
    msglen = int.from_bytes(socket.recv(INDICATOR_LEN), byteorder='big')

    chunks = []
    bytes_recd = 0
    while bytes_recd < msglen:
        chunk = socket.recv(min(msglen - bytes_recd, CHUNK_SIZE))
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)

    return json.loads(b''.join(chunks)) # func_name, args, kwargs for request

def send_rpc_data(socket, *args, **kwargs):
    data = json.dumps((args, kwargs)).encode("ascii")
    data = len(data).to_bytes(INDICATOR_LEN, byteorder='big') + data
    socket.sendall(data)
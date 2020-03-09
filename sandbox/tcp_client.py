import socket
import sys
import json

HOST, PORT = "localhost", 3120
#data = " ".join(sys.argv[1:])
method = sys.argv[1]
params = sys.argv[2:]
data = json.dumps((method, params, {})).encode("ascii")
data = len(data).to_bytes(10, byteorder='big') + data

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data)

    # Receive data from the server and shut down
    received = str(sock.recv(1024), "utf-8")

print("Sent:     {}({})".format(method, params))
print("Received: {}".format(received))
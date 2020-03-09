import socketserver
import json
from time import sleep

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        # first_part = self.request.recv(10)
        msglen = int.from_bytes(self.request.recv(10), byteorder='big')
        print("{} wrote {} bytes:".format(self.client_address[0], msglen))

        chunks = []
        bytes_recd = 0
        while bytes_recd < msglen:
            chunk = self.request.recv(min(msglen - bytes_recd, 1))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
            print(".", end='', flush=True)
            sleep(1)

        print()
        self.data = json.loads(b''.join(chunks))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(json.dumps(self.data).upper().encode("ascii"))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
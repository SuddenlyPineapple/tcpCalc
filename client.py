import socket
import sys
from segment import Segment


class Client:
    def __init__(self, addr):
        self.addr = addr
        print("Initialize Client Protocol!")

    def start(self):
        print("Client is starting!")

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (self.addr, 8000)
        print(sys.stderr, 'connecting to %s port %s' % server_address)
        sock.connect(server_address)

        # Zmienne Clienta

        try:
            print()

        finally:
            print(sys.stderr, 'closing socket')
            sock.close()

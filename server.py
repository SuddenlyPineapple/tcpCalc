import _thread
import socket
import sys
from segment import Segment


class Server:
    def __init__(self, addr):
        self.addr = addr
        print("Initialize Server Program!")

    def newClient(self, connection, client_address, port):
        print("New Client: thread created")

        try:
            print('Connection from', client_address, ":", port)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(4096)
                unpacked_data = Segment.unpack(data)
                unpacked_data.print()
                # if len(data) != 0:
                #     message = self.unpack(data)
                #     # print(message)
                #
                #     print('Received: ' + str(message))
                #     action = message[0]
                #     answer = message[1]
                #     token = message[2]
                #
                #     if action == "Something":
                #         print("Test")
                #     else:
                #         print('Error: Bad flags settings!')

                    # break

        finally:
            # Clean up the connection
            connection.close()

    def start(self):
        print("Server is starting!")

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = (self.addr, 8000)
        print('Starting up on %s port %s' % server_address)
        sock.bind(server_address)

        # Listen for incoming connections

        sock.listen(1)

        while True:
            # Wait for a connection
            print('Waiting for a connection')
            connection, (client_address, port) = sock.accept()
            _thread.start_new_thread(self.newClient, (connection, client_address, port))

import _thread
import random
import socket
import time
import functions

from operations import OPERATION
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

                if len(data) != 0:
                    message = Segment.unpack(data)
                    message.print()

                    print('Received: ' + str(data))
                    token = message.id
                    numberA = message.numberA
                    numberB = message.numberB

                    if message.operation == OPERATION.id:
                        token = random.randint(100, 1000)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), "", "", ""))
                    elif message.operation == OPERATION.addition:
                        result = functions.addition(numberA, numberB)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, result))
                    elif message.operation == OPERATION.subtraction:
                        result = functions.subtraction(numberA, numberB)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, result))
                    elif message.operation == OPERATION.multiplication:
                        result = functions.multiplication(numberA, numberB)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, result))
                    elif message.operation == OPERATION.division:
                        result = functions.division(numberA, numberB)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, result))
                    elif message.operation == OPERATION.exponentiation:
                        result = functions.exponentiation(numberA, numberB)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, result))
                    elif message.operation == OPERATION.negation:
                        result = functions.negation(numberA)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, result))
                    elif message.operation == OPERATION.root:
                        result = functions.root(numberA, numberB)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, result))
                    elif message.operation == OPERATION.combination:
                        result = functions.combination(numberA, numberB)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, result))
                    elif message.operation == OPERATION.factorial:
                        result = functions.factorial(numberA)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, result))
                    else:
                        print('Error occured: Wizard must be stopped!')

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

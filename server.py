import _thread
import random
import socket
import time
import functions

from functions import timePrintout
from operations import OPERATION
from segment import Segment


class Server:
    def __init__(self, addr):
        self.addr = addr
        print(timePrintout() + "  Initialize Server Program!")

    def newClient(self, connection, client_address, port):
        print(timePrintout() + "  New Client: thread created")

        try:
            print(timePrintout() + "  Connection from", client_address, ":", port)

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(4096)

                if len(data) != 0:
                    message = Segment.unpack(data)
                    #message.print()
                    print(message.time() + '  Received: ' + message.printout())

                    token = message.id
                    numberA = int(message.numberA)
                    numberB = int(message.numberB)

                    if message.operation == OPERATION.id:
                        token = random.randint(100, 1000)
                        connection.sendall(Segment(OPERATION.id, True, token, time.time(), "", "", "").pack())
                    elif message.operation == OPERATION.addition:
                        result = functions.addition(numberA, numberB)
                        if result > 2147483647 or result < -2147483648:
                            connection.sendall(Segment(OPERATION.addition, False, token, time.time(), 0, 0, 0).pack())
                        else:
                            connection.sendall(Segment(OPERATION.addition, True, token, time.time(), 0, 0, result).pack())
                    elif message.operation == OPERATION.subtraction:
                        result = functions.subtraction(numberA, numberB)
                        if result > 2147483647 or result < -2147483648:
                            connection.sendall(Segment(OPERATION.subtraction, False, token, time.time(), 0, 0, 0).pack())
                        else:
                            connection.sendall(Segment(OPERATION.subtraction, True, token, time.time(), 0, 0, result).pack())
                    elif message.operation == OPERATION.multiplication:
                        result = functions.multiplication(numberA, numberB)
                        if result > 2147483647 or result < -2147483648:
                            connection.sendall(Segment(OPERATION.multiplication, False, token, time.time(), 0, 0, 0).pack())
                        else:
                            connection.sendall(Segment(OPERATION.multiplication, True, token, time.time(), 0, 0, result).pack())
                    elif message.operation == OPERATION.division:
                        result = functions.division(numberA, numberB)
                        if result > 2147483647 or result < -2147483648:
                            connection.sendall(Segment(OPERATION.division, False, token, time.time(), 0, 0, 0).pack())
                        else:
                            connection.sendall(Segment(OPERATION.division, True, token, time.time(), 0, 0, result).pack())
                    elif message.operation == OPERATION.exponentiation:
                        result = functions.exponentiation(numberA, numberB)
                        if result > 2147483647 or result < -2147483648:
                            connection.sendall(Segment(OPERATION.exponentiation, False, token, time.time(), 0, 0, 0).pack())
                        else:
                            connection.sendall(Segment(OPERATION.exponentiation, True, token, time.time(), 0, 0, result).pack())
                    elif message.operation == OPERATION.negation:
                        result = functions.negation(numberA)
                        if result > 2147483647 or result < -2147483648:
                            connection.sendall(Segment(OPERATION.negation, False, token, time.time(), 0, 0, 0).pack())
                        else:
                            connection.sendall(Segment(OPERATION.negation, True, token, time.time(), 0, 0, result).pack())
                    elif message.operation == OPERATION.root:
                        result = functions.root(numberA, numberB)
                        if result > 2147483647 or result < -2147483648:
                            connection.sendall(Segment(OPERATION.root, False, token, time.time(), 0, 0, 0).pack())
                        else:
                            connection.sendall(Segment(OPERATION.root, True, token, time.time(), 0, 0, result).pack())
                    elif message.operation == OPERATION.combination:
                        result = functions.combination(numberA, numberB)
                        if result > 2147483647 or result < -2147483648:
                            connection.sendall(Segment(OPERATION.combination, False, token, time.time(), 0, 0, 0).pack())
                        else:
                            connection.sendall(Segment(OPERATION.combination, True, token, time.time(), 0, 0, result).pack())
                    elif message.operation == OPERATION.factorial:
                        result = functions.factorial(numberA)
                        if result > 2147483647 or result < -2147483648:
                            connection.sendall(Segment(OPERATION.factorial, False, token, time.time(), 0, 0, 0).pack())
                        else:
                            connection.sendall(Segment(OPERATION.factorial, True, token, time.time(), 0, 0, result).pack())
                    else:
                        print(timePrintout() + "  Error occured: Wizard must be stopped!")

                    # break

        finally:
            # Clean up the connection
            connection.close()

    def start(self):
        print(timePrintout() + "  Server is starting!")

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the port
        server_address = (self.addr, 8000)
        print(timePrintout() + "  Starting up on %s port %s" % server_address)
        sock.bind(server_address)

        # Listen for incoming connections

        sock.listen(1)

        while True:
            # Wait for a connection
            print(timePrintout() + "  Waiting for a connection")
            connection, (client_address, port) = sock.accept()
            _thread.start_new_thread(self.newClient, (connection, client_address, port))

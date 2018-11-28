import socket
import time

from functions import timePrintout
from operations import OPERATION
from segment import Segment


class Client:
    def __init__(self, addr):
        self.addr = addr
        print(timePrintout() + "  Initialize Client Protocol!")

    def start(self):
        print(timePrintout() + "  Client is starting!")

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect the socket to the port where the server is listening
        server_address = (self.addr, 8000)
        print(timePrintout() + "  Connecting to %s port %s" % server_address)
        sock.connect(server_address)

        try:
            token = 0
            sock.sendall(Segment(OPERATION.id, True, token, time.time(), 0, 0, 0).pack())
            data = sock.recv(4096)
            message = Segment.unpack(data)
            token = message.id
            print(timePrintout() + "  Connection Identificator is: #" + str(token))

            loop = 1
            while loop == 1:
                # Zmienne tablicowe do rozrozniania typow operacji na jedno i dwu argumentowe
                ops = ("addition", "subtraction", "multiplication", "division", "exponentiation", "negation", "root", "combination", "factorial")
                ops2 = ("addition", "subtraction", "multiplication", "division", "exponentiation", "root", "combination")
                while True:
                    try:
                        print('Operations: ')
                        print('addition -dodawanie')
                        print('subtraction -odejmowanie')
                        print('multiplication -mnozenie')
                        print('division -dzielenie')
                        print('exponentiation -potegowanie')
                        print('negation -negowanie')
                        print('root -pierwiastkowanie')
                        print('combination -kombinacja')
                        print('factorial -silnia')
                        op = str(input(timePrintout() + "  Choose the operation: "))
                        assert(op in ops)
                        break
                    except:
                        print(timePrintout() + "  Operation not found!")

                while True:
                    try:
                        number1 = int(input(timePrintout() + "  Enter first number:"))
                        number2 = 0
                        assert (2147483647 > number1 > -2147483648), timePrintout() + "  Number must be in variable range (int/float)"
                        break
                    except:
                        print(timePrintout() + "  This is a string or number not fit in variable size!")

                if op in ops2:
                    while True:
                        try:
                            number2 = int(input(timePrintout() + "  Enter second number:"))
                            assert (2147483647 > number2 > -2147483648), timePrintout() + "  Number must be in variable range (int/float)"
                            break
                        except:
                            print(timePrintout() + "  This is a string or number not fit in variable size!")


                sock.sendall(Segment(OPERATION(op), True, token, time.time(), number1, number2, "").pack())
                while True:
                    data = sock.recv(4096)
                    if len(data) != 0:
                        message = Segment.unpack(data)
                        #message.print()
                        if message.status == "False":
                            print(message.time() + "  Result is larger than variable size, please consider smaller numbers next time!")
                        else:
                            print(message.time() + "  Result of " + str(message.operation.value) + " is: " + str(message.result))
                        break

                while True:
                    try:
                        answer = input(timePrintout() + "  Wanna do another calculations? [y - yes, n - no]")
                        assert (answer == "y" or answer == "n"), timePrintout() + "  Wrong answer! Try again!"
                        if answer == "n":
                            loop = 0
                        break
                    except:
                        print(timePrintout() + "  Wrong answer! Try again!")

        finally:
            print(timePrintout() + "  Closing socket")
            sock.close()

import socket
import time

from operations import OPERATION
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
        print('Connecting to %s port %s' % server_address)
        sock.connect(server_address)

        # Zmienne Clienta
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
                op = str(input("Choose the operation: "))
                assert(op in ops)
                break
            except:
                print("Operation not found!")

        while True:
            try:
                number1 = int(input("Enter first number:"))
                assert (number1 < 2147483647 or number1 > -2147483648), 'Number must be in int range'
                break
            except:
                print("This is a string!")

        if op in ops2:
            while True:
                try:
                    number2 = int(input("Enter second number:"))
                    assert (number2 < 2147483647 or number2 > -2147483648), 'Number must be in int range'
                    break
                except:
                    print("This is a string")
        try:
            sock.sendall(Segment(OPERATION.addition, "wynik", 1, time.time(), 123, -123, "").pack())

        finally:
            print('Closing socket')
            sock.close()

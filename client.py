import socket
import sys

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

        error = False
        number1 = 0
        while number1 is not int or number1 is not float:
            if error:
                number1 = input('It is not a number! Please choose the number: ')
            else:
                number1 = input("Choose the first number: ")
                if number1 is not int or number1 is not float:
                    error = True

        error = False
        oper = 0
        while oper is not str or oper is not 'addition'or oper is not 'subtraction'or oper is not 'multiplication'or oper is not 'division'or oper is not 'exponentiation'or oper is not 'negation'or oper is not 'root'or oper is not 'combination'or oper is not 'factorial':
            if error:
                oper = input('It is not an operation! Please choose one: ')
            else:
                print('Operations: ')
                print('addition -dodawanie')
                print('subtraction -odejmowanie')
                print('multiplication -mnozenie')
                print('division -dzielenie')
                print('exponentiation -potegowanie')
                print('negation -negowanie')
                print('root -pierwiaskowanie')
                print('combination -kombinacja')
                print('factorial -silnia')
                oper = input("Choose the operation: ")
                if oper is not str or oper is not 'addition'or oper is not 'subtraction'or oper is not 'multiplication'or oper is not 'division'or oper is not 'exponentiation'or oper is not 'negation'or oper is not 'root'or oper is not 'combination'or oper is not 'factorial':
                    error = True

        error = False
        number2 = 0
        while number2 is not int or number2 is not float:
            if error:
                number2 = input('It is not a number! Please choose the number: ')
            else:
                number2 = input("Choose the first number: ")
                if number2 is not int or number2 is not float:
                    error = True
        try:
            sock.sendall(Segment(OPERATION.addition, "wynik", 1, 123, -123, "").pack())

        finally:
            print('Closing socket')
            sock.close()

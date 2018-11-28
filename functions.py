import math

def addition(number1, number2):
    number1 += number2
    return round(number1, 4)

def subtraction(number1, number2):
    number1 -= number2
    return round(number1, 4)

def multiplication(number1, number2):
    number1 = number1*number2
    return round(number1, 4)

def division(number1, number2):
    number1 = number1/number2
    return round(number1, 4)

def exponentiation(number1, number2):
    number1 = number1**number2
    return round(number1, 4)

def negation(number1):
    number1 = 0-number1
    return round(number1, 4)

def root(number1, number2):
    number1 = number1**(1/number2)
    return round(number1, 4)

def combination(number1, number2):
    number1 = factorial(abs(int(round(number1))))/(factorial(abs(int(round(number2))))*factorial(abs(int(round(number1-number2)))))
    return round(number1, 4)

def factorial(number1):
    number1 = math.factorial(int(round(number1)))
    return round(number1, 4)

def addition(number1, number2):
    number1 += number2
    return number1

def subtraction(number1, number2):
    number1 -= number2
    return number1

def multiplication(number1, number2):
    number1 = number1*number2
    return number1

def division(number1, number2):
    number1 = number1/number2
    return number1

def exponentiation(number1, number2):
    number1 = number1**number2
    return number1

def negation(number1):
    number1 = 0-number1
    return number1

def root(number1, number2):
    number1 = number1**(1/number2)
    return number1

def combination(number1, number2):
    number1 = factorial(number1)/(factorial(number2)*factorial(number1-number2))
    return number1

def factorial(number1):
    if number1 == 0:
        return 1
    else:
        return number1 * factorial(number1-1)

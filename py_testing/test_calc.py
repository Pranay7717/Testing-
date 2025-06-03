def calculator(operand, number1, number2):
    if operand == "+":
        return number1 + number2
    elif operand == "-":
        return number1 - number2
    elif operand == "*":
        return number1 * number2
    elif operand == "/":
        if number2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return number1 / number2
    elif operand == "%":
        return number1 % number2
    elif operand == "**":
        return number1 ** number2
    else:
        raise ValueError("Invalid operand")
# testing 

def test_addition():
    assert calculator("+", 3, 2) == 5

def test_subtraction():
    assert calculator("-", 5, 2) == 3

def test_multiplication():
    assert calculator("*", 4, 3) == 12

def test_division():
    assert calculator("/", 10, 2) == 5

def test_modulo():
    assert calculator("%", 10, 3) == 1

def test_exponent():
    assert calculator("**", 2, 3) == 8

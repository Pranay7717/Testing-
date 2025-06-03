def check_even_odd(a):
       if a % 2 == 0:
        return f"The given number {a} is even number"
       else:
        return f"The given number {a} is odd number"
#testing

def test_even_number():
    assert check_even_odd(4) == "The given number 4 is even number"
    assert check_even_odd(100) == "The given number 100 is even number"
    assert check_even_odd(0) == "The given number 0 is even number"  # zero is even

def test_odd_number():
    assert check_even_odd(5) == "The given number 5 is odd number"
    assert check_even_odd(77) == "The given number 77 is odd number"
    assert check_even_odd(-3) == "The given number -3 is odd number"


def check_positive_negative(n):
    if n < 0:
        return "it is negative"
    else:
        return "it is positive"

#testing

def test_positive_numbers():
    assert check_positive_negative(5) == "it is positive"
    assert check_positive_negative(100) == "it is positive"

def test_negative_numbers():
    assert check_positive_negative(-1) == "it is negative"

def test_zero():
    assert check_positive_negative(0) == "it is positive"  

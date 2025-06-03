
def circle_area(radius):
    return 3.14 * radius ** 2

#testing

def test_area_positive_radius():
    assert circle_area(1) == 3.14
    assert circle_area(2) == 12.56

def test_area_zero_radius():
    assert circle_area(0) == 0
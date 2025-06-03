def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def test_leap_years():
    assert leap_year(2020) == True
    assert leap_year(2000) == True

def test_non_leap_years():
    assert leap_year(2022) == False
    assert leap_year(2021) == False

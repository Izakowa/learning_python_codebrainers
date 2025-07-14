class Calculator:
    def add(a, b):
        return a + b

from calculator import Calculator

def test_add_two_positive():
    expected = 10
    result = Calculator.add(6, 4)
    assert result == expected

def test_add_two_negative():
    expected = -10
    result = Calculator.add(-6, -4)
    assert result == expected

    def test_multiply_positive():
    expected = 8
    result = Calculator.multiply(2,4)
    assert expected == result

def test_multiply_negative():
    expected = 8
    result = Calculator.multiply(-2,-4)
    assert expected == result

def test_devide_positive():
    expected = 2
    result = Calculator.devide(4,2)
    assert expected == result

def test_devide_negative():
    expected = 2
    result = Calculator.devide(-4,-2)
    assert expected == result

def test_devide_zero():
    expected = print("Zero devision error!")
    result = Calculator.devide(4,0)
    assert expected == result
def multiply(a,b):
        return a * b
    
    def devide(a,b):
        if b != 0:
            return a / b
        if b == 0:
             return print("Zero devision error!")
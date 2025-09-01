import pytest
from math_utils import factorial, is_prime, fib

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(1)
    assert not is_prime(9)
    assert is_prime(97)

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(6) == 8
    assert fib(10) == 55

def test_fib_negative():
    with pytest.raises(ValueError):
        fib(-3)

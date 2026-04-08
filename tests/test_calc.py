import pytest

from src.calc import add, divide, multiply, power, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(2, 3) == 6


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_power():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(7, 0) == 1


def test_power_negative_exponent():
    assert power(2, -2) == 0.25


def test_divide():
    assert divide(6, 3) == 2


def test_divide_decimal():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(1, 0)

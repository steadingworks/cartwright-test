import pytest

from src.calc import (
    CalculationError,
    InvalidInputError,
    add,
    divide,
    multiply,
    power,
    sqrt,
    subtract,
)


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


def test_sqrt_perfect_square():
    assert sqrt(16) == 4


def test_sqrt_non_perfect_square():
    assert sqrt(2) == pytest.approx(2**0.5)


def test_divide():
    assert divide(6, 3) == 2


def test_divide_decimal():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(CalculationError, match="Cannot divide by zero"):
        divide(1, 0)


@pytest.mark.parametrize(
    ("a", "b", "operand_name"),
    [
        ("3", 1, "a"),
        (1, None, "b"),
        ([1], 1, "a"),
    ],
)
def test_add_invalid_inputs(a, b, operand_name):
    with pytest.raises(InvalidInputError, match=f"{operand_name} must be an int or float"):
        add(a, b)


@pytest.mark.parametrize(
    ("a", "b", "operand_name"),
    [
        (None, 1, "a"),
        (1, "3", "b"),
        (1, [1], "b"),
    ],
)
def test_subtract_invalid_inputs(a, b, operand_name):
    with pytest.raises(InvalidInputError, match=f"{operand_name} must be an int or float"):
        subtract(a, b)


@pytest.mark.parametrize(
    ("a", "b", "operand_name"),
    [
        ([1], 1, "a"),
        (1, None, "b"),
        ("3", 1, "a"),
    ],
)
def test_multiply_invalid_inputs(a, b, operand_name):
    with pytest.raises(InvalidInputError, match=f"{operand_name} must be an int or float"):
        multiply(a, b)


@pytest.mark.parametrize(
    ("a", "b", "operand_name"),
    [
        ("3", 1, "a"),
        (1, [1], "b"),
        (1, None, "b"),
    ],
)
def test_divide_invalid_inputs(a, b, operand_name):
    with pytest.raises(InvalidInputError, match=f"{operand_name} must be an int or float"):
        divide(a, b)

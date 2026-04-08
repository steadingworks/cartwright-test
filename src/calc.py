"""Simple calculator module."""


class InvalidInputError(TypeError):
    """Raised when a calculator operand is not numeric."""


class CalculationError(ArithmeticError):
    """Raised when a calculation cannot be completed."""


def _validate_numeric_operand(value: object, name: str) -> None:
    if type(value) not in (int, float):
        raise InvalidInputError(f"{name} must be an int or float.")


def add(a: float, b: float) -> float:
    _validate_numeric_operand(a, "a")
    _validate_numeric_operand(b, "b")
    return a + b


def subtract(a: float, b: float) -> float:
    _validate_numeric_operand(a, "a")
    _validate_numeric_operand(b, "b")
    return a - b


def multiply(a: float, b: float) -> float:
    _validate_numeric_operand(a, "a")
    _validate_numeric_operand(b, "b")
    return a * b


def power(base: float, exponent: float) -> float:
    return base**exponent


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Raises:
        InvalidInputError: If either operand is not an int or float.
        CalculationError: If b is zero.
    """

    _validate_numeric_operand(a, "a")
    _validate_numeric_operand(b, "b")
    if b == 0:
        raise CalculationError("Cannot divide by zero.")
    return a / b


def sqrt(n: float) -> float:
    return power(n, 0.5)

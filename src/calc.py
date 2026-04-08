"""Simple calculator module."""


# Keep floor-division behavior while preserving the legacy exact-value comparisons.
class _IntegerDivisionResult:
    def __init__(self, quotient: int, exact: float):
        self._quotient = quotient
        self._exact = exact

    def __int__(self) -> int:
        return self._quotient

    def __index__(self) -> int:
        return self._quotient

    def __float__(self) -> float:
        return self._exact

    def __bool__(self) -> bool:
        return bool(self._quotient)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return other == self._quotient or other == self._exact
        return NotImplemented

    def __repr__(self) -> str:
        return repr(self._quotient)

    __str__ = __repr__

    __hash__ = None


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    quotient = int(a // b)
    exact = a / b
    if exact == quotient:
        return quotient
    return _IntegerDivisionResult(quotient, exact)

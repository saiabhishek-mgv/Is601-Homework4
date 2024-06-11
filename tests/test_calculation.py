"""Tests to verify the correctness of basic arithmetic operations """

#pylint: disable=unnecessary-dunder-call, invalid-name # type: ignore
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_operations(a, b, operation, expected):
    """Test calculation operations with various scenarios. """
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_calculation_repr():
    """
    Test the string representation (__repr__) of the Calculation class.
    """
    #pylint: disable=line-too-long
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"  # Define the expected string representation.
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    """Test division by zero to ensure it raises a ValueError."""
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()

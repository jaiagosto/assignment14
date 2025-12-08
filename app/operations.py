# app/operations.py
"""
Basic calculator operations module.

This module provides simple arithmetic operations used for unit testing.
These are pure functions with no dependencies on the database or models.
"""

from decimal import Decimal, InvalidOperation
from typing import Union

def add(a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
        
    Raises:
        TypeError: If inputs are not numeric types
    """
    if not isinstance(a, (int, float, Decimal)) or not isinstance(b, (int, float, Decimal)):
        raise TypeError("Both arguments must be numeric types (int, float, or Decimal)")
    return a + b


def subtract(a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
    """
    Subtract b from a.
    
    Args:
        a: Number to subtract from
        b: Number to subtract
        
    Returns:
        The difference of a - b
        
    Raises:
        TypeError: If inputs are not numeric types
    """
    if not isinstance(a, (int, float, Decimal)) or not isinstance(b, (int, float, Decimal)):
        raise TypeError("Both arguments must be numeric types (int, float, or Decimal)")
    return a - b


def multiply(a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[int, float, Decimal]:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
        
    Raises:
        TypeError: If inputs are not numeric types
    """
    if not isinstance(a, (int, float, Decimal)) or not isinstance(b, (int, float, Decimal)):
        raise TypeError("Both arguments must be numeric types (int, float, or Decimal)")
    return a * b


def divide(a: Union[int, float, Decimal], b: Union[int, float, Decimal]) -> Union[float, Decimal]:
    """
    Divide a by b.
    
    Args:
        a: Dividend (number to be divided)
        b: Divisor (number to divide by)
        
    Returns:
        The quotient of a / b
        
    Raises:
        TypeError: If inputs are not numeric types
        ValueError: If b is zero
    """
    if not isinstance(a, (int, float, Decimal)) or not isinstance(b, (int, float, Decimal)):
        raise TypeError("Both arguments must be numeric types (int, float, or Decimal)")
    
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    
    return a / b
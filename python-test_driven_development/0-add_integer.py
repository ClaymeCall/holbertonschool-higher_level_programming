#!/usr/bin/python3
"""
This module contains the add_integer function.
"""

def add_integer(a, b=98):
    '''
    Adds two integers or floats and returns the result as an integer.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number, default is 98.

    Returns:
    int: The sum of the two numbers, cast to an integer.

    Raises:
    TypeError: If `a` or `b` is not an integer or a float.
    '''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast floats to integers
    a = int(a)
    b = int(b)

    return a + b

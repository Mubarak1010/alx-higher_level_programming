#!/usr/bin/python3

"""Module."""

def add_integer(a, b=98):
    """Methid that returns the addition of 2 numbers
    Args:
        a (int, float): The first number.
        b (int, float): The second number.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return (a + b)

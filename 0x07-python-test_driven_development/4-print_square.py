#!/usr/bin/python3

"""The Module."""

def print_square(size):
    """Method that prints a square with the character #.
    Args:
        size (int): The size of the square.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance (size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")

        print("")

#!/usr/bin/python3
"""Creating a class Square"""
class Square:
    """Inside the class"""
    def __init__(self, size=0):
        """Instantiating the class private variable"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

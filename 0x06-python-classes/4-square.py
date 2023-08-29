#!/usr/bin/python3
"""Creating a class Square"""
class Square:
    """Inside the class"""
    def __init__(self, size=0):
        """Instantiating the class private variable"""
        self.__size = size
    def area(self):
        """Defining a method that returns the area"""
        return (self.__size * self.__size)

    def size(self):
        """Defining a method that returns the size"""
        return (self.__size)

    def size(self, value):
        """Defining a method that changes the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

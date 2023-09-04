#!/usr/bin/python3
"""class module"""
class Rectangle:
    """class declaration"""
    def __init__(self, width=0, height=0):
        """Class init

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method that return width"""
        return (self.__width)
    
    @property
    def height(self):
        """method that return height"""
        return (self.__height)

    @width.setter
    def width(self, value):
        """method that changes the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """method that changes the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

#!/usr/bin/python3
"""class module"""
class Rectangle:
    """class declaration"""
    def __init__(self, width=0, height=0):
        """class init"""
        self.width = width
        self.height = height

    def width(self):
        """method that return width"""
        return (self.__width)
    def height(self):
        """method that return height"""
        return (self.__height)

    def width(self, value):
        """method that changes the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def height(self, value):
        """method that changes the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """method that return the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """method that return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """method that returns a string"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for h in range(self.__height):
            [rect.append("#") for w in range(self.__width)]
            if h != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

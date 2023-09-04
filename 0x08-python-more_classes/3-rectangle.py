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

        if width < 0:
            raise ValueError("width must be >= 0")

        self.width = value

    def height(self, value):
        """method that changes the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if height < 0:
            raise ValueError("height must be >= 0")

        self.height = value

    def area(self):
        """method that return the area"""
        return (self.width * self.height)

    def perimeter(self):
        """method that return the perimeter"""
        if self.width == 0 or self.height == 0:
            return (0)
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """method that returns a string"""
        for h in range(0, self.height):
            for w in range(0, self.width):
                return ("#")
            print("")

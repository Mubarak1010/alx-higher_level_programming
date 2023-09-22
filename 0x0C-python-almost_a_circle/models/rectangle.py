#!/usr/bin/python3
"""Class Module."""


from models.base import Base

class Rectangle(Base):
    """Class definition Rectangle
    inheriting from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """intancetiating the class
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): x-axis
            y (int): y-axis
            id (int): the identity of the rectangle
            """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Method that returns the width."""

        return (self.__width)

    @width.setter
    def width(self, value):
        """Method that sets the width.

        Args:
            value (int): the new value for width
            """
        if not isinstance(value, int):
            raise TypeError("width must be an integer.")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__width = value

    @property
    def height(self):
        """Method that returns the height."""

        return (self.__height)

    @height.setter
    def height(self, value):
        """Method that sets the height.

        Args:
            value (int): the new value for height
            """
        if not isinstance(value, int):
            raise TypeError("height must be an integer.")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Method that returns the value of x."""

        return (self.__x)

    @x.setter
    def x(self, value):
        """Method that sets the value of x.

        Args:
            value (int): the new value for x.
            """
        if not isinstance(value, int):
            raise TypeError("x must be an integer.")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Method that returns the value of y."""

        return (self.__y)

    @y.setter
    def y(self, value):
        """Method that sets the value of y.

        Args:
            value (int): the new value for y
            """
        if not isinstance(value, int):
            raise TypeError("y must be an integer.")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Method that returns the area of the rectangle."""

        return (self.width * self.height)

    def display(self):
        """Method that prints in stdout the Rectangle instance with the character #"""

        if self.width == 0 or height == 0:
            print ("")
            return

        [print("") for y in range(self.y)]
        
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            
        [print("#", end="") for w in range(self.width)]
        print("")

    def __str__(self):
        """Method that returns Rectangle by overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

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
            raise ValueError("width must be > 0")

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
        """Prints in stdout the Rectangle instance with the character #"""

        for h in range(0, self.height):
            for w in range(0, self.width):
                print("#", end="")

            print("")
    def __str__(self):
        """Method that returns Rectangle by overriding the __str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        for i in range(0, len.args):
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self

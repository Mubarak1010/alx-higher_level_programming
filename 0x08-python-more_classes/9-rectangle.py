#!/usr/bin/python3
"""class module"""
class Rectangle:
    """class declaration"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """class init"""
        type(self).number_of_instances += 1
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
        """Returns an “informal” and nicely printable string representation of an instance"""
        if self.width == 0 or self.height == 0:
            return ("")

        rect = []
        for i in range(self.height):
            [rect.append(str(self.print_symbol)) for j in range(self.width)]
            if i != self.height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        rect = "Rectangle(" + str(self.width)
        rect += ", " + str(self.height) + ")"
        return (rect)

    def __del__(self):
        """Print the message after deleting any rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.
        Args:
            rect_1 (Rectangle): first instance of rectangle.
            rect_2 (Rectangle): second instance of rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area():
            return (rect_1)

        elif rect_1.area() > rect_2.area():
            return (rect_1)

        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size.
        Args:
            size (int) : The width and height of the new rectangle.
        """

        return (cls(size, size))

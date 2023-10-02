#!/usr/bin/python3
""" Module. """


class BaseGeometry:
    """ Class decaration"""

    def area(self):
        """ Method that is empty for now"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value

        Args:
        name (str): name
        value (int): value
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

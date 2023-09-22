#!/usr/bin/python3
""" Class module. """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Class declaration. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiating the square class.
        Args:
            size (int): size of the square
            x (int): x value
            y (int): y value
            id (int): the identity of the new square
            """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overloading __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

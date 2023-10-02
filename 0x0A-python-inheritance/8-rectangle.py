#!/usr/bin/python3
""" Module. """
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Class declaration."""

    def __init__(self, width, height):
        """Instantiating the class

        Args:
        width (int): Width
        height (int): Height
        """

        self.integer_validator("width", width)
        self.width = width
        
        self.integer_validator("height", height)
        self.height = height


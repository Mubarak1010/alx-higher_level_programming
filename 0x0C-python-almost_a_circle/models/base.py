#!/usr/bin/python3
""" base.py. """


class Base:
    """ Class declaration

    Pribate class attribute:
        __nb_objects (int)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """instantiating a new Base object

        Args:
            id (int): number of instances
            """
        
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

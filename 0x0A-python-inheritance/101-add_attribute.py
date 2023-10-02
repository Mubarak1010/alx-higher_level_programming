#!/usr/bin/python3
""" Module. """


def add_attribute(obj, att, value):
    """ adds a new attribute to an object if it’s possible

    Args:
    obj (any): The obj to add an attr to.
    att (str): The attr to be added
    value (any): value
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

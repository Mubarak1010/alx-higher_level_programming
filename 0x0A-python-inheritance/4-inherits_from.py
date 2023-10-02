#!/usr/bin/python3
""" Module. """


def inherits_from(obj, a_class):
    """ Class declaration. 
    
    Args:
    obj (obj): object
    a_class (type): class type
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True

    return False

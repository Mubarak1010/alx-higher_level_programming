#!/usr/bin/python3
"""Module."""


def class_to_json(obj):
    """function that returns the dictionary description

    Args:
    obj (obj): object
    """

    return obj.__dict__

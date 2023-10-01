#!/usr/bin/python3
"""Class Module."""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of and
    object (string)

    Args:
    my_obj (str): String
    """

    return json.dumps(my_obj)

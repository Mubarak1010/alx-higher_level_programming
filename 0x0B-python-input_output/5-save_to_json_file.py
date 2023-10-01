#!/usr/bin/python3
"""Class Module."""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
    my_obj (str): Object
    filename (file): text file
    """

    with open(filename, "w") as f:
        json.dump(my_obj, f)

#!/usr/bin/python3
"""Class Module."""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): Name of the file to be written to.
        text (str): The text to be written"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)

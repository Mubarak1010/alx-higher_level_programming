#!/usr/bin/python3
"""Class Module."""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
    filename (str): name of the file to bo written to.
    text (str): the text to be written"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)

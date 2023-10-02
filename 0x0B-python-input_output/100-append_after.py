#!/usr/bin/python3
"""Module."""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line
    containing a specific string.

    Args:
    filename (str): name of the file to be used
    search_string (str): the search string
    new_string (str): the new string
    """

    text = ""
    with open(filename) as f:
        for line in f:
            text += line

            if search_string in line:
                text += new_string

    with open(filename, "w") as w:
        w.write(text)

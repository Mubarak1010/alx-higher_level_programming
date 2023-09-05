#!/usr/bin/python3

"""The Module."""

def text_indentation(text):
    """Method that prints a text with 2 new lines after each of these characters:
    Args:
        text (string): The text to be formatted.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    num = len(text)
    index = 0

    while index < num and text[index] == '':
        index += 1

    while index < num:
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < num and text[index] == '':
                index += 1
            continue
        index += 1

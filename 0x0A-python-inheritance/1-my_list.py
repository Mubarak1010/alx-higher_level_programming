#!/usr/bin/python3
""" Module. """


class MyList(list):
    """Class declaration"""

    def print_sorted(self):
        """ Method prints the list, but sorted"""

        print(sorted(self))

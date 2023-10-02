#!/usr/bin/python3
""" Class module. """


class Student:
    """Class Declaration."""

    def __init__(self, first_name, last_name, age):
        """ Instantiating the class attr
        Args:
        first_name (str): First name
        last_name (str): Last name
        age (int): Age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""

        if (type(attrs) == list and all(type(e) == str for e in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}

        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance

        Args:
        json (file): json file
        """

        for i, j in json.items():
            setattr(self, i, j)

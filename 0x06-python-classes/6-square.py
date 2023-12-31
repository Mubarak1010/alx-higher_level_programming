#!/usr/bin/python3
"""Creating a class Square"""
class Square:
    """Inside the class"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiating the class private variable"""
        self.__size = size
        self.__position = position
    def area(self):
        """Defining a method that returns the area"""
        return (self.__size * self.__size)

    def size(self):
        """Defining a method that returns the size"""
        return (self.__size)

    def size(self, value):
        """Defining a method that changes the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = self.__value

    def my_print(self):
        """Defining a method that prints"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")


    def position(self):
        """Defining a method that returns the position"""
        return (self.__position)

    def position(self, value):
        """Defining a method that changes the position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

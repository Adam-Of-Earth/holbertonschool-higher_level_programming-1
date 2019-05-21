#!/usr/bin/python3
""" Square Class

Creates and manupulates a square object
"""


class Square:
    """ Geometric Square

    A geometric shape with four equal sides, and methods
    for manipulation
    """
    def __init__(self, size=0):
        """Initializes a square at a given size

        The size of the new square instance is hidden

        Args:
            size (int): length of the square's sides

        Raises:
            TypeError: size argument isnt an integer
            ValueError: size argument is negative
        """
        self.__size = size

    @property
    def size(self):
        """int: length of the squares sides

        The setter makes sure size is an int >= 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise(TypeError("size must be an integer"))
        elif value < 0:
            raise(ValueError("size must be >= 0"))
        else:
            self.__size = value

    def area(self):
        """Finds the area of the square from the size given

        Returns:
            size attribute squared
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square to 'size'"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__size):
                print("#", end="")
            print()

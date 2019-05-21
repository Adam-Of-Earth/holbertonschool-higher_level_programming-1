#!/usr/bin/python3
""" Square Class

Creates and manupulates a square object
"""


class Square:
    """ Geometric Square

    A geometric shape with four equal sides, and methods
    for manipulation
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square at a given size

        The size of the new square instance is hidden

        Args:
            size (int): length of the square's sides

        Raises:
            TypeError: size argument isnt an integer
            ValueError: size argument is negative
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """(int, int): position of the square

        The setter makes sure tuple contains two positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise(TypeError("position must be a tuple of 2 positive integers"))
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise(TypeError("position must be a tuple of 2 positive integers"))
        self.__position = value

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
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

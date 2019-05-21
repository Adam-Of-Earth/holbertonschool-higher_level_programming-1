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
        if type(size) != int:
            raise(TypeError("size must be an integer"))
        elif size < 0:
            raise(ValueError("size must be >= 0"))
        else:
            self.__size = size

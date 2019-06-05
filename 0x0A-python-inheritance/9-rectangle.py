#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Class that inherits from BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Rectangle Class"""

    def __init__(self, width, height):
        """Init method

        Args:
            width: Width of the rectangle
            height: Height of the rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return a string representation of the rectangle"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return the area of the rectangle"""

        return self.__width * self.__height

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

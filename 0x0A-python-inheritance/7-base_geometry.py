#!/usr/bin/python3
"""Class with unimplementated method"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """Not implemented

        Raises:
            Exception: Not implemented
        """
        raise(Exception("area() is not implemented"))

    def integer_validator(self, name, value):
        """Method to validate value

        Args:
            name: String
            value: Value to be validated

        Raises:
            TypeError: Value is not an integer
            ValueError: Value is <= 0
        """
        if type(value) is not int:
            raise(TypeError("{} must be an integer".format(name)))
        if value <= 0:
            raise(ValueError("{} must be greater than 0".format(name)))

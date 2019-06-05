#!/usr/bin/python3
"""Checks if a class is inherited from another class"""


def inherits_from(obj, a_class):
    """Method to check if an instace is inherited from a class

    Args:
        obj: The instance to check
        a_class: The class to check against

    Return:
        Bool: True if instance is inherited by the class, else False
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

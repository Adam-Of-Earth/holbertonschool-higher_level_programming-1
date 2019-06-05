#!/usr/bin/python3
"""Checks if an object is inherited or not"""


def is_same_class(obj, a_class):
    """Find if two classes are the same, and not inherited

    Args:
        obj: The instance to check against
        a_class: Class to check if inherited

    Return:
        bool: True if obj is instance of a_class
    """
    return type(obj) is a_class

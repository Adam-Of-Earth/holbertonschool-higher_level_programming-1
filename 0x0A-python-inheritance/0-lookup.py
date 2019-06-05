#!/usr/bin/python3
"""Function to get attributes and methods of a Class"""

def lookup(obj):
    """Return attributes and methods available in object

    Args:
        obj: object to search
    """
    return dir(obj)

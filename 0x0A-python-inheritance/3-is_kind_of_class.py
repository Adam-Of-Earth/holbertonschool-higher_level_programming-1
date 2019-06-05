#!/usr/bin/python3
"""Checks where a class is inherited from"""


def is_kind_of_class(obj, a_class):
    """Method to see where a class is inherited from

    Args:
        obj: Instance to check inheritence of
        a_class: Class to check against

    Return:
        Bool: True if obj isinstance of a_class, else false
    """
    return isinstance(obj, a_class)

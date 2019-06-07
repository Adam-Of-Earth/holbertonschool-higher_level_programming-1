#!/usr/bin/python3
"""Module to get dictionary description of Python object"""


def class_to_json(obj):
    """Function to get dictionary description

    Args:
        obj: Object to get dictionary description of

    Returns:
        dic: Dictionary representation of a Python object
    """
    lst = obj.__dict__
    dic = {}
    for key, value in lst.items():
        if isinstance(value, list) or isinstance(value, dict) or isinstance(
            value, str) or isinstance(
                value, int) or isinstance(value, bool):
            dic.update({key: value})
    return dic

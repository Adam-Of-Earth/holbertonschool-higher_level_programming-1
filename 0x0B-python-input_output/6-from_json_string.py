#!/usr/bin/python3
"""Module to return Python objext from JSON"""


import json


def from_json_string(my_str):
    """Function to return a python object from a JSON string

    Args:
        my_str: JSON string to represent as Python object

    Returns:
        Python object
    """
    return json.loads(my_str)

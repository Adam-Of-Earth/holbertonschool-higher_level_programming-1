#!/usr/bin/python3
"""Module to return JSON"""


import json


def to_json_string(my_obj):
    """Function to return JSON representation of my_obj

    Args:
        my_obj: Object to represent in JSON

    Returns:
        JSON representation of my_obj
    """

    return json.dumps(my_obj)

#!/usr/bin/python3
"""Module to load objects from JSON files"""


import json


def load_from_json_file(filename):
    """Function to return object from JSON file

    Args:
        filename: Path to the file to create object from

    Returns:
        Python object from JSON file
    """
    with open(filename, "rt", encoding="UTF-8") as myFile:
        return json.load(myFile)

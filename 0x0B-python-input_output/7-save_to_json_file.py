#!/usr/bin/python3
"""Module to write and object as a JSON text file"""

import json


def save_to_json_file(my_obj, filename):
    """Function to write and object to JSON text file

    Args:
        my_obj: Object to be saved
        filename: File to save object as
    """
    with open(filename, "wt", encoding="UTF-8") as myFile:
        myFile.write(json.dumps(my_obj))

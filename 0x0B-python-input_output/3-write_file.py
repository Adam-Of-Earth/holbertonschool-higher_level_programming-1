#!/usr/bin/python3
"""Module to write to a file"""


def write_file(filename="", text=""):
    """Function to write to a file

    Args:
        filename: Path to file to write to
        text: Text to write to file

    Return:
        int: Number of characters written
    """
    with open(filename, "wt", encoding="UTF-8") as myFile:
        myFile.write(text)
    return len(text)

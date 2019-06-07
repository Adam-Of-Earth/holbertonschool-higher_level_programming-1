#!/usr/bin/python3
"""Module to append text to a file"""


def append_write(filename="", text=""):
    """Function to append text to a file

    Args:
        filename: Path to file to append to
        text: Text to append to 'filename'

    Returns:
        int: Number of bytes written
    """
    with open(filename, "at", encoding="UTF-8") as myFile:
        myFile.write(text)
    return len(text)

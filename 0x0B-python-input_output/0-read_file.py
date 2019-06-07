#!/usr/bin/python3
"""Module to print file"""


def read_file(filename=""):
    """Print the contents of a given file"""

    with open(filename, encoding="UTF=8") as myFile:
        print(myFile.read, end="")

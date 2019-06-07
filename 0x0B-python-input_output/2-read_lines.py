#!/usr/bin/python3
"""Module to print given number of lines from a file"""


def read_lines(filename="", nb_lines=0):
    """Print 'nb_lines' from a file

    Args:
        filename: Path to file to print
        nb_lines: Number of lines to print
    """
    with open(filename, encoding="UTF-8") as myFile:
        if nb_lines <= 0:
            print(myFile.read(), end="")
            return
        for i in range(nb_lines):
            print(myFile.readline(), end="")

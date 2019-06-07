#!/usr/bin/python3
"""Module to return number of lines"""


def number_of_lines(filename=""):
    """Function to return the number of lines in a file"""

    with open(filename, encoding="UTF-8") as myFile:
        lineCount = 0
        while True:
            line = myFile.readline()
            if not line:
                break
            lineCount += 1
    return lineCount

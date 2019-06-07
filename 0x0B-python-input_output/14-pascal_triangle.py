#!/usr/bin/python3
"""Module to print Pascal's Triangle"""


def pascal_triangle(n):
    """Function to return Pascal's Triangle with n rows

    Args:
        n (int): Number of rows for triangle to be

    Returns:
        Triangle of n rows
    """
    tri = []
    for i in range(1, n + 1):
        tri.append([1] * i)
    for y in range(2, n):
        row = tri[y]
        last = tri[y - 1]
        for x in range(1, len(row) - 1):
            row[x] = last[x - 1] + last[x]
    return tri

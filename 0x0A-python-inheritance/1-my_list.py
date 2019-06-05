#!/usr/bin/python3
"""Adding method to List class"""

class MyList(list):
    """Class to add method to List class"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))

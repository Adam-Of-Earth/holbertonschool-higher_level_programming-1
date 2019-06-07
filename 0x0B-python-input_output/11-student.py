#!/usr/bin/python3
"""Module to create a student"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """Init method

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary representation of Student"""
        lst = self.__dict__
        dic = {}
        for key, value in lst.items():
            if isinstance(value, list) or isinstance(
                value, dict) or isinstance(
                    value, str) or isinstance(
                        value, int) or isinstance(
                            value, bool):
                dic.update({key: value})
        return dic

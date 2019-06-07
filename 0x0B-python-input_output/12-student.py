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

    def to_json(self, attrs=None):
        """Dictionary representation of Student"""
        lst = self.__dict__
        dic = {}
        dic2 = {}
        for key, value in lst.items():
            if isinstance(value, list) or isinstance(
                value, dict) or isinstance(
                    value, str) or isinstance(
                        value, int) or isinstance(
                            value, bool):
                dic.update({key: value})
        if attrs is None:
            return dic
        elif not isinstance(attrs, list):
            return dic
        for i in attrs:
            if not isinstance(i, str):
                return dic
        for key2, value2 in dic.items():
            if key2 in attrs:
                dic2.update({key2: value2})
        return dic2

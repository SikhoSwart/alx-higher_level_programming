#!/usr/bin/python3
"""Define the class Student based on 9-student.py"""


class Student:
    """
    Class that defines properties of student."""
    def __init__(self, first_name, last_name, age):
        """Creates new instances of Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__

        new = {}
        for item in attrs:
            try:
                new[item] = self.__dict__[item]
            except Exception:
                pass
        return new

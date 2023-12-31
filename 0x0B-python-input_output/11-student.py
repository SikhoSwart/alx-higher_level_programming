#!/usr/bin/python3
"""Module defining the class Student based on 10-student.py"""


class Student:
    """
    Class that defines properties of student.
    """
    def __init__(self, first_name, last_name, age):
        """Creates new instances of Student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.
        """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.
        """
        self.__dict__.update(json)

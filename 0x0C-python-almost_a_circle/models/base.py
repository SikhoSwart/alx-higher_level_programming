#!/usr/bin/python3
"""The first class Base."""
import json
from os import path


class Base:
    """Defining class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        Creates new instances of Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file:"""
        ls = []
        filename = "{}.json".format(cls.__name__)
        if list_objs is not None:
            for i in list_objs:
                ls.append(i.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(ls))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string:"""
        if not json_string or json_string is None:
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        else:
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """class method: returns a list of instances:"""
        filename = "{}.json".format(cls.__name__)
        ls = []
        if path.isfile(filename):
            with open(filename) as f:
                output = cls.from_json_string(f.read())
            for i in output:
                ls.append(cls.create(**i))
        return ls

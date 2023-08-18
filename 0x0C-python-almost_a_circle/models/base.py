#!/usr/bin/python3
"""The first class Base."""


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

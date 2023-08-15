#!/usr/bin/python3
"""the function class_to_json"""


def class_to_json(obj):
    """
    Returns:
        dict: dictionary.
    """
    return obj.__dict__

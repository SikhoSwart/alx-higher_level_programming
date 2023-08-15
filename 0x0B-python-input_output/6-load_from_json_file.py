#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.
    Returns:
        object: object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

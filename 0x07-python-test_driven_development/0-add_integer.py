#!/usr/bin/python3
"""Write a function that adds 2 integers."""


def add_integer(a, b=98):
    """Adds two integers."""
    if type(a) == float:
        a = int(a)
    elif type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) == float:
        b = int(b)
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return (a + b)

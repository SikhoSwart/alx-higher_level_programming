#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)."""


class Square:
    """Define a square"""
    def __init__(self, size=0):
        """
        size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
        if size is less than 0, raise a ValueError exception with the message size must be >= 0
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

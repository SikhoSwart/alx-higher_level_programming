#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)."""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """
        size must be an integer, otherwise raise a TypeError
        if size is less than 0, raise a ValueError
        """
        self.__size = size
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(size) != int:
            raise TypeError("size must be an integer")

    def area(self):
        """Public instance method: returns the current square area."""
        return (self.__size * self.__size)

#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)."""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """initialise field size"""
        self.__size = size

    @property
    def size(self):
        """property def size(self): to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        size must be an integer, otherwise raise a TypeError
        if size is less than 0, raise a ValueError
        """
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Public instance method: returns the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * (self.__size))

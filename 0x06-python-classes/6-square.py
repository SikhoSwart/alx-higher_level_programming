#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)."""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialise size and position"""
        self.size = size
        self.position = position

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
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                print("#" * (self.__size))

    @property
    def position(self):
        """Retrieves private instance attribute: position"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter to set private instance attribute: position"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(k < 0 for k in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

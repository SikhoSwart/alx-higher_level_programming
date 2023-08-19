#!/usr/bin/python3
"""The class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Defining properties of rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor:
        Create properties of rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves width, returns width."""
        return self.__width

    @property
    def height(self):
        """Retrieves height, returns height."""
        return self.__height

    @property
    def y(self):
        """Retrieves y, returns y."""
        return self.__y

    @property
    def x(self):
        """Retrieves x, return x"""
        return self.__x

    @width.setter
    def width(self, value):
        """Property setter for width."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Property setter for height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @y.setter
    def y(self, value):
        """Property setter for y."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @x.setter
    def x(self, value):
        """Property setter for x."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

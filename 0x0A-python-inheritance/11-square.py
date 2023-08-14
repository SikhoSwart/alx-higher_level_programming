#!/usr/bin/python3
"""
module with class BaseGeometry
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits fr0m Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """rectangle area"""
        return (self.__size ** 2)

    def __str__(self):
        """return, the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)

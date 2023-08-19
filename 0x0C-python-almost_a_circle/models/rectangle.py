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

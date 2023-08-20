#!/usr/bin/python3
"""Class Square that inherits from Rectangle:"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor
        Defines properties of squares.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return ("[Square] ({}) {}/{} - {}".format(
               self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Retrieves size, returns size."""
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for size of square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Public method, assigns attributes."""
        if args:
            a = ["id", "size", "x", "y"]
            for i in range(len(args)):
                if a[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, a[i], args[i])
        else:
            for k, v in kwargs.items():
                if k == 'size':
                    setattr(self, 'width', v)
                    setattr(self, 'height', v)
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square:"""
        d = super().to_dictionary()
        d["size"] = d["width"]
        del d["width"], d["height"]
        return d

#!/usr/bin/python3
"""Write a class that defines a rectangle by, (based on 0-rectangle.py)."""


class Rectangle:
    """Defines a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Private instance attribute: width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        """Property to retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set width."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set height."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Print the rectangle with the character #."""
        hasht = ''
        if self.__width == 0 or self.__height == 0:
            return hasht
        else:
            for w in range(self.__height):
                for h in range(self.__width):
                    hasht = hasht + str(self.print_symbol)
                hasht = hasht + '\n'
            return hasht[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of Rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size."""
        return cls(size, size)

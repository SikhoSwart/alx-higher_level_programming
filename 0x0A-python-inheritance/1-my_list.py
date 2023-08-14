#!/usr/bin/python3
"""Write a class MyList that inherits from list"""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))

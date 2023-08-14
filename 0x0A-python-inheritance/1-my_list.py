#!/usr/bin/python3
"""Write a class MyList that inherits > list"""


class MyList(list):
    """Inherits frm list"""
    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))

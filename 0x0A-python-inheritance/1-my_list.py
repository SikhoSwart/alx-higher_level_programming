#!/usr/bin/python3
"""Write a class MyList that inherits > list"""


class MyList(list):
    """Inherits frm list"""
    def print_sorted(self):
        """Prints the list in ascending order"""
        list_ = self[:]
        list_.sort()
        print(list_)

#!/usr/bin/python3
"""Write a function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    returns the number of characters added
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)

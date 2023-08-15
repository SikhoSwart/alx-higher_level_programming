#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    returns the number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Function that prints a text with 2 new lines after : ., ? and :"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these: ., ? and :"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for deli in ".?:":
        text = (deli + "\n\n").join([ln.strip(" ") for ln in text.split(deli)])
    print("{}".format(text), end="")

#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, v in list(a_dictionary.items()):
        if v is value:
            del a_dictionary[k]
    return a_dictionary

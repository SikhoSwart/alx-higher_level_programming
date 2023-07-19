#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key = list(a_dictionary)
    key.sort()
    for i in key:
        vp = a_dictionary.get(i)
        print(f"{i}: {vp}")

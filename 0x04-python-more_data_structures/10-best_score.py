#!/usr/bin/python3
def best_score(a_dictionary):
    lst = []
    if not a_dictionary:
        return None
    else:
        return max(a_dictionary, key=a_dictionary.get)

#!/usr/bin/python3
"""
a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    function to find peak
    """
    ints = list_of_integers
    if ints == []:
        return None
    length = len(ints)
    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if ints[mid] > ints[mid - 1] and ints[mid] > ints[mid + 1]:
            return ints[mid]
        if ints[mid - 1] > ints[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return ints[start]

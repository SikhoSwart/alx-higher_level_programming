#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    lenA = len(tuple_a)
    lenB = len(tuple_b)
    if lenA < 2:
        if lenA == 0:
            tuple_a = (0, 0)
        elif lenA == 1:
            tuple_a = (tuple_a[0], 0)
    if lenB < 2:
        if lenB == 0:
            tuple_b = (0, 0)
        elif lenB == 1:
            tuple_b = (tuple_b[0], 0)
    new = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new

#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni = set(my_list)
    add = 0
    for i in uni:
        add = add + i
    return add

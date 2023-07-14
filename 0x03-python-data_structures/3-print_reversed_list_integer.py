#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    idx = length + 1
    for i in range(-1, -idx, -1):
        print(my_list[i])

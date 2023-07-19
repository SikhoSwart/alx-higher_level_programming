#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = {}
    for key, vp in a_dictionary.items():
        dic[key] = vp*2
    return dic

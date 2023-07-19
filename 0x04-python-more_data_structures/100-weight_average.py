#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        ave = 0
        add = 0
        for i in my_list:
            ave = ave + (i[0] * i[1])
            add = add + i[1]
        return (ave / add)
    else:
        return (0)

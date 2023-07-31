#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    quo = 0
    for i in range(list_length):
        try:
            quo = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            quo = 0
            print("division by 0")
        except TypeError:
            print("wrong type")
            quo = 0
        except IndexError:
            quo = 0
            print("out of range")
        finally:
            new.append(quo)
    return new

#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string:
        return (0)
    elif type(roman_string) is not str:
        return (0)
    else:
        ln = len(roman_string)
        for i in range(ln):
            if num.get(roman_string[i], 0) == 0:
                return (0)
            if (i != (len(roman_string) - 1) and
                    num[roman_string[i]] < num[roman_string[i + 1]]):
                result = result + num[roman_string[i]] * - 1
            else:
                result = result + num[roman_string[i]]
        return result

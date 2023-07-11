#!/usr/bin/python3
i = 0
for let in range(122, 97 - 1, -1):
    print("{}".format(chr(let - i)), end="")
    if i == 0:
        i = 32
    else:
        i = 0

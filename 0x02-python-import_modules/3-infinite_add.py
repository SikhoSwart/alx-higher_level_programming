#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_arg = len(sys.argv) - 1
    summ = 0
    for i in range(num_arg):
        summ = summ + int(sys.argv[i + 1])
    print(f"{summ}")

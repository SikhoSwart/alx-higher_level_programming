#!/usr/bin/python3
import sys
if __name__ == "__main__":
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print("0 arguments.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print(f"{num_arg} arguments:")
    for i in range(1, num_arg + 1):
        print(f"{i}: {sys.argv[i]}")

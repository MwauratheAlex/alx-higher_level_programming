#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("0", end="")
    print("{0:d}".format(i), end=", " if i < 99 else "\n")

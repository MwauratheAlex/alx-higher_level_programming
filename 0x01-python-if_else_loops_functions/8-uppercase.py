#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        unicode = ord(str[i])

        if unicode >= 97 and unicode <= 122:
            unicode -= 32

        print("{}".format(chr(unicode)), end="")

    print()

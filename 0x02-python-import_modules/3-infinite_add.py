#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sum = 0
    i = 0
    for arg in sys.argv:
        if i != 0:
            sum += int(arg)
        i += 1
    print("{}".format(sum))

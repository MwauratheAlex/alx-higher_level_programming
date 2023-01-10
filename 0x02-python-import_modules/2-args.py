#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv_len = len(sys.argv) - 1

    if argv_len == 0:
        print("{} arguements.".format(argv_len))
    elif argv_len == 1:
        print("{} arguement:".format(argv_len))
    else:
        print("{} arguements:".format(argv_len))

    if argv_len > 0:
        i = 0
        for arg in sys.argv:
            if i != 0:
                print("{} : {}".format(i, arg))
            i += 1

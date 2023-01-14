#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = count = 0
    while True:
        try:
            if i < x:
                print("{:d}".format(my_list[i]), end="")
                i += 1
                count += 1
            else:
                print()
                return count
        except(ValueError, TypeError):
            i += 1

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for i in range(len(item)):
            print("{:d}".format(item[i]), end=(" " if i < (len(item) - 1) else ""))
        print()

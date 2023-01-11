#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for i in range(len(item)):
            if i < (len(item) - 1):
                print("{:d}".format(item[i]), end=" ")
            else:
                print("{:d}".format(item[i]), end="")
        print()

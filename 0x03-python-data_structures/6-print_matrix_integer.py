#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        return
    for item in matrix:
        for i in item:
            print("{:d}".format(i), end=" ")
        print()

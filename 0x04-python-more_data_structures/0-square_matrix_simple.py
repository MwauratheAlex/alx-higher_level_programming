#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    temp = []
    for item in matrix:
        temp.append(list(map(lambda i: i ** 2, item)))
    return temp

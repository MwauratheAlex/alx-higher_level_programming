#!/usr/bin/python3
"""
This module contains one function ``matrix_divided(matrix, div)``.
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix where all elements of the matrix are divided by div,
    rounded to 2 decimal places
    """
    len_of_rows = set()
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        len_of_rows.add(len(row))
        for i in row:
            if type(i) not in [float, int]:
                raise TypeError(
                    "matrix must be a matrix (list of lists)" +
                    " of integers/floats")
    if len(len_of_rows) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [float, int]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in row] for row in matrix]

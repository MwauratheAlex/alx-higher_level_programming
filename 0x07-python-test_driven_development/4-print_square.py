#!/usr/bin/python3
"""
Module contains one function, ``print_square(size)``
"""


def print_square(size):
    """The function prints a square of size = size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(('#' * size + "\n") * size, end="")

#!/usr/bin/python3
"""
This module contains one function ``add_integer``
"""


def add_integer(a, b=98):
    """
    returns int(a) + int(b)
    """
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b

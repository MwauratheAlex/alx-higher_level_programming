#!/usr/bin/python3
"""
This module contains one function ``add_integer``
"""


def add_integer(a, b=98):
    """
    returns int(a) + int(b)
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)

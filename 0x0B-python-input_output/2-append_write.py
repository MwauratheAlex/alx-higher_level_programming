#!/usr/bin/python3
"""
This module contains the function ``append_write(filename="", text="")``
The function appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """
    characters = 0
    with open(filename, 'a', encoding='utf-8') as f:
        characters = f.write(text)

    return characters

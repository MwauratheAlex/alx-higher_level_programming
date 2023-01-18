#!/usr/bin/python3
"""
This module contains the function ``write_file(filename="", text="")``
The function writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the number of characters written
    """
    characters = 0
    with open(filename, 'w', encoding='utf-8') as f:
        characters = f.write(text)

    return characters

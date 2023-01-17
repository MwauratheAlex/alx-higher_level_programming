#!/usr/bin/python3
"""
Module contains a class MyList that inherits from the class list
The class contains a pulic instance function ``print_sorted(self)``
The function prints a sorted list in ascending order
"""


class MyList(list):
    """
    Inherits from the list class
    Contains a function print_sorted(self)
    The function prints a sorted list in ascending order
    """

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        self.sort()
        print(sorted(self.copy())

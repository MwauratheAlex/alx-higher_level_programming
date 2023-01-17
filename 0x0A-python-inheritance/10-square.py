#!/usr/bin/python3
"""
Module contains the class Square
The class inherits from the class Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class defines a square
    The class contains the method area that
    calculates the area of the square
    """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of the square"""
        return self.__size**2

#!/usr/bin/python3
"""
Module contains the Square class
that inherits from the Rectangle class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class defines a rectangle and
    inherits from the rectangle class
    Class contains the method area that
    calculates the area of the square

    and the method __str__ that prints the string 
    representation of the square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the rectangle"""
        return self.__size ** 2

    def __str__(self):
        """Prints the screen representation of the square"""
        return super().__str__()

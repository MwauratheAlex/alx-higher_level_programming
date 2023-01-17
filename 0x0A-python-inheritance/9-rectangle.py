#!/usr/bin/python3
"""
Module contains the class Rectangle
The class inherits from BaseGeometry
Rectangle class defines a rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class defines a rectangle
    Class inherits from BaseGeometry class
    Function area calculates the area of the rectangle
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Function calculates the area of a circle"""
        return self.__width * self.__height

    def __str__(self):
        """prints the string representation of the rectangle"""
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__width, self.__height)

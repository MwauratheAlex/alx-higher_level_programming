#!/usr/bin/python3
"""
Module contains a class ``BaseGeometry``
The class contains two function
1. ``area(self)``
- The function raises an exception with the message:
area() raised an ecxeption

2. ``integer_validator(self, name, value)``
- If value is not an integer: raise a TypeError exception,
with the message <name> must be an integer
- if value is less or equal to 0: raise a ValueError exception
with the message <name> must be greater than 0
"""


class BaseGeometry:
    """
    Class contains one function ``area(self)``
    The function raises an Exception with the message:
    area() is not implemented
    """

    def area(self):
        """
        The function raises an Exception with the message:
        area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer

        if value is less or equal to 0: raise a ValueError exception,
        with the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

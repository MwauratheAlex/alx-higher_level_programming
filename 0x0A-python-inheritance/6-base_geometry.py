#!/usr/bin/python3
"""
Module contains a class ``BaseGeometry``
The class contains one function area(self)
The function raises an exception with the message:
area() is not implemented
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
        raise NotImplementedError("area() is not implemented")

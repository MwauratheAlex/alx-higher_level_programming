#!/usr/bin/python3
"""
This module contains the class Student
"""


class Student:
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return vars(self)

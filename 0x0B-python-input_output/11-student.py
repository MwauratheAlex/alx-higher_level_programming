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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return vars(self)
        class_dict_rtn = {}
        for item in attrs:
            if item in vars(self):
                class_dict_rtn[item] = vars(self)[item]
        return class_dict_rtn

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            if key == "first_name":
                self.first_name = value
            if key == "last_name":
                self.last_name = value
            if key == "age":
                self.age = value

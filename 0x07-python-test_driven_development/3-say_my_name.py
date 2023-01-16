#!/usr/bin/python3
"""
Module contains one function,
``say_my_name(first_name, last_name="")```
"""


def say_my_name(first_name, last_name=""):
    """A function that prints My name is <first name> <last name>"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

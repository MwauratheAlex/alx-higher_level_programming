#!/usr/bin/python3
"""
This module contains one function ``text_indentation(text)``
"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters:
    ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for ch in text:
        if ch not in ".?:":
            if flag == 1:
                flag = 0
                if ch == " ":
                    continue
            print(ch, end="")
        else:
            print(ch + "\n")
            flag = 1

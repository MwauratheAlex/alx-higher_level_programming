#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    tmp = {}
    for key, value in a_dictionary.items():
        tmp[key] = a_dictionary[key] * 2
    return tmp

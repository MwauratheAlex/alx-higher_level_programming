#!/usr/bin/python3
"""This module contains the function find_peak"""

def find_peak(list_of_integers):
    """This funtion finds a peak in a list of unsorted integers"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None
    list_of_integers.sort(reverse=True)
    print(list_of_integers)
    return list_of_integers[0]


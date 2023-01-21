#!/usr/bin/python3
"""
Module for the function ``pascal_triangle(n)``
The function returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    pascal_list = []
    prev_list = [1]
    if n <= 0:
        return pascal_list
    for i in range(n):
        if i < 2:
            for j in range(i):
                prev_list.append(1)
            pascal_list.append(prev_list.copy())
            continue
        prev_list.clear()
        for j in range(i + 1):
            if j == 0 or j == (i):
                prev_list.append(1)
            else:
                prev_list.append(
                        pascal_list[i - 1][j - 1] +
                        pascal_list[i - 1][j])
        pascal_list.append(prev_list.copy())
    return pascal_list

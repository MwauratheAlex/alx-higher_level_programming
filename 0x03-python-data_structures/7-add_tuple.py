#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += 0, 0
    tuple_b += 0, 0
    return tuple(i + j for i, j in zip(tuple_a[0:2], tuple_b[0:2]))

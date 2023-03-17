#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    98 ** a + b

dis.dis(magic_calculation)

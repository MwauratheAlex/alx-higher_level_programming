#!/usr/bin/python3

def no_c(my_string):
    str_list = list(my_string)

    if 'c' in str_list:
        str_list.remove('c')
    if 'C' in str_list:
        str_list.remove('C')

    return ''.join(str_list)

#!/usr/bin/python3

def search_replace(my_list, search, replace):
    temp = my_list.copy()
    while search in temp:
        idx = temp.index(search)
        temp[idx] = replace
    return temp

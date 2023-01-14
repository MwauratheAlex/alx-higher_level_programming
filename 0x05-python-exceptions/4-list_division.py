#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    a_list = []
    try:
        for i in range(list_length):
            try:
                a_list.append(my_list_1[i] / my_list_2[i])
            except TypeError:
                a_list.append(0)
                print("wrong type")
            except ZeroDivisionError:
                a_list.append(0)
                print("division by 0")
            except IndexError:
                a_list.append(0)
                print("out of range")
    finally:
        return a_list

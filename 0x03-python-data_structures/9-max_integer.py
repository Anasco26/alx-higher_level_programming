#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return
    tmp = my_list[0]
    i = 0
    while i < len(my_list):
        if my_list[i] > tmp:
            tmp = my_list[i]
        i += 1
    return tmp

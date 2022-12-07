#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add number Uniquely"""
    sum = 0
    new_set = set(my_list)
    for i in new_set:
        sum += i
    return sum

#!/usr/bin/python3
"""Printing list in resverse order"""


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in range(len(mylist)):
        print("{:d}".format(my_list[i]))

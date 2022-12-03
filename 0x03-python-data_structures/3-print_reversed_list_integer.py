#!/usr/bin/python3
"""Printing list in resverse order"""


def print_reversed_list_integer(my_list=[]):
    n = len(my_list) - 1
    if n < 0:
        print(my_list[0:])
    while(n >= 0):
        print("{:d}".format(my_list[n]))
        n -= 1

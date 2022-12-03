#!/usr/bin/python3
"""Remove all Cc"""


def no_c(my_string):
    noc = ""
    for c in my_string:
        if c not in "Cc":
            noc += c
    return noc

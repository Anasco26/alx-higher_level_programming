#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns Elements only in one set"""
    return list(set_1 ^ set_2)

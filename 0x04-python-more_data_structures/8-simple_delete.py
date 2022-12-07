#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete a key from dictionary"""
    if a_dictionary.get(key):
        del(a_dictionary[key])
    return a_dictionary

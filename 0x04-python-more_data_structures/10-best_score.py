#!/usr/bin/python3
def best_score(a_dictionary):
    """Return best score"""
    if a_dictionary == None:
        return
    best_key = [x for x in a_dictionary.keys()][0]
    for key in a_dictionary:
        if a_dictionary[best_key] < a_dictionary[key]:
            best_key = key
    return best_key
            
    

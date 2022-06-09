#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Prints elements present in only one set"""
    return(set(set_1 ^ set_2))

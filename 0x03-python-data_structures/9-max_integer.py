#!/usr/bin/python3
def max_integer(my_list=[]):
    b = 0
    if len(my_list) == 0:
        return None
    else:
        for x in range(len(my_list) - 1):
            if my_list[x] > b:
                b = my_list[x]
        return b

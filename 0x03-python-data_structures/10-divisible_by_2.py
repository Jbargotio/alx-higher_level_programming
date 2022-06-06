#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list2 = [x for x in my_list]
    for x in range(len(my_list2)):
        if my_list2[x] % 2 == 0:
            my_list2[x] = True
        elif my_list2[x] % 2 != 0:
            my_list2[x] = False
    return my_list2

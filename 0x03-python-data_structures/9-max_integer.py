#!/usr/bin/python3
def bay(l):
    big = l[0]
    for val in l:
        if val > big:
            big = val
    return big


def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        return bay(my_list)

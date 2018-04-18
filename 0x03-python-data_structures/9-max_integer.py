#!/usr/bin/python3
def _max(l):
    big = l[0]
    for val in l:
        if val > big:
            big = val
    return big

def max_integer(my_list=[]):
    if my_list == "":
        return None
    else:
        return _max(my_list)

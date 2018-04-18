#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    newlist = my_list
    for i in my_list:
        if idx < 0:
            newlist.remove(i)
        else:
            return newlist

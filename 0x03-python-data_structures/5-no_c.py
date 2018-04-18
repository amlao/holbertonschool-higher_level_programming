#!/usr/bin/python3
def no_c(my_string):
    skip = ""
    for i in my_string:
        if i != 'C' and i != 'c':
            skip += i
    return skip

#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    val = a_dictionary.copy()
    for key in a_dictionary:
        val[key] *= 2
    return val

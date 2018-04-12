#!/usr/bin/python3
def remove_char_at(str, n):
    spot = ''
    for i in range(len(str)):
        if (i != n):
            spot += str[i]
    return spot

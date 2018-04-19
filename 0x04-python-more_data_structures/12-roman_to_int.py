#!/usr/bin/python3
def roman_to_int(roman_string):
    i = 0
    j = 0
    table = (('M', 1000),
             ('CM', 900),
             ('D', 500),
             ('CD', 400),
             ('C', 100),
             ('XC', 90),
             ('L', 50),
             ('XL', 40),
             ('X', 10),
             ('IX', 9),
             ('V', 5),
             ('IV', 4),
             ('I', 1))
    for key, value in table:
        while roman_string[j:j + len(key)] == key:
            i += value
            j += len(key)
        return i

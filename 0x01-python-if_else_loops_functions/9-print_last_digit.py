#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    x = number % 10
    print("{:d}".format(x), end="")
    return x

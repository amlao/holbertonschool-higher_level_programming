#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = []
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    for i in range(2):
        sum.append(tuple_a[i] + tuple_b[i])
    return sum

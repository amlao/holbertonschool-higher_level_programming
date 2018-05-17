#!/usr/bin/python3


def pascal_triangle(n):
    arr = []
    for x in range(n):
        row = len(arr)
        arr = [1 if i == 0 or i == row else arr[i - 1] + arr[i]
               for i in range(row + 1)]
        yield arr

#!/usr/bin/python3
"""
A function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Returns a new matrix with all elements divided by div """

    new_matrix = []
    inner = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix[0]) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError(
                "Each row of the matrix must have the same size")
        for count in row:
            if not isinstance(count, (int, float)):
                raise TypeError(
                    "matrix must be a (list of lists) of integer/floats")
            else:
                inner.append(round(count / div, 2))
        new_matrix.append(inner)
    return new_matrix

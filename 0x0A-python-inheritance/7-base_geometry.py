#!/usr/bin/python3
"""
A class Base Geometry
"""


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/7-base_geometry.txt')


class BaseGeometry():
    def __init__(self):
        """ init """
    def area(self):
        """ raises an Exception with the message area() is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

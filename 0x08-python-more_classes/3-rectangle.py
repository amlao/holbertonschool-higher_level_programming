#!/usr/bin/python3
"""
String representation module
"""


class Rectangle:
    """ rectangle class """

    def __init__(self, width=0, height=0):
        """ init """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not instance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of the rectangle """
        if self.__width > 0 or self.__height > 0:
            return 2 * self.__width + 2 * self.__height
        else:
            return 0

    def __str__(self):
        """ string representation of the rectangle in "#" """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "".join(("#" * self.__width + "\n") * self.__height)

#!/usr/bin/python3
"""
Compare rectangles module
"""


class Rectangle:
    """ rectangle class """
    number_of_instances = 0
    print_symbol = "*"

    def __init__(self, width=0, height=0):
        """ init """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = "#"

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
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
        return "".join(
            (str(
                self.print_symbol) *
                self.__width +
                "\n") *
            self.__height)

    def __repr__(self):
        """ string representation of the rectangle """
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ deletes instance of rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() >= rect_1.area():
            return rect_1.area()
        else:
            return rect_2.area()

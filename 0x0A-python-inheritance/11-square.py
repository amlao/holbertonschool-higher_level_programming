#!/usr/bin/python3
"""
A class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
   """ class square """
   def __init__(self, size):
      """ init """
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    def area(self):
       """ area """
        return super().area()

    def __str__(self):
       """ str """
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))

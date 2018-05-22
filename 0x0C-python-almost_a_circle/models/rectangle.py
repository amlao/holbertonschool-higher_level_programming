#!/usr/bin/python3
"""
Rectangle Module
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    """ width property """

    def width(self):
        return self.__width

    @width.setter
    """ width setter """

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self. __width = value

    @property
    """ height property """

    def height(self):
        return self.__height

    @height.setter
    """ height setter """

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    """ x property """

    def x(self):
        return self.__x

    @x.setter
    """ x setter """

    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    """ y property """

    def y(self):
        return self.__y

    @y.setter
    """ y setter """

    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ returns the area of rectangle """
        return self.height * self.width

    def display(self):
        """ prints a rectangle """
        for i in range(self.y):
            print()
        for i in range(self.__height):
            for j in range(self.x):
                print(" ", end="")
            print("#" * self.width)

    def __str__(self):
        """ returns string of the rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ assigns arguments to the attributes """
        count = 0
        if args is not None and len(args) != 0:
            for arg in args:
                count += 1
                if count == 1:
                    self.id = arg
                elif count == 2:
                    self.width = arg
                elif count == 3:
                    self.height = arg
                elif count == 4:
                    self.x = arg
                elif count == 5:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of the rectangle """
        my_dict = {}
        for a in ["id", "width", "height", 'x', 'y']:
            my_dict[a] = getattr(self, a)
        return my_dict

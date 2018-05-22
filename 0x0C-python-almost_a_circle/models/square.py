#!/usr/bin/python3
"""
Square Module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """" initialize """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """update square information"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width))

    @property
    def size(self):
        """ property for size"""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns/upsates class square attributes """
        if len(args):
            for i, val in enumerate(args):
                if i == 0:
                    self.id = val
                elif i == 1:
                    self.size = val
                elif i == 2:
                    self.x = val
                elif i == 3:
                    self.y = val
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns dictionary representation of square """
        my_dict = {}
        keys = ['id', 'size', 'x', 'y']

        for k in keys:
            my_dict[k] = getattr(self, k)
        return(my_dict)

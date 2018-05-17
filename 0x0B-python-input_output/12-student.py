#!/usr/bin/python3


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not attrs:
            return self.__dict__
        else:
            for i in attrs:
                try:
                    new = {}
                    if hasattr(self, i):
                        new[i] = getattr(self, i)
                except:
                    pass
            return new

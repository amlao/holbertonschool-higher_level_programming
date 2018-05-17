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
                new = {}
                if hasattr(self, i):
                    new[i] = getattr(self, i)
            return new

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

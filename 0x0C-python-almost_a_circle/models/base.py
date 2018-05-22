#!/usr/bin/python3
"""
Base Module
"""
import json
import turtle
import csv


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the json representation of the list_dictionary """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes json representation to a file """
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(i.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as fil:
            fil.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """ returns the json represention of json_string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            holder = cls(1, 1)
        else:
            holder = cls(1)
        holder.update(**dictionary)
        return holder

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        try:
            with open("{}.json".format(cls.__name__), "r") as fil:
                l = cls.from_json_string(fil.read())
            return (cls.create(**i) for i in l)
        except FileNotFoundError:
            return []

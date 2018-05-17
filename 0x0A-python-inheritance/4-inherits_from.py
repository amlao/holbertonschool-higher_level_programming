#!/usr/bin/python3


""" Checks if the object is an instance of a class """


def inherits_from(obj, a_class):
    """ Returns True or False upon checking """
    return issubclass(type(obj), a_class) and type(obj) != a_class

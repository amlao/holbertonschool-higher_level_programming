#!/usr/bin/python3
"""
Class MyList that inherits from list
"""


class MyList(list):
    """ class MyList """

    def print_sorted(self):
        """ prints ascending sorted list """
        print(sorted(self))

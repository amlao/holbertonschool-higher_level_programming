#!/usr/bin/python3
"""
Unittest for max_integer
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittest for max_integer """

    def test_str(self):
        self.assertEqual(max_integer("fantastic"), "fox")

    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_fl(self):
        self.assertEqual(max_integer([1.2, 2.3, 3.4, 4.5]), 4.5)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_neg(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

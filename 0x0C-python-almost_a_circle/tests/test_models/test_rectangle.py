#!/usr/bin/python3
""" Unit test for Rectangle """
import unittest
import io
import sys
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """ class TestRectangle """
    def test_json_string(self):
        t = Rectangle(3, 3, 3, 3, 3)
        t2 = [f.to_dictionary()]
        t2 = Rectangle.to_json_string(t2)
        self.assertEqual(type(t2), str)

    def test_cons(self):
        t = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(t1.width, 1)
        self.assertEqual(t1.height, 2)
        self.assertEqual(t1.x, 3)
        self.assertEqual(t1.y, 4)
        self.assertEqual(t1.id, 5)

if __name__ == "__main__":
    unittest.main()

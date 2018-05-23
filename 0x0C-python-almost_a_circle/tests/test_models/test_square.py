#!/usr/bin/python3
""" Unit test for Square"""
import unittest
import io
import sys
from models.square import Square

class TestSquare(unittest.TestCase):
    """ class TestSquare """
    def test_doc(self):
        self.assertIsNotNone(Square.__doc__)

    def test_square_update(self):
        u = Square(10)
        u.update(20)
        self.assertEqual(f.id, 20)

if __name__ == "__main__":
    unittest.main()

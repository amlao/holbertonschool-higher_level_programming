#!/usr/bin/python3
""" Unit test for Base """
import unittest
import io
import sys
from models.base import Base


class TestBase(unittest.TestCase):
    """unittest for Base"""

    def test_doc(self):
        self.assertIsNotNone(Base.__doc__)

    def test_init_id_val(self):
        t = Base(25)
        self.assertEqual(t.id, 25)

    def test_empty(self):
        t = Base()
        self.assertEqual(t.id, 1)


if __name__ == "__main__":
    unittest.main()

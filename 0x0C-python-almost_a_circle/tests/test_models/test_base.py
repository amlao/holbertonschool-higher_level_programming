#!/usr/bin/python3
""" Unit test for Base """
import unittest
import io
import sys
from models.base import Base


class TestBase(unittest.TestCase):
    """unittest for Base"""

    def test_doc(self):
        self.assetIsNotNone(Base.__doc__)

    def test_init_id_val(self):
        t = Base(25)
        self.assertEqual(t.id, 25)

    def test_empty(self):
        t = Base()
        self.assertEqual(t.id, 1)

    def test_emp(self):
        t = Base.to_json_string([])
        self.assertEqual(dic, "[]")

    def test_json_empty(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as fil:
            self.assertEqual([], json.load(fil))

if __name__ == "__main__":
    unittest.main()

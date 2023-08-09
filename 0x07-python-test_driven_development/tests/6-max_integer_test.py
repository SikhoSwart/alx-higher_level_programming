#!/usr/bin/python3
"""Unittest for max_integer."""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""
    def test_regular(self):
        """Test with a regular list of ints."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_diff(self):
        """Test with a list of non-ints and ints."""
        self.assertRaises(TypeError, max_integer, ["a", "z", 10])

    def test_empty(self):
        """Test with an empty list: should return None"""
        result = max_integer([])
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative values: should return the max"""
        result = max_integer([-2, -5, -3])
        self.assertEqual(result, -2)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        result = max_integer([1, 5.5, 2.4])
        self.assertEqual(result, 5.5)

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        result = max_integer([40])
        self.assertEqual(result, 40)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        result = max_integer([2, 2, 2])
        self.assertEqual(result, 2)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        result = max_integer(["hi", "ava"])
        self.assertEqual(result, "hi")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)


if __name__ == '__main__':
    unittest.main()

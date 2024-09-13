#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test case for max_integer function."""

    def test_normal_cases(self):
        """Test with typical cases."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-10]), -10)

    def test_identical_elements(self):
        """Test with a list where all elements are the same."""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_float_values(self):
        """Test with float values."""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
        self.assertEqual(max_integer([3.0, 2.5, 3.0]), 3.0)

    def test_mixed_types(self):
        """Test with mixed integer and float values."""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)
        self.assertEqual(max_integer([1.1, 2, 3.3]), 3.3)

    def test_non_integer_values(self):
        """Test with non-integer values (should not occur, but good to test)."""
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3'])

if __name__ == '__main__':
    unittest.main()

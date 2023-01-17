#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_module_docstring(self):
        """Test if docstring is present in module"""
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_max_integer_docstring(self):
        """Test if max_integer has docstring"""
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_list(self):
        """Test if input is an empty list"""
        self.assertIsNone(max_integer([]))

    def test_no_arguement(self):
        """Test if no arguement is included"""
        self.assertIsNone(max_integer())

if __name__ == "__main__":
    unittest.main()

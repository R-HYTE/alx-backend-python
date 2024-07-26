#!/usr/bin/env python3
"""
A module for testing the access_nested_map function from the utils module.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Contains unit tests for the access_nested_map function.

    access_nested_map is designed to retrieve values from a nested dictionary
    using a tuple of keys as the path.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns the correct value for a given path.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path of keys to navigate the nested dictionary.
            expected: The expected value to be returned by access_nested_map.

        Asserts:
            The value returned by access_nested_map
            is equal to the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError("a")),
        ({"a": 1}, ("a", "b"), KeyError("b")),
    ])
    def test_access_nested_map_exception(
        self,
        nested_map,
        path,
        expected_exception
    ):
        """
        Test that access_nested_map raises a KeyError for invalid paths.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path of keys to navigate the nested dictionary.
            expected_exception (Exception): The expected exception to be raised

        Asserts:
            A KeyError is raised with the expected message.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(expected_exception))


if __name__ == '__main__':
    unittest.main()

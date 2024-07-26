#!/usr/bin/env python3
"""
A module for testing the access_nested_map function from the utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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


class TestGetJson(unittest.TestCase):
    """
    Contains unit tests for the get_json function.

    get_json is designed to perform an HTTP GET request and return the JSON
    payload from the response.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected JSON payload from a URL.

        Args:
            test_url (str): The URL to request.
            test_payload (dict): The expected JSON payload from the URL.

        Asserts:
            The return value of get_json is equal to the expected payload.
            requests.get is called exactly once with the test_url.
        """
        # Mock the requests.get method
        with patch("requests.get") as mock_get:
            # Set up the mock to return a mock response with the json method
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call get_json and assert it returns the expected payload
            self.assertEqual(get_json(test_url), test_payload)

            # Verify that requests.get was called exactly once with test_url
            mock_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()

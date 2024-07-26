#!/usr/bin/env python3
"""
A module for testing the GithubOrgClient class from the client module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Contains unit tests for the GithubOrgClient class.

    Tests the org method to ensure it returns the correct data without making
    actual HTTP requests.
    """

    @parameterized.expand([
        ("google", {"org": "google"}),
        ("abc", {"org": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_response, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Args:
            org_name (str): The name of the organization to test.
            mock_response (dict): The mock response to be returned by get_json.
            mock_get_json (Mock): The mocked get_json function.

        Asserts:
            - The get_json function is called exactly once
                with the expected URL.
            - The org method returns the correct value.
        """
        mock_get_json.return_value = mock_response

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        self.assertEqual(result, mock_response)


if __name__ == '__main__':
    unittest.main()

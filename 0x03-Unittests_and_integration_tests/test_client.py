#!/usr/bin/env python3
"""
A module for testing the GithubOrgClient class from the client module.
"""

import unittest
from unittest.mock import patch, PropertyMock
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
            - The get_json function is called exactly once with the expected URL.
            - The org method returns the correct value.
        """
        # Create a mock response for get_json
        mock_get_json.return_value = mock_response

        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

        self.assertEqual(result, mock_response)

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that _public_repos_url returns the correct URL based on the org property.

        Args:
            mock_org (PropertyMock): Mocked org property of GithubOrgClient.

        Asserts:
            - The _public_repos_url method returns the correct URL.
        """
        # Define a mock payload for the org property
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        client = GithubOrgClient("google")
        result = client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/google/repos")


if __name__ == '__main__':
    unittest.main()

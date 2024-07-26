#!/usr/bin/env python3
"""Unit and integration tests for the `GithubOrgClient` class.

This module contains tests for the `GithubOrgClient` class from the `client`
module. It verifies the functionality of the class methods and properties,
including:
- `org()`: Retrieves the organization data.
- `_public_repos_url`: Provides the URL for public repositories.
- `public_repos()`: Returns a list of public repositories.
- `has_license()`: Checks if a repository has a specific license.

Tests are performed using mocks and patches to simulate API responses and
validate the behavior of the class.
"""

import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the `GithubOrgClient` class.

    These tests verify the behavior of the `GithubOrgClient` methods and
    properties, ensuring they interact with the GitHub API as expected
    without making actual network calls.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(
        self,
        org_name: str,
        expected_response: Dict,
        mock_get_json: MagicMock
    ) -> None:
        """
        Test the `org` method of `GithubOrgClient`.

        Args:
            org_name (str): The name of the organization to test.
            expected_response (Dict): The expected JSON response from the mock.
            mock_get_json (MagicMock): The mocked `get_json` function.

        Asserts:
            - The `get_json` function is called exactly once
                with the correct URL.
            - The `org` method returns the expected organization data.
        """
        mock_get_json.return_value = expected_response
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_response)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """
        Test the `_public_repos_url` property of `GithubOrgClient`.

        Asserts:
            - The `_public_repos_url` property returns the correct URL based on
              the organization data.
        """
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) \
                as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos"
            }
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url,
                "https://api.github.com/users/google/repos"
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """
        Test the `public_repos` method of `GithubOrgClient`.

        Args:
            mock_get_json (MagicMock): The mocked `get_json` function.

        Asserts:
            - The `public_repos` method returns a list of repository names.
            - The `_public_repos_url` property and `get_json` function
                are called exactly once.
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {"id": 7697149, "name": "episodes.dart", "private": False,
                 "owner": {"login": "google", "id": 1342004}, "fork": False,
                 "url": "https://api.github.com/repos/google/episodes.dart",
                 "created_at": "2013-01-19T00:31:37Z",
                 "updated_at": "2019-09-23T11:53:58Z", "has_issues": True,
                 "forks": 22, "default_branch": "master"},
                {"id": 8566972, "name": "kratu", "private": False,
                 "owner": {"login": "google", "id": 1342004}, "fork": False,
                 "url": "https://api.github.com/repos/google/kratu",
                 "created_at": "2013-03-04T22:52:33Z",
                 "updated_at": "2019-11-15T22:22:16Z", "has_issues": True,
                 "forks": 32, "default_branch": "master"},
            ]
        }
        mock_get_json.return_value = test_payload['repos']
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload['repos_url']
            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["episodes.dart", "kratu"])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """
        Test the `has_license` method of `GithubOrgClient`.

        Args:
            repo (Dict): The repository dictionary to check.
            key (str): The license key to search for.
            expected (bool): Expected boolean result indicating presence of the
                             license.

        Asserts:
            - The `has_license` method returns whether
                the license key is present.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, key), expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the `GithubOrgClient` class.

    These tests ensure that the `GithubOrgClient` interacts with the GitHub
    API correctly and processes responses as expected, simulating actual API
    calls.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up class-level fixtures before running the integration tests.

        Sets up a mock for `requests.get` function to simulate API responses.
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            raise HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """
        Test the `public_repos` method with integration data.

        Asserts:
            - The `public_repos` method returns the correct list
              of repositories based on the integration test data.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """
        Test the `public_repos` method with a license filter using integration
        data.

        Asserts:
            - The `public_repos` method correctly filters
              repositories by license.
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Tear down class-level fixtures after running the integration tests.

        Stops the mock patch for `requests.get`.
        """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()

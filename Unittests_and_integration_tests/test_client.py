#!/usr/bin/env python3

"""
Tests for functions in client module
"""

from typing import Any, Dict, List
from client import GithubOrgClient
import unittest
from unittest.mock import Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_url, mock_get_json):
        """Tests that GithubOrgClient.org returns correct value
        """
        request = GithubOrgClient(org_url)
        # below works because org method just needs to be called
        # () not needed because memoize decorator on org saves as property
        request.org
        mock_get_json.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=org_url)
        )

    def test_public_repos_url(self):
        """Tests that _public_repos_url returns mocked payload
        """
        # example JSON return from org containing repos_url key
        known_payload: dict = {"repos_url": "https://example.com/test"}
        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = known_payload
            request = GithubOrgClient("test")
            result = request._public_repos_url

            self.assertEqual(result, known_payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Tests public_repos for correct output
        """
        my_payload: str = "https://example.com/test"
        site_name_1: str = "foo"
        site_name_2: str = "bar"
        mock_get_json.return_value = ([
            {"name": site_name_1},
            {"name": site_name_2}
        ])
        with patch.object(
            GithubOrgClient, "_public_repos_url", new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = my_payload
            request = GithubOrgClient("test")
            result = request.public_repos()

            self.assertEqual(result, [site_name_1, site_name_2])
            mock_get_json.assert_called_once()

    @parameterized.expand([
        # (repo, license, expected)
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """Tests has_license output for matching/invalid license keys
        """
        request = GithubOrgClient("test")
        repo_has_license: bool = request.has_license(repo, license)

        self.assertEqual(repo_has_license, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    # TEST_PAYLOAD has exactly four elements in the same order as above
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test suite for GithubOrgClient
    """
    # types defined for parameterized_class attributes for pyright
    org_payload: Dict[str, str]
    repos_payload: List[Dict[str, Any]]
    expected_repos: List[str]
    apache2_repos: List[str]

    @classmethod
    def setUpClass(cls):
        """Sets up class for testing
        """
        def get_payload(url):
            """Gets mock response from url
            """
            mock_response = Mock()
            org_pattern = GithubOrgClient.ORG_URL.format(org="google")

            if url == org_pattern:
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload.get("repos_url"):
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = {}

            return mock_response

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tears down class after testing
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests that public_repos method gets correct data from fixtures
        """
        request = GithubOrgClient("google")
        self.assertEqual(request.public_repos(), self.expected_repos)

#!/usr/bin/env python3

"""
Tests for functions in client module
"""

from typing import Any, Mapping, Sequence
from unittest import mock
from client import GithubOrgClient
import unittest
from unittest.mock import Mock, PropertyMock, patch
from parameterized import parameterized


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

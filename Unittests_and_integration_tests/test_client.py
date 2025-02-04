#!/usr/bin/env python3

"""
Tests for functions in client module
"""

from typing import Any, Mapping, Sequence
from unittest import mock
from client import GithubOrgClient
import unittest
from unittest.mock import Mock, patch
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

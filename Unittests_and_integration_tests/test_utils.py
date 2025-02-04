#!/usr/bin/env python3

"""
Tests for functions in utils module
"""

from typing import Any, Mapping, Sequence
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for access_nested_map
    """
    @parameterized.expand([
        # (nested_map, path, expected)
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self, nested_map: Mapping, path: Sequence, expected: Any
    ):
        """test access_nested_map for correct inputs
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(
        self, nested_map: Mapping, path: Sequence
    ):
        """test access_nested_map for faulty inputs
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test suite for get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """test get_json with mocked requests object
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Test suite for memoize
    """
    class TestClass:

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, "a_method")
    def test_memoize(self, mock_a_method):
        """test memoize for single a_method call
        """
        mock_a_method.return_value = 42
        test_object = self.TestClass()
        result_1 = test_object.a_property
        result_2 = test_object.a_property

        mock_a_method.assert_called_once()
        self.assertEqual(result_1, result_2)

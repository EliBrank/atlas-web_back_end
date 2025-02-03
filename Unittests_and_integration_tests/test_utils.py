#!/bin/bin/env python3

from typing import Any, Mapping, Sequence
from utils import access_nested_map
import unittest
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
        """test access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

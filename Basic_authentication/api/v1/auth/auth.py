#!/usr/bin/env python3
"""
Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manages API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Specifies auth requirement for endpoint
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Gets authorization header
        """
        return None  # pyright: ignore

    def current_user(self, request=None) -> TypeVar("User"):  # pyright: ignore
        """Gets user
        """
        return None  # pyright: ignore

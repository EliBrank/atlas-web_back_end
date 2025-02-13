#!/usr/bin/env python3
"""
Auth module
"""

from flask import request
from typing import List, TypeVar, Union


class Auth:
    """
    Manages API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Specifies auth requirement for endpoint
        """
        if not path or not excluded_paths:
            return True
        if path[-1] != "/":
            path += "/"
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> Union[str, None]:
        """Gets authorization header
        """
        if not request or "Authorization" not in request.headers:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar("User"):  # pyright: ignore
        """Gets user
        """
        return None  # pyright: ignore

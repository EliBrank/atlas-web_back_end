#!/usr/bin/env python3
"""
Auth module
"""

import os
from flask import request
from typing import List, Optional, TypeVar, Union


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
        return None  # type: ignore

    def session_cookie(self, request=None):
        """Gets cookie value from request object
        """
        if not request:
            return
        session: Optional[str] = os.getenv("SESSION_NAME")
        session_cookie: str = request.cookies.get(session)

        return session_cookie

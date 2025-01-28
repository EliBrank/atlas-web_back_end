#!/usr/bin/env python3
"""
BasicAuth module
"""

from api.v1.auth.auth import Auth
from typing import Optional, Optional
import base64
import binascii
from api.v1.views.users import User


class BasicAuth(Auth):
    """
    BasicAuth authenication implementation
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> Optional[str]:
        """Takes base64 component from auth value of request header
        """
        if (
            not authorization_header
            or not isinstance(authorization_header, str)
            or not authorization_header.startswith("Basic ")
        ):
            return
        extracted_base64: str = authorization_header.split("Basic ", 1)[1]

        return extracted_base64

    def decode_base64_authorization_header(
            self, base64_authorization_header: Optional[str]
    ) -> Optional[str]:
        """Decodes extracted base64 string from request header
        """
        if (
            not base64_authorization_header
            or not isinstance(base64_authorization_header, str)
        ):
            return

        decoded_string: Optional[str] = None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode("utf-8")
        except (binascii.Error, UnicodeDecodeError):
            return

        return decoded_string

    def extract_user_credentials(
            self, decoded_base64_authorization_header: Optional[str]
    ) -> tuple[Optional[str], Optional[str]]:
        """Gets user email, password from request header
        """
        if (
            not decoded_base64_authorization_header
            or not isinstance(decoded_base64_authorization_header, str)
            or ":" not in decoded_base64_authorization_header
        ):
            return (None, None)

        email, password = decoded_base64_authorization_header.split(":", 2)

        return (email, password)

    def user_object_from_credentials(
            self, user_email: Optional[str], user_pwd: Optional[str]
    ) -> Optional[User]:
        """Gets user instance from credentials
        """
        if (
            not user_email
            or not user_pwd
            or not isinstance(user_email, str)
            or not isinstance(user_pwd, str)
        ):
            return

        try:
            users: list[User] = User.search({"email": user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return

    def current_user(self, request=None) -> Optional[User]:
        """Gets user instance from request object
        """
        auth_header: Optional[str] = self.authorization_header(request)

        auth_header_b64: Optional[str] = (
            auth_header
            and self.extract_base64_authorization_header(auth_header)
        )

        auth_header_decoded: Optional[str] = (
            auth_header_b64 and
            self.decode_base64_authorization_header(auth_header_b64)
        )

        credentials: tuple[Optional[str], Optional[str]] = (
            self.extract_user_credentials(auth_header_decoded)
            if auth_header_decoded else (None, None)
        )

        user: Optional[User] = (
            self.user_object_from_credentials(*credentials)
            if credentials
            and credentials[0] is not None
            and credentials[1] is not None
            else None
        )

        return user

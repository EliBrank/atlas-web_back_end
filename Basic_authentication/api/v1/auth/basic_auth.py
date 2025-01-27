#!/usr/bin/env python3
"""
BasicAuth module
"""

from api.v1.auth.auth import Auth
from typing import Union
import base64
import binascii


class BasicAuth(Auth):
    """
    BasicAuth authenication implementation
    """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> Union[str, None]:
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
            self, base64_authorization_header: str
    ) -> Union[str, None]:
        """Decodes extracted base64 string from request header
        """
        if (
            not base64_authorization_header
            or not isinstance(base64_authorization_header, str)
        ):
            return

        decoded_string: Union[str, None] = None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_string = decoded_bytes.decode("utf-8")
        except binascii.Error:
            return

        return decoded_string

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> tuple[Union[str, None], Union[str, None]]:
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

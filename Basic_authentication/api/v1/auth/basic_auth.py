#!/usr/bin/env python3
"""
BasicAuth module
"""

from api.v1.auth.auth import Auth
from typing import Union


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

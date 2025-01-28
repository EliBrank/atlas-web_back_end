#!/usr/bin/env python3
"""
SessionAuth module
"""

import uuid
from api.v1.auth.auth import Auth
from typing import Optional


class SessionAuth(Auth):
    """
    SessionAuth authenication implementation
    """
    user_id_by_session_id: dict = {}

    def create_session(self, user_id: Optional[str] = None) -> Optional[str]:
        """Creates session ID for given user ID
        """
        if not user_id or not isinstance(user_id, str):
            return
        session_id: str = str(uuid.uuid4())

        self.user_id_by_session_id.update({session_id: user_id})

        return session_id

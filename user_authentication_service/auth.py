#!/usr/bin/env python3

"""
Auth module
"""
from typing import Optional, cast
import bcrypt
from db import DB
from user import User
import uuid
try:
    # Older SQLAlchemy
    from sqlalchemy.orm.exc import NoResultFound  # pyright: ignore
except ImportError:
    from sqlalchemy.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Creates hash of input password with bcrypt

    Args:
        password: String to be hashed, salted

    Return:
        Hashed bytes object from password
    """
    pw_bytes: bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    pw_hashed: bytes = bcrypt.hashpw(pw_bytes, salt)

    return pw_hashed


def _generate_uuid() -> str:
    """Creates UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with authentication database
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Creates user object from email, password
        """
        try:
            if self._db.find_user_by(email=email):
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password: str = str(_hash_password(password))
        return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Checks for user, ensures password is correct
        """
        try:
            user: User = self._db.find_user_by(email=email)
            pw_bytes: bytes = password.encode("utf-8")
            hashed_pw_bytes: bytes = (
                user.hashed_password.strip("b\'\'").encode("utf-8")
            )
            return bcrypt.checkpw(pw_bytes, hashed_pw_bytes)
        except NoResultFound:
            pass

        return False

    def create_session(self, email: str) -> str:
        """Creates new session based on input user email
        """
        try:
            user: User = self._db.find_user_by(email=email)
            session_id: str = _generate_uuid()
            user_id: int = cast(int, user.id)
            self._db.update_user(user_id, session_id=session_id)
            return session_id
        except NoResultFound:
            pass

        return ""

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """Gets user object tied to current session
        """
        if not session_id:
            return
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return

    def destroy_session(self, user_id: int) -> None:
        """Deletes user session
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except ValueError:
            pass

        return None

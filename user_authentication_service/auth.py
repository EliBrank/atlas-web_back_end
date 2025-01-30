#!/usr/bin/env python3

"""
Auth module
"""
import bcrypt
from db import DB
from user import Base, User
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
            if user:
                pw_bytes: bytes = password.encode("utf-8")
                hashed_pw_bytes: bytes = (
                    user.hashed_password.strip("b\'\'").encode("utf-8")
                )
                return bcrypt.checkpw(pw_bytes, hashed_pw_bytes)
        except NoResultFound:
            pass

        return False

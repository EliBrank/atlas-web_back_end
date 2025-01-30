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




class Auth:
    """Auth class to interact with authentication database
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
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

    def register_user(self, email: str, password: str) -> User:
        """Creates user object from email, password
        """
        try:
            if self._db.find_user_by(email=email):
                raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass

        hashed_password: str = str(self._hash_password(password))
        return self._db.add_user(email, hashed_password)

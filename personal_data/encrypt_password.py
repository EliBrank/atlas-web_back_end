#!/usr/bin/env python3

"""Encrypts and checks passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks if password matches provided hash

    Args:
        hashed_password: Hashed string to check password against
        password: Unhashed string to check

    Return:
        True if password and hash match, else false
    """
    pw_bytes: bytes = password.encode("utf-8")

    return bcrypt.checkpw(pw_bytes, hashed_password)

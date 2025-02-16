#!/usr/bin/env python3

"""
Main exercise module
"""

import redis
from uuid import uuid4
from typing import Callable, Optional, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count calls to decorated function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """Simple cache class using redis
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Saves input data to database with generated uuid key
        """
        generated_key: str = str(uuid4())
        self._redis.set(generated_key, data)

        return generated_key

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        """Retrieves value from cache
        Args:
            key: String used to fetch value
            fn: Optional function to convert
        Returns:
            Value stored in input key, if any
        """
        value_bytes = self._redis.get(key)
        if value_bytes and fn:
            return fn(value_bytes)
        return value_bytes  # pyright: ignore

    def get_str(self, data: bytes) -> str:
        """Returns given data as a string
        """
        return str(data)

    def get_int(self, data: bytes) -> int:
        """Returns given data as an integer
        """
        return int(data)

#!/usr/bin/env python3

"""
Main exercise module
"""

import redis
from uuid import uuid4
from typing import Callable, Optional, Union


class Cache():
    """Simple cache class using redis
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Saves input data to database with generated uuid key
        """
        generated_key: str = str(uuid4())
        self._redis.set(generated_key, data)

        return generated_key

    def get(
        self, key: str, fn: Optional[Callable]
    ) -> Optional[Union[str, bytes, int, float]]:
        """Retrieves value from cache
        Args:
            key: String used to fetch value
            fn: Optional function to convert
        Returns:
            Value stored in input key, if any
        """
        value_bytes = self._redis.get(key)
        return ""

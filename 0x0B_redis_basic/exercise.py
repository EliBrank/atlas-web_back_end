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
        # actual method call here
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to log in/output for decorated function
    """
    inputs_key: str = f"{method.__qualname__}:inputs"
    outputs_key: str = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs_key, str(args))
        # actual method call here
        output_value = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, output_value)
        return output_value
    return wrapper


class Cache():
    """Simple cache class using redis
    """
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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

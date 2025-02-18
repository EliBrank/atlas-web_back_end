#!/usr/bin/env python3

"""
Main exercise module
"""

import redis
from uuid import uuid4
from typing import Callable, Optional, Union
from functools import wraps
import inspect


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


def replay(method: Callable) -> None:
    """Displays information logged via call_history/count_calls
    """
    # check to make sure method has __self__
    if not hasattr(method, "__self__"):
        raise TypeError("Expected bound method")
    instance = method.__self__  # pyright: ignore

    # use short circuit for None case since int() can't convert None
    call_count = instance._redis.get(method.__qualname__) or 0
    call_count = int(call_count)

    print(f"{method.__qualname__} was called {call_count} "
          f"time{'s' if call_count != 1 else ''}:")

    inputs_key: str = f"{method.__qualname__}:inputs"
    outputs_key: str = f"{method.__qualname__}:outputs"
    inputs = instance._redis.lrange(inputs_key, 0, -1)
    outputs = instance._redis.lrange(outputs_key, 0, -1)

    for input, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input.decode('utf-8')}) -> "
              f"{output.decode('utf-8')}")


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

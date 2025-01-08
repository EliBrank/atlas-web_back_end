#!/usr/bin/env python3

"""Defines to_kv function"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Squares input value and assigns it to a key/value pair

    Args:
        k: string which becomes key in key/value pair
        v: float or integer which is squared and made value in key/value pair

    Returns:
        Tuple containing key/value pair (string and squared float/integer)
    """

    return (k, v * v)

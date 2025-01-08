#!/usr/bin/env python3

from typing import Tuple, Union

"""Defines to_kv function"""


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """Squares input value and assigns it to a key/value pair

    Args:
        k: string which becomes key in key/value pair
        v: float or integer which is squared and made value in key/value pair

    Returns:
        Tuple containing key/value pair (string and squared float/integer)
    """

    return (k, v * v)

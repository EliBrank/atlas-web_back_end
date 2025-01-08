#!/usr/bin/env python3

from typing import Callable

"""Defines make_multiplier function"""

# the Callable type hint has this format: Callable[[param_type], return_type]
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Creates function which multiplies input by multiplier

    Args:
        multiplier: value used to multiply input in returned function

    Returns:
        New function which multiplies input by multiplier given here
    """

    def multiply_func(n: float) -> float:
        """Multiplies input by value (determined by make_multiplier)"""
        return (n * multiplier)

    return multiply_func

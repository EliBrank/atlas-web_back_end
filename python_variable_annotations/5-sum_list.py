#!/usr/bin/env python3

"""Defines sum_list function"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Adds together all values in a list

    Args:
        input_list: list of floats

    Returns:
        Sum of all floats in input list
    """

    return sum(input_list)

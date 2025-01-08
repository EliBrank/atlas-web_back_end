#!/usr/bin/env python3

"""Defines sum_mixed_list function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Adds together all values (floats or integers) in a list

    Args:
        mxd_lst: list of floats and/or integers

    Returns:
        Sum of all floats/integers in input list (as a float)
    """

    return sum(mxd_lst)

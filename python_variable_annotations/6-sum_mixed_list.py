#!/usr/bin/env python3

from typing import List, Union

"""Defines sum_mixed_list function"""


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Adds together all values (floats or integers) in a list

    Args:
        mxd_lst: list of floats and/or integers

    Returns:
        Sum of all floats/integers in input list (as a float)
    """

    return sum(mxd_lst)

#!/usr/bin/env python3

"""Defines element_length function"""

from typing import List, Tuple, Iterable, Sequence


# Iterable here can be list, generator, etc
# Sequence can be list, tuple, etc
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """For each sequence in iterable, create new tuple with
    sequence and length and add to a list

    Args:
        lst: iterable containing sequence(s)

    Returns:
        List of tuples, each containing sequence, sequence length from lst
    """
    return [(i, len(i)) for i in lst]

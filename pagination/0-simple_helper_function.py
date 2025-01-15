#!/usr/bin/env python3

"""defines index_range function"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start and end indices for a given page, page size

    Args:
        page: number of the requested page
        page_size: number of items per page

    Returns:
        start, end indices for elements on a given page
    """
    first_item_index: int = (page - 1) * page_size
    last_item_index: int = first_item_index + page_size

    return (first_item_index, last_item_index)

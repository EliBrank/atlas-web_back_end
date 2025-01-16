#!/usr/bin/env python3

"""set up pagination for baby name dataset"""

from typing import List, Tuple
import csv


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


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves entries list from specified page, given page size

        Args:
            page: number of the requested page
            page_size: number of items per page

        Returns:
            List of entries from provided page number
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        indices: Tuple[int, int] = index_range(page, page_size)
        start_index, end_index = indices

        current_page: slice = slice(start_index, end_index)

        return self.dataset()[current_page]

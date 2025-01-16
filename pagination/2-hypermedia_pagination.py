#!/usr/bin/env python3

"""set up advanced pagination for baby name dataset"""

from typing import Any
import csv
import math


def index_range(page: int, page_size: int) -> tuple[int, int]:
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

    def dataset(self) -> list[list]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> list[list]:
        """Retrieves entries list from specified page, given page size

        Args:
            page: number of the requested page
            page_size: number of items per page

        Returns:
            List of entries from provided page number
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        indices: tuple[int, int] = index_range(page, page_size)
        start_index, end_index = indices

        current_page: slice = slice(start_index, end_index)

        return self.dataset()[current_page]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict[str, Any]:
        """Retrieves various information for page of dataset

        Args:
            page_size: length of returned dataset page
            page: current page number
            data: dataset page (calculated from get_page)
            next_page: number of next page, None if no next page
            prev_page: number of previous page, None if no previous page
            total_pages: total number of pages in the dataset

        Returns:
            Dictionary containing relevant page info in key-value pairs
        """
        data: list[list] = self.get_page(page, page_size)
        dataset_length: int = len(self.dataset())
        # page size is cast as float to properly round result (as float) up
        total_pages: int = math.ceil(dataset_length / float(page_size))
        next_page: int | None = page + 1 if page < total_pages else None
        prev_page: int | None = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

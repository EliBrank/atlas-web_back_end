#!/usr/bin/env python3

"""Deletion-resilient hypermedia pagination"""

import csv


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> list[list]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, list]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int | None = None,
                        page_size: int = 10) -> dict:
        """Retrieves various information for dataset page (deletion resilient)

        Args:
            index: current start index of return page
            next_index: first index after last item index on the current page
            page_size: current page size
            data: dataset page

        Returns:
            Dictionary containing relevant page info in key-value pairs
        """
        dataset: dict = self.indexed_dataset()
        dataset_length: int = len(dataset)

        assert type(index) is int and type(page_size) is int
        assert index >= 0 and index < dataset_length
        assert page_size > 0

        data: list = []
        current_index: int = index

        while len(data) < page_size:
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1
            if current_index > dataset_length:
                break

        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": current_index
        }

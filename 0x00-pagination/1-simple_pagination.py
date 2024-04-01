#!/usr/bin/env python3
""" This is a simple pagination module"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ This is a helper function
    @page: Takes page as argument
    @page_size: Takes a page size as argument
    Return: Returns a tuple
    """
    start_index = (page_size * (page - 1))
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
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
        """ This is the get_page function
        @page: the page number
        @page_size: the size of items to return
        Return: List of pages to fetch
        """
        for values in [page, page_size]:
            assert isinstance(values, int)
            assert values > 0
        (start_index, end_index) = index_range(page, page_size)
        data_set_value = self.dataset()
        if end_index > len(data_set_value):
            return []
        return data_set_value[start_index:end_index]

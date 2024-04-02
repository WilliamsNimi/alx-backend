#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ This is the hyper index function
        @index: The index to be searched for
        @page_size: the size of the list returned
        Return: Returns a dictionary of values
        """
        indices = self.indexed_dataset()
        assert isinstance(index, int) and index < len(indices) - 1
        data_partition = []
        page = 0
        data_pointer = index
        next_index = None
        while page < page_size:
            value = indices.get(page + index, None)
            page = page + 1
            if value:
                data_partition.append(value)
                data_pointer = data_pointer + 1

        while data_pointer < len(indices):
            value = indices.get(data_pointer, None)
            if value:
                next_index = data_pointer
                break
            data_pointer = data_pointer + 1

        hyper_index = {}
        hyper_index['index'] = index
        hyper_index['next_index'] = next_index
        hyper_index['page_size'] = page_size
        hyper_index['data'] = data_partition

        return (hyper_index)

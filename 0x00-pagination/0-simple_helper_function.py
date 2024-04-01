#!/usr/bin/env python3
""" A helper function """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ This is a helper function
    @page: Takes page as argument
    @page_size: Takes a page size as argument
    Return: Returns a tuple
    """
    start_index = (page_size * (page - 1))
    end_index = start_index + page_size
    return (start_index, end_index)

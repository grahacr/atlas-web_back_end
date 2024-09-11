#!/usr/bin/env python3
'''
module implements index_range global function and class Server to
access and use the dataset of Popular Baby Names (csv file)
'''
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    index_rangs funtion takes 2 arguments:
    - page (int)
    - page_size (int)
    Return:
    - Tuple (ints)
    '''
    start_index = int((page - 1) * page_size)
    end_index = int(start_index + page_size)
    range = (start_index, end_index)
    return range


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
        '''
        get_page takes 3 arguments:
        - self
        -page (int, default of 1)
        -page_size (int, default of 10)
        -Return: list of data if index is in range
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start:end] if start < len(dataset) else []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''
        get_hyper takes 3 arguments:
        - self
        - page (int, default = 1)
        - page_size (int, default = 10)
        Return:
        - Dictionary "result" containing hypermedia key:value pairs
        '''
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = int(math.ceil(total_items / page_size))
        has_prev = page > 1
        has_next = page < total_pages

        result = {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": page + 1 if has_next else None,
            "prev_page": page - 1 if has_prev else None,
            "total_pages": total_pages
        }
        return result

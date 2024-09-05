#!/usr/bin/env python3
'''
module provides simple helper function for returning an
index range to utilize for pagination
'''
from typing import Tuple


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

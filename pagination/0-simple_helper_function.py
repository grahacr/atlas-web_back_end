#!/usr/bin/env python3
'''
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start_index = int((page - 1) * page_size)
    end_index = int(start_index + page_size)
    range = (start_index, end_index)
    return range

#!/usr/bin/env python3
'''
using type annotation, this module includes a function sum_list
which will return the sum of all float types within a list
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    function sum_list takes in one argument: input_list (list of float types)
    return: sum of all float types within the list
    '''
    return sum(input_list)

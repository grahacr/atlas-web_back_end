#!/usr/bin/env python3
'''
using type annotation, this module includes a function sum_mixed_list
which will return the sum of both the integers and floats in the List
and returns in float type
'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    '''
    function sum_mixed_list takes in one argument: mxd_list (list of both float and int types)
    return: return sum of both ints and floats within the list, utilizing Union from typing module
    '''
    return float(sum(mxd_list))

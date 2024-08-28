#!/usr/bin/env python3
'''
module adds type annotation to the element_length function
utilizing List and Tuple from typing module
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    function element_length takes one argument:
    - lst (a list of string data types)
    Returns:
    - a list of tuples, starting with string type, and then int type
    - The tuple contains the list element and then length of that element
    '''
    return [(i, len(i)) for i in lst]

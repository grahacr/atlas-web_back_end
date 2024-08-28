#!/usr/bin/env python3
'''
module adds type annotation to the element_length function
utilizing List and Tuple from typing module
'''
from typing import List, Tuple
'''
function element_length takes one argument:
- lst (a list of string data types)
Returns:
- a list of tuples, starting with string type, and then int type
- The tuple contains the list element and then length of that element
'''
def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]

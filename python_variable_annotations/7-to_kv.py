#!/usr/bin/env python3
'''
using type annotation, this module uses the typing module
for to_kv function, which uses type annotation to return a tuple
with a string and the value of either the int or float squared
'''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str,float]:
    '''
    function to_kv takes 2 arguments:
    k = string
    v = either int or float
    return: tuple with string first and then squared int or float
    in format of float
    '''
    squared = float(v ** 2)
    return (k, squared)

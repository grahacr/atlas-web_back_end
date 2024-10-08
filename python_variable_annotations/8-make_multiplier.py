#!/usr/bin/env python3
'''
this module utilizes the typing module to create a function:
make_multiplier will return a multiplier function that can be used as an object
due to closures and using Callable
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    make_multiplier takes one argument:
    - multiplier (float type)
    Returns: a function multiplier_function
    to be stored in an object and utilized as multiplier
        - inner function takes one argument(a float),
        - returns the multiplied value using the multiplier value
        from the scope of the original function
    '''
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function

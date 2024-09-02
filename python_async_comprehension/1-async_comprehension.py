#!/usr/bin/env python3
'''
use imported async_generator function
and generate 10 random numbers using async_comprehension
'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    async_comprehension takes no arguments.
    Returns:
    List of floats, from async_generator
    '''
    return [num async for num in async_generator()]

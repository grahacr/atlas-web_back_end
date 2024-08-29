#!/usr/bin/env python3
'''
module utilizes typing, random, and asyncio packages
imports a function to generate a random delay
function wait_n takes 2 integers as an argument to return a list of
delays, generated due to multiple coroutines running
at the same time with async
'''
from typing import List
import random
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    function wait_n takes two arguments:
    - n (integer)
    - max_delay (integer)
    Returns:
    - List of floats
    Function generates list of delays (float values) as coroutines
    are being executed, then returns that list
    '''
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        index = 0
        while index < len(delays) and delays[index] < delay:
            index += 1
        delays.insert(index, delay)

    return delays

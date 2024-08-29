#!/usr/bin/env python3
'''

'''
from typing import List
import random
import asyncio
wait_random = __import__('0-basic-async-syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        index = 0
        while index < len(delays) and delays[index] < delay:
            index += 1
        delays.insert(index, delay)

    return delays

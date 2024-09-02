#!/usr/bin/env python3
'''
use imported async_comprehension function
and measure the time it takes to run it 4 times
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''
    '''
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    elapsed_time = end_time - start_time
    return float(elapsed_time)

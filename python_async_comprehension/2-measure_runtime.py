#!/usr/bin/env python3
'''
use imported async_generator function
and generate 10 random numbers using async_comprehension
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''
    '''
    start_time = time.time()
    results = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    elapsed_time = end_time - start_time
    return float(elapsed_time)

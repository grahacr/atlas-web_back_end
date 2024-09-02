#!/usr/bin/env python3
'''
use imported async_comprehension function
and write new function that will measure
the time it takes to run imported function 4 times
'''
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    measure_runtime: no arguments,
    returns: float representing amount of time it took
    to execute the imported function 4 times, utilizing gather
    '''
    start_time = time.time()
    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return float(elapsed_time)

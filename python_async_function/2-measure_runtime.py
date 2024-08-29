#!/usr/bin/env python3
'''
module utilizes time and asyncio packages for measure_time function
function measures total elapsed time for running wait_n function
'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    measure_time takes two arguments:
    - n (int)
    - max_delay (int)
    Returns: float which represents the total elapsed time
    that it took to complete the wait_n function
    utilizing time module
    '''
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    elapsed_time = end_time - start_time
    return float(elapsed_time)

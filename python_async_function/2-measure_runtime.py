#!/usr/bin/env python3
'''
'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
   start_time = time.time()
   await wait_n(n, max_delay)
   end_time = time.time()
   elapsed_time = end_time - start_time
   return float(elapsed_time)

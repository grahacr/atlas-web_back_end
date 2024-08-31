#!/usr/bin/env python3
'''
module includes an async_generator utilizing the following modules:
asyncio, random, and AsyncGenerator from typing to accomplish the function
of generating a random number after asynchronous delays
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    async_generator takes no arguments.
    it will asychronously wait 1 second, then
    yield a random integer between 0 and 10
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

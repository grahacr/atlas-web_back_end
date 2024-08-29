#!/usr/bin/env python3
'''
this module utilizes the random and asyncio modules
includes function wait_random which sets a randomly generated
delay for the asynchronous program
'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    function wait_random takes one argument:
    - max_delay = integer of 10
    Returns:
    - float representing randomly generated delay
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

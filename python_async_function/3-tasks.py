#!/usr/bin/env python3
'''
module utilizes asyncio and imported function wait_random
includes function task_wait_random which returns asyncio task
'''

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    task_wait_random takes one argument:
    - max_delay (int)
    Returns:
    asyncio Task, which wraps around the wait_random coroutine
    '''
    return asyncio.create_task(wait_random(max_delay))

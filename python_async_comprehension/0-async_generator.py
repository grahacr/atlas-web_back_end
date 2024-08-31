#!/usr/bin/env python3

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[int, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)

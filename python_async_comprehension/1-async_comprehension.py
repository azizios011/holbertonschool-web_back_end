#!/usr/bin/env python3


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ a coroutine called 'async_generator' """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        
async def async_comprehension():
    numbers = [num async for num in async_generator()]
    return numbers

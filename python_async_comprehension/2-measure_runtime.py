#!/usr/bin/env python3
"""a 'measure_runtime' coroutine """


import asyncio
import asyncio.tasks
import random
from typing import Generator
from typing import List


async def async_generator() -> Generator[float, None, None]:
    """ a coroutine called 'async_generator' """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """a coroutine called 'async_comprehension' """
    numbers = [num async for num in async_generator()]
    return numbers


async def measure_runtime() -> float:
    coroutines = [async_comprehension() for _ in range(4)]
    results = await asyncio.gather(*coroutines)
    return sum(len(result) for result in results)
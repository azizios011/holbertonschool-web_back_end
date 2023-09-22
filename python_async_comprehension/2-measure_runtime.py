#!/usr/bin/env python3
"""a 'measure_runtime' coroutine """


import asyncio
import asyncio.tasks
import random
import time
from typing import Generator
from typing import List
from time import perf_counter


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
    """Measure the total runtime of four parallel async comprehensions."""
    start_time = asyncio.get_event_loop().time()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time

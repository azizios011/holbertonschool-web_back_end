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


async def measure_runtime() -> bool:
    start_time = perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = perf_counter()
    total_runtime = end_time - start_time
    allowed_runtime = 10.0 + (10.0 * 0.1)
    return total_runtime <= allowed_runtime

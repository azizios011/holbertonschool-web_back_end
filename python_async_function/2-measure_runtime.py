#!/usr/bin/env python3
"""# Define a 'measure_time' function that
takes 'n' and 'max_delay' as arguments"""


import time
import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    return uniform(0, max_delay)


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


def measure_time(n: int, max_delay: int) -> float:
    """Start a timer"""
    start = time.time()
    """Call the wait_n function with 'n' and 'max_delay' """
    asyncio.run(wait_n(n, max_delay))
    """Stop the timer"""
    end = time.time()
    """Calculate the total execution time"""
    total_time = end - start
    """eturn the average execution time per coroutine"""
    return total_time / n

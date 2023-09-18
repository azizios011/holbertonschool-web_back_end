#!/usr/bin/env python3
"""User request"""


import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    """
    Generate a random delay between 0 and max_delay.

    Args:
        max_delay (int): The maximum delay value.

    Returns:
        float: A random delay between 0 and max_delay.
    """
    return uniform(0, max_delay)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute multiple coroutines concurrently and return their
    delays in ascending order.

    Args:
        n (int): The number of coroutines to execute.
        max_delay (int): The maximum delay value for each coroutine.

    Returns:
        List[float]: A list of delays (float values) in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


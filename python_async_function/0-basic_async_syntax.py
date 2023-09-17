#!/usr/bin/env python3
""" an asynchronous coroutine 'wait_random' """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay (inclusive) seconds.
    
    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: The random delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay

if __name__ == "__main__":
    asyncio.run(wait_random())

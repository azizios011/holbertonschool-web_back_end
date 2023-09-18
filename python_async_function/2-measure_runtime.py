#!/usr/bin/env python3

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
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n

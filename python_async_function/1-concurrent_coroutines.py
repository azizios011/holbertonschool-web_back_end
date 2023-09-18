#!/usr/bin/env python3

import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    return uniform(0, max_delay)


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

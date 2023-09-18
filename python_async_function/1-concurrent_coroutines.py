#!/usr/bin/env python3
""" user request """


import asyncio
from typing import List
from random import uniform


""" an asynchronous coroutine 'wait_random' """


async def wait_random(max_delay: int) -> float:
    return uniform(0, max_delay)


"""n async routine called wait_n"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


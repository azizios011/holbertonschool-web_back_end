#!/usr/bin/env python3
""" an function 'task_wait_n' """


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns the list of all the delays (float values) of each task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed, _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    result_list = [t.result() for t in completed]
    return sorted(result_list)

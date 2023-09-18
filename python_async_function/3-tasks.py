#!/usr/bin/env python3
"""a function 'task_wait_random' """


import asyncio
from random import uniform


async def wait_random(max_delay: int) -> float:
    """ an asynchronous coroutine 'wait_random' """
    return uniform(0, max_delay)


def task_wait_random(max_delay):
    loop = asyncio.get_event_loop()
    """ 'asyncio.create_task(wait_random(max_delay))',
    which will execute 'wait_random' asynchronously."""
    task = asyncio.create_task(wait_random(max_delay))
    return task

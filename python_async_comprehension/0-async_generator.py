#!/usr/bin/env python3
""" a coroutine called 'async_generator' """


import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Loop 10 times"""
    for _ in range(10):
        """ Wait for 1 second asynchronously"""
        await asyncio.sleep(1)
        """Yield a random float between 0 and 10"""
        yield random.uniform(0, 10)

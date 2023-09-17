#!/usr/bin/env python3
import asyncio
import random
from typing import Union

async def wait_random(max_delay: Union[int, float] = 10) -> float:
    # Generate a random delay between 0 and max_delay
    delay: float = random.uniform(0, max_delay)
    
    # Sleep for the random delay
    await asyncio.sleep(delay)
    
    return delay
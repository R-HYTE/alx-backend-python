#!/usr/bin/env python3
"""
Includes the wait_n coroutine to demonstrate concurrent execution of coroutines
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute the wait_random coroutine n times with the specified max_delay.

    Args:
        n (int): The number of times to wait.
        max_delay (int): The maximum delay passed to wait_random.

    Returns:
        List[float]: A list of float values representing the delays,
            returned in the order they were completed.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return sorted(completed_delays)

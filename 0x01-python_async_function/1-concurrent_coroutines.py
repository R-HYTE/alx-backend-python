#!/usr/bin/env python3
"""
Includes the wait_n coroutine to demonstrate concurrent execution of coroutines
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Execute the wait_random coroutine n times with the specified max_delay.

    Args:
        n (int): The number of times to wait.
        max_delay (int): The maximum delay passed to wait_random.

    Returns:
        list: A list of float values representing the delays,
            returned in the order they were completed.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = []
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        completed_delays.append(result)
    return completed_delays

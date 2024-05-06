#!/usr/bin/env python3
"""
Provides a function task_wait_n that creates and gathers
multiple asyncio.Tasks with random delays.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously create and gather multiple tasks that
    wait for a random delay.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay, in seconds, for each task.

    Returns:
        List[float]: A list of floats representing the delays experienced
        by each task, sorted in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_delays = await asyncio.gather(*tasks)
    return sorted(completed_delays)

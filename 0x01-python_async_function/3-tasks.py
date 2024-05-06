#!/usr/bin/env python3
"""
Defines a function to create an asyncio.Task that awaits
a random delay based on max_delay.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create and return an asyncio.Task that waits for a random delay.

    Args:
        max_delay (int):  The maximum delay, in seconds, the task will wait.

    Returns:
        asyncio.Task: Task that runs a coroutine waiting for
        a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))

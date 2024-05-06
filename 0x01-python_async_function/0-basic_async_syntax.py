#!/usr/bin/env python3
"""
This module provides an asynchronous coroutine, wait_random,
which simulates waiting for a random amount of time
based on a specified maximum delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random amount of time between 0 and max_delay seconds.

    Args:
    max_delay (int): The maximum number of seconds to wait; defaults to 10.

    Returns:
    float: The actual number of seconds waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

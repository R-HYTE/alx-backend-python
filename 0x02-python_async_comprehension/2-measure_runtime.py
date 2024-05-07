#!/usr/bin/env python3
"""
Module to measure the runtime of executing async_comprehension
four times in parallel.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure and return the total runtime of executing async_comprehension
    four times concurrently.

    Returns:
        float: Total runtime in seconds.
    """
    start_time = time.time()
    # Run four instances of async_comprehension concurrently
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start_time

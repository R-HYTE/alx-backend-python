#!/usr/bin/env python3
"""
Module for measuring the average runtime of asynchronous tasks.
"""


import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure and return the average time per operation of asynchronous tasks.

    Args:
        n (int): The number of asynchronous operations.
        max_delay (int):  The maximum delay (s) to wait for each operation.

    Returns:
        float:  The average time taken per operation.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time) / n

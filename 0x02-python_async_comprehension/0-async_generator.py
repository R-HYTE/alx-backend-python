#!/usr/bin/env python3
"""
This module contains an asynchronous generator named async_generator.
The generator asynchronously yields random numbers between 0 and 10,
with a 1-second pause between each yield.
"""

import asyncio
import random


async def async_generator():
    """
    This function is an asynchronous generator that yields random numbers
    between 0 and 10, with a 1-second pause between each yield.

    Yields:
        A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

if __name__ == "__main__":
    asyncio.run(async_generator())

#!/usr/bin/env python3
"""
This module contains an asynchronous generator named async_generator.
The generator asynchronously yields random numbers between 0 and 10,
with a 1-second pause between each yield.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates a sequence of random numbers
    between 0 and 10, with a 1-second pause between each number.

    Returns:
        A float representing a random number between 0 and 10.

    Yields:
        A float representing a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

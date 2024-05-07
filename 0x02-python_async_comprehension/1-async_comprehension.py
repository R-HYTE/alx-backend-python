#!/usr/bin/env python3
"""
Module containing an asynchronous comprehension coroutine that collects
random numbers yielded from an asynchronous generator.
"""

import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """
    Asynchronously collects 10 random numbers using an async comprehension
    over an asynchronous generator, then returns the collected numbers.

    Returns:
        list: A list of 10 random numbers.
    """
    return [num async for num in async_generator()]

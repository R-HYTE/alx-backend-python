#!/usr/bin/env python3
"""Module for transforming a string and numerical input into a tuple."""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and a number into a tuple
    containing the string and the square of the number.

    Args:
    k (str): The string to be included in the tuple.
    v (Union[int, float]): The numerical value to be squared
                        and included in the tuple as a float.

    Returns:
    Tuple[str, float]: Tuple with the string and
                square of the number as a float.
    """
    return (k, (v ** 2))

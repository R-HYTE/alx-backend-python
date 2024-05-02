#!/usr/bin/env python3
"""Module to calculate the sum of a list of floating-point numbers.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floats.

    Args:
    input_list (List[float]): A list of floating-point numbers.

    Returns:
    float: The sum of all elements in the input list.
    """
    return sum(input_list)

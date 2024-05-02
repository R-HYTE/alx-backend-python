#!/usr/bin/env python3
"""Module to provide a floor function for float numbers."""

import math


def floor(n: float) -> int:
    """ Calculate the floor of a float number and return it as an integer.

    Args:
    n (float): The float number for which the floor is calculated.

    Returns:
    int: The floor value of the float.
    """
    return math.floor(n)

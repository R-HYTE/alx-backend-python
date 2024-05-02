#!/usr/bin/env python3
"""Module to generate multiplier functions."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a multiplier function that multiplies any float by a fixed multiplier.
        
    Args:
    multiplier (float): The multiplier to apply in the returned function.
        
    Returns:
    Callable[[float], float]: A function that takes a float and multiplies it by the multiplier.
    """
    return lambda x: x * multiplier

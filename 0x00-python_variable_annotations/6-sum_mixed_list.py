#!/usr/bin/env python3
"""Module to calculate the sum of lists containing mixed data types."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list containing both integers and floats.

    Args:
    mxd_lst (List[Union[int, float]]): A list of integers and floats.

    Return:
    float: The sum of all elements in the list.
    """
    return sum(mxd_lst)

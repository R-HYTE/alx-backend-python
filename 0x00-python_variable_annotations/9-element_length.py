#!/usr/bin/env python3
"""
Provides a function to calculate and
return the length of items in sequences as a list of tuples.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each sequence and
    its length from the input iterable of sequences.

    Args:
    lst (Iterable[Sequence]): An iterable of sequences to calculate lengths.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
    a sequence and its length.
    """
    return [(i, len(i)) for i in lst]

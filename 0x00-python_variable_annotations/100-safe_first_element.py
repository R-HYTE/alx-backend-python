#!/usr/bin/env python3
"""
Provides a function to safely retrieve the first element of any sequence,
returning None if empty.
"""
from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence, or None if the sequence is empty.

    Args:
    lst (Sequence[Any]): The sequence from which to extract the first element.

    Returns:
    Optional[Any]: The first element of the sequence or
                        None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
